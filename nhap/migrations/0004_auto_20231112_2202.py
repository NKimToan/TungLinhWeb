# Generated by Django 2.1.15 on 2023-11-12 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nhap', '0003_auto_20231112_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nhap',
            name='ma_phieu_nk',
            field=models.CharField(db_column='Ma_phieu_nhap_kho', max_length=10, primary_key=True, serialize=False),
        ),
    ]
