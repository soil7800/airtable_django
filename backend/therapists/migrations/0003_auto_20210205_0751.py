# Generated by Django 3.1.6 on 2021-02-05 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapists', '0002_auto_20210205_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='therapist',
            name='method',
            field=models.ManyToManyField(blank=True, to='therapists.Method'),
        ),
        migrations.AlterField(
            model_name='therapist',
            name='photo_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]