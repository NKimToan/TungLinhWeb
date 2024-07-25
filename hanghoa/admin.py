from django.contrib import admin
from .models import Hanghoa
# Register your models here.
class HanghoaAdmin(admin.ModelAdmin):
    list_display = ('ma_hh','ten_hh','so_luong','don_gia')
    search_fields = ['ten_hh']
    list_filter = ('ma_hh','ten_hh','so_luong','don_gia')
admin.site.register(Hanghoa,HanghoaAdmin)