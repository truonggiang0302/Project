# Generated by Django 3.1.3 on 2020-11-20 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20201119_2142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(verbose_name='Số lượng')),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_phone', models.CharField(max_length=20)),
                ('customer_address', models.CharField(max_length=200)),
                ('order_date', models.DateTimeField()),
                ('deliver_date', models.DateTimeField(null=True)),
                ('status', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.product')),
            ],
        ),
    ]
