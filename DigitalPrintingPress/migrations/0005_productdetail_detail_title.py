# Generated by Django 4.0.4 on 2022-06-19 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DigitalPrintingPress', '0004_remove_productdetail_detail_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetail',
            name='detail_title',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
