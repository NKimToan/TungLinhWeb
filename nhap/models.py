from django.db import models
from kho.models import Kho
from nguoigiaohang.models import Nguoigiaohang
# # Create your models here.
class Nhap(models.Model):
    ma_phieu_nk = models.CharField(db_column='Ma_phieu_nhap_kho', primary_key=True, max_length=10)
    ma_nguoi_giao_hang = models.ForeignKey(Nguoigiaohang, db_column='Ma_nguoi_giao_hang', max_length=10, on_delete=models.CASCADE, to_field='ma_ngh')
    ma_kho = models.ForeignKey(Kho, default=None, max_length=10, db_column='Ma_kho', on_delete=models.CASCADE, to_field='ma_kho')
    thuc_nhap = models.IntegerField(db_column='Thuc_nhap', null=True) 
    tong_cong = models.DecimalField(db_column='Tong_cong', max_digits=12, decimal_places=0, null=True) 

    class Meta:
        db_table = 'Nhap'

    def __str__(self):
        return f"{self.ma_phieu_nk},{self.ma_nguoi_giao_hang},{self.ma_kho},{self.thuc_nhap},{self.tong_cong}"