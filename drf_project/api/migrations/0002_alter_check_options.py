# Generated by Django 5.0.6 on 2024-06-24 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='check',
            options={'verbose_name': 'Запрос к сайту', 'verbose_name_plural': 'Запросы к сайту'},
        ),
    ]