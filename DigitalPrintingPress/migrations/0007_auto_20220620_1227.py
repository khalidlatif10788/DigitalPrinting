# Generated by Django 3.2.4 on 2022-06-20 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DigitalPrintingPress', '0006_productdetail_detail_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart_product_detail_id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product_description',
        ),
        migrations.AddField(
            model_name='cart',
            name='description_detail',
            field=models.TextField(default='', max_length=3000),
        ),
        migrations.AddField(
            model_name='cart',
            name='descripton_title',
            field=models.CharField(default='', max_length=3000),
        ),
    ]
