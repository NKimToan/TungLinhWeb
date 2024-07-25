from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Kho as Kho_models
from nhap.models import Nhap as Nhap_models
# Kiểm soát quyền truy cập
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponse
# Kiểm soát người xem
def can_view_kho(user):
    return user.has_perm('kho.get_kho')

# Kiểm soát người thêm dữ liệu
def can_add_kho(user):
    return user.has_perm('kho.add_kho')

# Kiểm soát người chỉnh sửa dữ liệu
def can_change_kho(user):
    return user.has_perm('kho.change_kho')

# Kiểm soát người xóa dữ liệu
def can_delete_kho(user):
    return user.has_perm('kho.delete_kho')

# Create your views here.
def get_kho(request):
    kho_list = Kho_models.objects.filter().order_by('ma_kho')
    return render(request,'kho.html',{'kho_list':kho_list})

@user_passes_test(can_add_kho, login_url='/kho/')

def add_kho(request):
    if request.method == 'POST':
        Ma_kho = request.POST['ma_kho']
        Dia_diem_kho =request.POST['dia_diem_kho']
        if Kho_models.objects.filter(ma_kho = Ma_kho).exists():
            messages.error(request, 'Mã kho đã tồn tại')
        else:
            if Ma_kho != '' and len(Ma_kho) == 10:
                kho = Kho_models.objects.create(ma_kho = Ma_kho,
                                                dia_diem_kho = Dia_diem_kho)
                messages.success(request,'Thêm kho thành công')
            else:
                messages.error(request, 'Mã kho sai định dạng')
        return redirect('kho/')
    else:
        return render(request,'error.html')

# Kiểm soát người chỉnh sửa dữ liệu
def can_change_kho(user):
    return user.has_perm('kho.change_kho')

def get_kho_change(request,id):
    kho_list = Kho_models.objects.filter(ma_kho=id)
    return render(request,'kho_update.html',{'kho_list':kho_list})

@user_passes_test(can_change_kho, login_url='/kho/')

def change_kho(request):
    if request.method == 'POST':
        try:
            ma_kho = request.POST['ma_kho']
            dia_diem_kho = request.POST['dia_diem_kho']
            kho = Kho_models.objects.get(ma_kho = ma_kho)
            kho.dia_diem_kho = dia_diem_kho
            kho.save()
            return redirect('kho/')
        except Exception as e:
            return render(request,'error.html')
    else:
        return render(request,'error.html')


def get_kho_delete(request):
    kho_list = Kho_models.objects.filter()
    nhap_list = Nhap_models.objects.filter()
    return render(request,'kho.html',{'kho_list':kho_list, 'nhap_list':nhap_list})

@user_passes_test(can_delete_kho, login_url='/kho/')

def delete_kho(request):
    if request.method == 'POST':
        try:
            ma_kho = request.POST['ma_kho_xoa']
            kho = Kho_models.objects.get(ma_kho = ma_kho)
            if Nhap_models.objects.filter(ma_kho = ma_kho).exists():
                messages.error(request, 'Mã kho đang được sử dụng trong phiếu nhập')
            else:
                kho.delete()
            return redirect('kho/')
        except Exception as e:
            return render(request,'error.html')
    else:
        return render(request,'error.html')
    
def get_kho_search(request,id):
    kho_list = Kho_models.objects.filter(ma_kho = id).order_by('ma_kho')
    return render(request,'kho_search.html',{'kho_list':kho_list})

def search_kho(request):
    if request.method == 'POST':
        try:
            mk = request.POST['ma_kho']
            kho = Kho_models.objects.get(ma_kho = mk)
        except Exception as e:
            respone = HttpResponse()
            respone.writelines('<h1>Mã kho không tồn tại</h1>')
            respone.writelines('<a href="/kho">Trở về trang kho</a>')
            return respone
        return redirect('khoSearch/'+mk+'/')
    else:
        return render(request,'error.html')