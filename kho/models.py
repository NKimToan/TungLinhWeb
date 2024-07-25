from django.db import models

# Create your models here.
class Kho(models.Model):
    ma_kho = models.CharField(db_column='Ma_kho', primary_key=True, max_length=10)  # Field name made lowercase.
    dia_diem_kho = models.CharField(db_column='Dia_diem_kho', max_length=100, null=False)  # Field name made lowercase.
    
    class Meta:
        db_table = 'Kho'
        
    def __str__(self):
        return f"{self.ma_kho},{self.dia_diem_kho}"