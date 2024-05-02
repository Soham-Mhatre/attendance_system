# Generated by Django 5.0.3 on 2024-04-23 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barcode_app', '0017_rename_s13s14_rb0001s13s14'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rb0002s91s92',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rollno', models.CharField(max_length=100)),
                ('present', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameModel(
            old_name='Rb0001s13s14',
            new_name='Rb0002s13s14',
        ),
    ]
