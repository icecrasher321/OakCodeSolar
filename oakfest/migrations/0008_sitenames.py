# Generated by Django 2.1.5 on 2019-01-19 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oakfest', '0007_auto_20190119_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='oakfest.Site')),
            ],
        ),
    ]
