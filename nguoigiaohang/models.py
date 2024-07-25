from django.db import models

# Create your models here.
class Nguoigiaohang(models.Model):
    ma_ngh = models.CharField(primary_key=True, max_length=10, db_column='Ma_nguoi_giao_hang')
    ten_ngh = models.CharField(max_length=50, db_column='Ten_nguoi_giao_hang')

    class Meta:
        db_table = 'NguoiGiaoHang'

    def __str__(self):
        return f'{self.ma_ngh},{self.ten_ngh}'