# Generated by Django 5.0.1 on 2024-02-04 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Components', '0008_display'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, unique=True)),
                ('heading', models.CharField(max_length=100)),
                ('content1', models.TextField(blank=True)),
                ('content2', models.TextField(blank=True)),
                ('content3', models.TextField(blank=True)),
                ('content4', models.TextField(blank=True)),
                ('content5', models.TextField(blank=True)),
                ('background_image', models.ImageField(blank=True, upload_to='Sensor/')),
                ('image1', models.ImageField(blank=True, upload_to='Sensor/')),
                ('image2', models.ImageField(blank=True, upload_to='Sensor/')),
                ('image3', models.ImageField(blank=True, upload_to='Sensor/')),
                ('image4', models.ImageField(blank=True, upload_to='Sensor/')),
                ('image5', models.ImageField(blank=True, upload_to='Sensor/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
