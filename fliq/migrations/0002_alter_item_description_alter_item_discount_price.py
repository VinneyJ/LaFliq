# Generated by Django 4.1.1 on 2022-09-21 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fliq', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='discount_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]