# Generated by Django 3.0.7 on 2020-08-17 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0010_auto_20200817_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='lineitem_nondel_total',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=6),
        ),
    ]
