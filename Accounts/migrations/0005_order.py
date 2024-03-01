# Generated by Django 5.0.1 on 2024-03-01 08:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_address'),
        ('Components', '0020_alter_product_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.PositiveIntegerField(default=1)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Time', models.DateTimeField(auto_now_add=True)),
                ('Pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Components.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
