# Generated by Django 3.1.7 on 2021-06-18 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_of_user', '0003_auto_20210618_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='pub_date',
        ),
    ]
