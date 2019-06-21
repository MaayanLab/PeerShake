# Generated by Django 2.2.2 on 2019-06-20 14:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('PeerShakeWeb', '0008_chromeextension_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chromeextension',
            name='datetime',
        ),
        migrations.AddField(
            model_name='chromeextension',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
