# Generated by Django 3.0.7 on 2020-08-03 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200725_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subscription_type',
        ),
    ]
