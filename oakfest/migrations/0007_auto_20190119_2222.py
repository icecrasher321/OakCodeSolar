# Generated by Django 2.1.5 on 2019-01-19 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oakfest', '0006_auto_20190119_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sites', to=settings.AUTH_USER_MODEL),
        ),
    ]