# Generated by Django 2.1.15 on 2023-11-12 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nguoigiaohang', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nguoigiaohang',
            name='ma_ngh',
            field=models.CharField(db_column='Ma_nguoi_giao_hang', max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='nguoigiaohang',
            name='ten_ngh',
            field=models.CharField(db_column='Ten_nguoi_giao_hang', max_length=50),
        ),
    ]
