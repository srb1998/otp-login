# Generated by Django 4.1.4 on 2023-01-22 20:02

import app.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_user_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', app.manager.UserManager()),
            ],
        ),
    ]
