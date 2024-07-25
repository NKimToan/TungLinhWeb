from django.contrib import admin
from .models import Nguoigiaohang
# Register your models here.
class NguoigiaohangAdmin(admin.ModelAdmin):
    list_display = ('ma_ngh','ten_ngh')
    search_fields = ['ten_ngh']
    list_filter = ('ma_ngh','ten_ngh')
admin.site.register(Nguoigiaohang,NguoigiaohangAdmin)