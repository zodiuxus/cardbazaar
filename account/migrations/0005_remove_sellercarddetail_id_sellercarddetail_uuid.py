# Generated by Django 4.2.4 on 2023-08-29 17:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_sellercarddetail_date_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellercarddetail',
            name='id',
        ),
        migrations.AddField(
            model_name='sellercarddetail',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
