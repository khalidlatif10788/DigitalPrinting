# Generated by Django 3.2.4 on 2022-09-02 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DigitalPrintingPress', '0013_order_transcation_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='adressid',
            field=models.IntegerField(default=0, verbose_name=models.IntegerField(default=0, null=True)),
            preserve_default=False,
        ),
    ]
