# Generated by Django 4.2.4 on 2023-08-29 18:29

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_sellercarddetail_id_sellercarddetail_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellercarddetail',
            name='card_image',
            field=models.ImageField(blank=True, upload_to=account.models.user_dir_upload, verbose_name='OPTIONAL, card images do not need to be supplied, but sellers are encouraged to do so.'),
        ),
    ]
