# Generated by Django 3.0.6 on 2020-09-05 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0013_orderupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='phone_no',
            field=models.IntegerField(default=0),
        ),
    ]