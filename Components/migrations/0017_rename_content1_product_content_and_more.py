# Generated by Django 5.0.1 on 2024-02-27 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Components', '0016_delete_active_delete_display_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='content1',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='product',
            name='content2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='content3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='content4',
        ),
        migrations.RemoveField(
            model_name='product',
            name='content5',
        ),
        migrations.RemoveField(
            model_name='product',
            name='heading',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image5',
        ),
    ]