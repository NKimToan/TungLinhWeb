# Generated by Django 2.1.15 on 2023-11-13 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nhap', '0004_auto_20231112_2202'),
        ('hanghoa', '0002_auto_20231112_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phieunhapchitiet',
            fields=[
                ('id', models.IntegerField(db_column='So_thu_tu', primary_key=True, serialize=False)),
                ('so_luong', models.IntegerField(db_column='So_luong')),
                ('thanh_tien', models.DecimalField(db_column='Thanh_tien', decimal_places=0, max_digits=12)),
                ('ma_hh', models.ForeignKey(db_column='Ma_hang_hoa', default=None, max_length=10, on_delete=django.db.models.deletion.CASCADE, to='hanghoa.Hanghoa')),
                ('ma_phieu_nk', models.ForeignKey(db_column='Ma_phieu_nhap_kho', default=None, on_delete=django.db.models.deletion.CASCADE, to='nhap.Nhap')),
            ],
            options={
                'db_table': 'PhieuNhapChiTiet',
            },
        ),
        migrations.AlterUniqueTogether(
            name='phieunhapchitiet',
            unique_together={('ma_hh', 'ma_phieu_nk')},
        ),
    ]
