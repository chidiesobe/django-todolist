# Generated by Django 3.1.2 on 2021-10-19 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20211019_1811'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='datecomplete',
            new_name='dateCompleted',
        ),
    ]
