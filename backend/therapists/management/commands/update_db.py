import requests
import datetime

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from therapists.models import Therapist, Method, RawAirtableData

API_KEY = settings.AIRTABLE_API_KEY


class Command(BaseCommand):

    def handle(self, *args, **options):
        airtable_all_records = self.get_airtable_records()
        airtable_updated_records = self.get_airtable_records(updated=True)
        airtable_id_set = [item['id'] for item in airtable_all_records]
        self.delete_records(airtable_id_set)
        self._save_raw_airtable_data(airtable_all_records)
        if airtable_updated_records:
            updated_list, created_list = self.update_database(airtable_updated_records)
            self.stdout.write(self.style.SUCCESS(f"Данные успешно обновлены"))
        else:
            self.stdout.write(self.style.SUCCESS("Нет данных для обновления"))
        
    
    def _get_url(self):
        table_id = settings.AIRTABLE_TABLE_BASE_ID
        table_name = settings.AIRTABLE_TABLE_NAME
        if not table_id or not table_name:
            raise CommandError('Не заданы имя и/или id таблицы airtable')
        url = 'https://api.airtable.com/v0/' + table_id + '/' + table_name
        return url

    def _get_uri_params(self, updated=True):
        if not RawAirtableData.objects.all():
            return {}
        last_updated = RawAirtableData.objects.last().created.isoformat()
        params = {
            'filterByFormula': f'LAST_MODIFIED_TIME() > "{last_updated}"', 
        }
        return params if updated else {}
    
    def get_airtable_records(self, updated=False):
        aritable_records = []
        url = self._get_url()
        headers = {'Authorization': 'Bearer '+API_KEY, }
        params = self._get_uri_params(updated=updated)
        while True:
            response = requests.get(url=url, params=params, headers=headers)
            aritable_records += response.json().get('records')
            if response.json().get('offset'):
                params['offset'] = str(response.json().get('offset'))
            else:
                break
        return aritable_records

    def update_database(self, data):
        updated_list = []
        created_list = []
        for record in data:
            date = datetime.datetime.strptime(
                    record.get('createdTime'), 
                    '%Y-%m-%dT%H:%M:%S.%fZ')
            try:
                photo_data = record.get('fields').get('Фотография')[0].get('url')
            except TypeError:
                photo_data = None
            therapist, therapist_status = Therapist.objects.update_or_create(
                id=record.get('id'),
                defaults={
                    'name': record.get('fields').get('Имя'),
                    'photo_url': photo_data,
                    'created': timezone.make_aware(date)
                },
            )
            method_set = record.get('fields').get('Методы', [])
            therapist.method.remove(*therapist.method.all().exclude(title__in=method_set))
            if method_set:
                for title in method_set:
                    method, created = Method.objects.get_or_create(title=title)
                    therapist.method.add(method)
            if therapist_status:
                created_list.append(therapist.name)
            else:
                updated_list.append(therapist.name)
        if updated_list:
            self.stdout.write(self.style.SUCCESS('Обновлены следующие записи:'))
            for obj in updated_list:
                self.stdout.write(f'\t- {obj}')
        if created_list:
            self.stdout.write(self.style.SUCCESS('Созданы следующие записи:'))
            for obj in created_list:
                self.stdout.write(f'\t- {obj}')
        return updated_list, created_list

    def _save_raw_airtable_data(self, data):
        obj = RawAirtableData.objects.create(airtable_data=data)

    def delete_records(self, id_list):
        objects = Therapist.objects.exclude(id__in=id_list)
        if objects:
            self.stdout.write(self.style.SUCCESS('Удалены следующие записи:'))
            for obj in objects:
                self.stdout.write(f'\t- {obj}')
                objects.delete()
        