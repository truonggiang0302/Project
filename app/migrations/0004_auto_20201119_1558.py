# Generated by Django 3.1.3 on 2020-11-19 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201119_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, max_length=30, verbose_name='Màu sắc'),
        ),
    ]