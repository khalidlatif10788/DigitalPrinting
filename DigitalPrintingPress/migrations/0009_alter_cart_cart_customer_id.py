# Generated by Django 3.2.4 on 2022-06-24 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DigitalPrintingPress', '0008_auto_20220624_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]