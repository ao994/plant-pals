# Generated by Django 3.1.7 on 2021-06-19 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_of_user', '0010_post_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
