# Generated by Django 5.0.3 on 2024-04-22 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barcode_app', '0014_s3s4_rename_barcdeo_app_s3s4_barcode_app_s3s4'),
    ]

    operations = [
        migrations.CreateModel(
            name='barcode_app_sg0001s5s6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rollno', models.CharField(max_length=100)),
                ('present', models.BooleanField(default=False)),
            ],
        ),
    ]