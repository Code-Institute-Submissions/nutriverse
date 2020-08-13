# Generated by Django 3.0.7 on 2020-08-10 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20200810_1408'),
        ('checkout', '0004_auto_20200810_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='product_size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Sizes'),
        ),
    ]