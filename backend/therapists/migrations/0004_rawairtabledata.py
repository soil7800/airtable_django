# Generated by Django 3.1.6 on 2021-02-05 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapists', '0003_auto_20210205_0751'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawAirtableData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('airtable_data', models.JSONField()),
            ],
        ),
    ]