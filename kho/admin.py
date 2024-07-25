from django.contrib import admin
from .models import Kho
# Register your models here.
class KhoAdmin(admin.ModelAdmin):
    list_display = ('ma_kho','dia_diem_kho')
    search_fields = ['dia_diem_kho']
    list_filter = ('ma_kho','dia_diem_kho')
admin.site.register(Kho,KhoAdmin)

# Tài khoản của các nhân viên kho
# Nhanvienkho1
# username: Nhanvienkho1
# pass: Kho1@gmail.com
# Nhanvienkho2
# username: Nhanvienkho2
# pass: Kho2@gmail.com