# Generated by Django 2.2.2 on 2019-06-05 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paperTitle', models.CharField(max_length=5000)),
                ('paperAuthors', models.CharField(max_length=5000)),
                ('paperDOI', models.IntegerField()),
                ('paperSubject', models.CharField(max_length=5000)),
            ],
        ),
    ]
