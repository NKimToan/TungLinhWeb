from django.db import models
from hanghoa.models import Hanghoa
from nhap.models import Nhap
# Create your models here.
class Nhapchitiet(models.Model):
    id = models.IntegerField(primary_key=True, db_column='So_thu_tu')
    ma_hh = models.ForeignKey(Hanghoa, on_delete=models.CASCADE, db_column='Ma_hang_hoa', max_length=10, default=None) 
    ma_phieu_nk = models.ForeignKey(Nhap, on_delete=models.CASCADE, db_column='Ma_phieu_nhap_kho', default=None) 
    so_luong = models.IntegerField(db_column='So_luong') 
    thanh_tien = models.DecimalField(db_column='Thanh_tien', max_digits=12, decimal_places=0) 
    
    class Meta:
        db_table = 'NhapChiTiet'
        unique_together = ('ma_hh','ma_phieu_nk')
        
    def __str__(self):
        return f'{self.id},{self.ma_hh},{self.ma_phieu_nk},{self.so_luong},{self.thanh_tien}'