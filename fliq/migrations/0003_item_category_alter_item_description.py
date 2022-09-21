# Generated by Django 4.1.1 on 2022-09-21 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fliq', '0002_alter_item_description_alter_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shirts'), ('H', 'Hoodies'), ('SW', 'Sweatpant')], default='p', max_length=200),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
