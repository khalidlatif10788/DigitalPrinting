# Generated by Django 3.2.4 on 2022-06-13 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_description', models.TextField(max_length=5000)),
                ('qty', models.IntegerField()),
                ('totalamount', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
                ('textprint', models.CharField(max_length=100)),
                ('cart_photo', models.ImageField(default='default.jpg', upload_to='uploads/cart')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=25)),
                ('billing_address', models.TextField(max_length=500, null=True)),
                ('shipping_address', models.TextField(max_length=500, null=True)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='MainCategoery',
            fields=[
                ('main_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('main_category_name', models.CharField(max_length=100)),
                ('main_category_photo', models.ImageField(default='default.jpg', upload_to='uploads/mainCategory')),
            ],
            options={
                'db_table': 'main_category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_description', models.TextField(max_length=5000)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('product_discount', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
                ('product_photo', models.ImageField(default='default.jpg', upload_to='uploads/product')),
                ('product_main_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DigitalPrintingPress.maincategoery')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('sub_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_category_name', models.CharField(max_length=100)),
                ('sub_category_photo', models.ImageField(default='default.jpg', upload_to='uploads/subCategory')),
                ('sub_main_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DigitalPrintingPress.maincategoery')),
            ],
            options={
                'db_table': 'sub_category',
            },
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('product_detail_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('detail_title', models.CharField(max_length=1000)),
                ('detail_description', models.TextField(max_length=5000)),
                ('detail_product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DigitalPrintingPress.product')),
            ],
            options={
                'db_table': 'product_detail',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_sub_category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DigitalPrintingPress.subcategory'),
        ),
        migrations.AddIndex(
            model_name='maincategoery',
            index=models.Index(fields=['main_category_id'], name='pk_main_category'),
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DigitalPrintingPress.customer'),
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_product_detail_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DigitalPrintingPress.productdetail'),
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DigitalPrintingPress.product'),
        ),
        migrations.AddIndex(
            model_name='subcategory',
            index=models.Index(fields=['sub_category_id'], name='pk_sub_category'),
        ),
        migrations.AddIndex(
            model_name='subcategory',
            index=models.Index(fields=['sub_main_category_id'], name='fk_main_category'),
        ),
        migrations.AddIndex(
            model_name='productdetail',
            index=models.Index(fields=['product_detail_id'], name='pk_product_detail'),
        ),
        migrations.AddIndex(
            model_name='productdetail',
            index=models.Index(fields=['detail_product_id'], name='fk_product'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['product_id'], name='pk_product'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['product_sub_category_id'], name='fk_sub_category'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['product_main_category_id'], name='fk_product_main_category'),
        ),
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['customer_id'], name='pk_customer'),
        ),
    ]
