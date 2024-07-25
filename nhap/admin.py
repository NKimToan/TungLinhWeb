from django.contrib import admin
from .models import Nhap
# Register your models here.
class NhapAdmin(admin.ModelAdmin):
    list_display = ("ma_phieu_nk","ma_nguoi_giao_hang","ma_kho","thuc_nhap","tong_cong")
    search_fields = ['ma_phieu_nk']
    list_filter = ("ma_phieu_nk","ma_nguoi_giao_hang","ma_kho","thuc_nhap","tong_cong")
admin.site.register(Nhap,NhapAdmin)

# Tài khoản của bộ phận nhập hàng
# Username: Nhanviennhap1
# pass: Nhap1@gmail.com
# Username: Nhanviennhap2
# pass: Nhap2@gmail.com