# Generated by Django 3.0.6 on 2020-07-16 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_auto_20200714_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='author',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
