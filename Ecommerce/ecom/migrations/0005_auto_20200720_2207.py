# Generated by Django 3.0.6 on 2020-07-20 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0004_auto_20200720_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]