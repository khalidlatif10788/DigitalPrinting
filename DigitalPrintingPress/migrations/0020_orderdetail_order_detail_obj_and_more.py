# Generated by Django 4.0.4 on 2022-09-25 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DigitalPrintingPress', '0019_alter_order_adressid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='order_detail_obj',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='DigitalPrintingPress.order'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='product_main_category_id',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='DigitalPrintingPress.maincategoery'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_sub_category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DigitalPrintingPress.subcategory'),
        ),
    ]