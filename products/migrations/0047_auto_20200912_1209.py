# Generated by Django 3.0.7 on 2020-09-12 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0046_auto_20200910_2151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='user',
            new_name='user_profile',
        ),
    ]