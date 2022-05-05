# Generated by Django 4.0.4 on 2022-05-04 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='office name')),
                ('street', models.CharField(max_length=64, verbose_name='street')),
                ('city', models.CharField(max_length=32, verbose_name='city')),
                ('zipcode', models.CharField(max_length=10, verbose_name='zipcode')),
                ('phone', models.CharField(max_length=10, verbose_name='phone number')),
            ],
        ),
    ]
