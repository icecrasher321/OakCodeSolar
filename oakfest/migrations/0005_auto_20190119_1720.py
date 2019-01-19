# Generated by Django 2.1.5 on 2019-01-19 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oakfest', '0004_auto_20190119_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='User',
        ),
        migrations.AddField(
            model_name='site',
            name='user',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
