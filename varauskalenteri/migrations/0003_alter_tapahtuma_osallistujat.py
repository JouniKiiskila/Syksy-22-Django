# Generated by Django 4.1.1 on 2022-09-19 12:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('varauskalenteri', '0002_tapahtuma_osallistujat_tapahtuma_paikkoja'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tapahtuma',
            name='osallistujat',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
