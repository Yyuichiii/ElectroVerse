# Generated by Django 5.0.1 on 2024-02-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Components', '0017_rename_content1_product_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='content',
            field=models.TextField(),
        ),
    ]