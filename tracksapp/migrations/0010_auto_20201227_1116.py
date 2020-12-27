# Generated by Django 3.1.4 on 2020-12-27 09:16

from django.db import migrations, models
import tracksapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('tracksapp', '0009_tracksapp_pathname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracksapp',
            old_name='description',
            new_name='description_in_detail',
        ),
        migrations.RenameField(
            model_name='tracksapp',
            old_name='pathname',
            new_name='description_in_list',
        ),
        migrations.RenameField(
            model_name='tracksapp',
            old_name='image',
            new_name='image_in_list',
        ),
        migrations.AddField(
            model_name='tracksapp',
            name='image_in_detail',
            field=models.ImageField(default='', upload_to=tracksapp.models.image_upload_detail),
            preserve_default=False,
        ),
    ]
