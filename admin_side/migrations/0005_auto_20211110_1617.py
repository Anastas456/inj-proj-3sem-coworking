# Generated by Django 3.1.7 on 2021-11-10 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0004_auto_20210412_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenants',
            name='phone',
            field=models.CharField(max_length=255),
        ),
    ]
