# Generated by Django 5.0.1 on 2024-02-03 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Components', '0003_delete_passivetype_remove_passive_h3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='passive',
            name='type',
            field=models.CharField(default=1, max_length=10, unique=True),
            preserve_default=False,
        ),
    ]
