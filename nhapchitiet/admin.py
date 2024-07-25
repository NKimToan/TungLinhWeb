from django.contrib import admin
from .models import Nhapchitiet
# Register your models here.
class NhapchitietAdmin(admin.ModelAdmin):
    list_display = ("id","ma_hh","ma_phieu_nk","so_luong","thanh_tien")
    search_fields = ['id']
    list_filter = ("id","ma_hh","ma_phieu_nk","so_luong","thanh_tien")
admin.site.register(Nhapchitiet,NhapchitietAdmin)