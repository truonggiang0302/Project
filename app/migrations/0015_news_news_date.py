# Generated by Django 3.1.3 on 2021-03-05 10:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_news_content_sumarize'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]