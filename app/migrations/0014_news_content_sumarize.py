# Generated by Django 3.1.3 on 2021-03-05 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='content_sumarize',
            field=models.CharField(default='', max_length=500, verbose_name='Tóm tắt tiêu đề'),
        ),
    ]