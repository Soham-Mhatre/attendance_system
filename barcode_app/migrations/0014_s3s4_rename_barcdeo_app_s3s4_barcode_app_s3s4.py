# Generated by Django 5.0.3 on 2024-04-22 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barcode_app', '0013_rename_barcode_app_sg0001s3s4_barcdeo_app_s3s4'),
    ]

    operations = [
        migrations.CreateModel(
            name='s3s4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rollno', models.CharField(max_length=100)),
                ('present', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameModel(
            old_name='barcdeo_app_s3s4',
            new_name='barcode_app_s3s4',
        ),
    ]
