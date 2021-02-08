# airtable_django
Демо - http://35.228.202.163/

Синхронизация базы данных с airtable:
1. Указать ``AIRTABLE_TABLE_BASE_ID``, ``AIRTABLE_TABLE_NAME``, ``AIRTABLE_API_KEY`` в файле .env
2. Выполнить ``python manage.py update_db`` для загрузки данных из airtable и записи в базу данных 
