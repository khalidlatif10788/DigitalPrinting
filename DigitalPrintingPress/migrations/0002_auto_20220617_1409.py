# Generated by Django 3.2.4 on 2022-06-17 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DigitalPrintingPress', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdetail',
            name='detail_description',
        ),
        migrations.CreateModel(
            name='ProductDescription',
            fields=[
                ('product_description_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('detail_Description', models.CharField(max_length=1000)),
                ('des_product_detail_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DigitalPrintingPress.productdetail')),
            ],
            options={
                'db_table': 'product_description',
            },
        ),
        migrations.AddIndex(
            model_name='productdescription',
            index=models.Index(fields=['product_description_id'], name='pk_product_description'),
        ),
        migrations.AddIndex(
            model_name='productdescription',
            index=models.Index(fields=['des_product_detail_id'], name='fk_product_detail'),
        ),
    ]
