# Generated by Django 5.0.1 on 2024-02-27 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Components', '0018_alter_product_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='P_name',
            field=models.CharField(max_length=200, verbose_name='Product Name'),
        ),
    ]
