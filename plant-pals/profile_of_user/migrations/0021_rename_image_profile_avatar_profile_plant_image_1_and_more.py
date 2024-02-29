# Generated by Django 5.0.1 on 2024-02-02 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_of_user', '0020_auto_20210621_1159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='avatar',
        ),
        migrations.AddField(
            model_name='profile',
            name='plant_image_1',
            field=models.ImageField(default='', upload_to='additional_images'),
        ),
        migrations.AddField(
            model_name='profile',
            name='plant_name_1',
            field=models.CharField(default='', max_length=60),
        ),
    ]
