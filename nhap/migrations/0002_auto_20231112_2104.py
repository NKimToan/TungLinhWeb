# Generated by Django 2.1.15 on 2023-11-12 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nhap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nhap',
            name='ma_nguoi_giao_hang',
            field=models.ForeignKey(db_column='Ma_nguoi_giao_hang', max_length=10, on_delete=django.db.models.deletion.CASCADE, to='nguoigiaohang.Nguoigiaohang'),
        ),
    ]
