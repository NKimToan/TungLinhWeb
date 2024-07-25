from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Nhap as Nhap_models
from kho.models import Kho as Kho_models
from nguoigiaohang.models import Nguoigiaohang as Nguoigiaohang_models
from nhapchitiet.models import Nhapchitiet as Nhapchitiet_models
from django.http import HttpResponse
# Kiểm soát quyền truy cập
from django.contrib.auth.decorators import user_passes_test
def can_view_nhap(user):
    return user.has_perm('nhap.get_nhap')

# Hàm xác thực quyền truy cập để thêm dữ liệu 
def can_add_nhap(user):
    return user.has_perm('nhap.add_nhap')

# Hàm xác thực quyền truy cập để chỉnh sửa dữ liệu 
def can_change_nhap(user):
    return user.has_perm('nhap.change_nhap')

# Hàm xác thực quyền truy cập để xóa dữ liệu 
def can_delete_nhap(user):
    return user.has_perm('nhap.delete_nhap')

# Create your views here.
def get_nhap(request):
    nhap_list = Nhap_models.objects.filter().order_by('ma_phieu_nk')
    kho_list = Kho_models.objects.filter()
    nguoigiaohang_list = Nguoigiaohang_models.objects.filter()
    return render(request,'nhap.html',{'nhap_list':nhap_list, 'kho_list':kho_list, 'nguoigiaohang_list':nguoigiaohang_list})

@user_passes_test(can_add_nhap, login_url='/nhap/')

def add_nhap(request):
    if request.method == 'POST':
        Ma_phieu_nk = request.POST['ma_phieu_nk']
        Ma_nguoi_giao_hang =request.POST['ma_nguoi_giao_hang']
        Ma_kho = request.POST['ma_kho']
        if Nhap_models.objects.filter(ma_phieu_nk = Ma_phieu_nk).exists():
            messages.error(request, 'Mã phiếu nhập kho đã tồn tại')
        elif not Kho_models.objects.filter(ma_kho = Ma_kho).exists():
            messages.error(request, 'Mã kho không tồn tại')
        elif not Nguoigiaohang_models.objects.filter(ma_ngh = Ma_nguoi_giao_hang).exists():
            messages.error(request, 'Mã người giao hàng không tồn tại')
        else:
            if Ma_phieu_nk != '' and len(Ma_phieu_nk) == 10:
                Ma_Kho = Kho_models.objects.get(ma_kho = Ma_kho)
                Ma_NGH = Nguoigiaohang_models.objects.get(ma_ngh = Ma_nguoi_giao_hang)
                nhap = Nhap_models.objects.create(ma_phieu_nk = Ma_phieu_nk,
                                                ma_nguoi_giao_hang = Ma_NGH,
                                                ma_kho = Ma_Kho)
                messages.success(request,'Thêm phiếu nhập kho thành công')
            else:
                messages.error(request, 'Mã phiếu nhập kho sai định dạng')
        return redirect('nhap/')
    else:
        return render(request,'error.html')
    
def get_nhap_change(request,id):
    nhap_list = Nhap_models.objects.filter(ma_phieu_nk = id)
    kho_list = Kho_models.objects.filter()
    nguoigiaohang_list = Nguoigiaohang_models.objects.filter()
    return render(request,'nhap_update.html',{'nhap_list':nhap_list, 'kho_list':kho_list, 'nguoigiaohang_list':nguoigiaohang_list})

@user_passes_test(can_change_nhap, login_url='/nhap/')

def change_nhap(request):
    if request.method == 'POST':
        try:
            Ma_phieu_nk = request.POST['ma_phieu_nk']
            Ma_nguoi_giao_hang =request.POST['ma_nguoi_giao_hang']
            Ma_kho = request.POST['ma_kho']
            Ma_Kho = Kho_models.objects.get(ma_kho = Ma_kho)
            Ma_NGH = Nguoigiaohang_models.objects.get(ma_ngh = Ma_nguoi_giao_hang)
            nhap = Nhap_models.objects.get(ma_phieu_nk = Ma_phieu_nk)
            nhap.ma_nguoi_giao_hang = Ma_NGH
            nhap.ma_kho = Ma_Kho
            nhap.save()
            return redirect('nhap/')
        except Exception as e:
            return render(request,'error.html')
    else:
        return render(request,'error.html')

def get_nhap_delete(request):
    nhap_list = Nhap_models.objects.filter()
    kho_list = Kho_models.objects.filter()
    nguoigiaohang_list = Nguoigiaohang_models.objects.filter()
    return render(request,'nhap.html',{'nhap_list':nhap_list, 'kho_list':kho_list, 'nguoigiaohang_list':nguoigiaohang_list})

@user_passes_test(can_delete_nhap, login_url='/nhap/')

def delete_nhap(request):
    if request.method == 'POST':
        try:
            Ma_phieu_nk = request.POST['ma_nhap_xoa']
            nhap= Nhap_models.objects.get(ma_phieu_nk = Ma_phieu_nk)
            nhap.delete()
            return redirect('nhap/')
        except Exception as e:
            return render(request,'error.html')
    else:
        return render(request,'error.html')

def get_nhapchitiet(request,id):
    nhap_list = Nhap_models.objects.filter(ma_phieu_nk=id).order_by('ma_phieu_nk')
    kho_list = Kho_models.objects.filter()
    nguoigiaohang_list = Nguoigiaohang_models.objects.filter()
    phieunhapchitiet_list = Nhapchitiet_models.objects.filter(ma_phieu_nk=id)
    return render(request,'phieunhapchitiet_check.html',{'nhap_list':nhap_list, 'kho_list':kho_list, 'nguoigiaohang_list':nguoigiaohang_list, 'phieunhapchitiet_list':phieunhapchitiet_list})

def get_nhap_search(request,id):
    nhap_list = Nhap_models.objects.filter(ma_phieu_nk = id).order_by('ma_phieu_nk')
    kho_list = Kho_models.objects.filter()
    nguoigiaohang_list = Nguoigiaohang_models.objects.filter()
    return render(request,'nhap_search.html',{'nhap_list':nhap_list, 'kho_list':kho_list, 'nguoigiaohang_list':nguoigiaohang_list})

def search_nhap(request):
    if request.method == 'POST':
        try:
            Ma_phieu_nhap_kho = request.POST['ma_phieu_nk']
            nhap = Nhap_models.objects.get(ma_phieu_nk = Ma_phieu_nhap_kho)
        except Exception as e:
            respone = HttpResponse()
            respone.writelines('<h1>Phiếu nhập kho không tồn tại</h1>')
            respone.writelines('<a href="/nhap">Trở về trang phiếu nhập</a>')
            return respone
        return redirect('nhapSearch/'+Ma_phieu_nhap_kho+'/')
    else:
        return render(request,'error.html')