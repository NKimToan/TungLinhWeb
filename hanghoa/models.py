from django.db import models

# Create your models here.
class Hanghoa(models.Model):
    ma_hh = models.CharField(db_column='Ma_hang_hoa', primary_key=True, max_length=10)
    ten_hh = models.CharField(db_column='Ten_hang_hoa',max_length=50)
    so_luong = models.IntegerField(db_column='So_luong', null=True)
    don_gia = models.DecimalField(db_column='Don_gia', max_digits=12, decimal_places=0)

    class Meta:
        db_table = 'HangHoa'

    def __str__(self):
        return f'{self.ma_hh},{self.ten_hh},{self.so_luong},{self.don_gia}'
