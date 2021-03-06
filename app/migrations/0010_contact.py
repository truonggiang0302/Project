# Generated by Django 3.1.3 on 2020-11-27 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_email', models.CharField(max_length=20)),
                ('customer_address', models.CharField(max_length=200)),
                ('order_date', models.DateTimeField()),
            ],
        ),
    ]
