# Generated by Django 3.1.4 on 2020-12-02 11:09

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('mainadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='image',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
