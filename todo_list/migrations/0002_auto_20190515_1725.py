# Generated by Django 2.2.1 on 2019-05-15 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='content',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='list',
            name='item',
            field=models.CharField(default='', max_length=200),
        ),
    ]
