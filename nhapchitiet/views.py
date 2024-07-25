from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Nhapchitiet as Nhapchitiet_models
from nhap.models import Nhap as Nhap_models
from hanghoa.models import Hanghoa as Hanghoa_models
# Kiểm soát quyền truy cập
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse

# Hàm xác thực quyền truy cập để xem dữ liệu 
def can_view_nhapchitiet(user):
    return user.has_perm('nhapchitiet.get_nhapchitiet')

# Hàm xác thực quyền truy cập để thêm dữ liệu 
def can_add_nhapchitiet(user):
    return user.has_perm('nhapchitiet.add_nhapchitiet')

# Hàm xác thực quyền truy cập để chỉnh sửa dữ liệu 
def can_change_nhapchitiet(user):
    return user.has_perm('nhapchitiet.change_nhapchitiet')

# Hàm xác thực quyền truy cập để xóa dữ liệu 
def can_delete_nhapchitiet(user):
    return user.has_perm('nhapchitiet.delete_nhapchitiet')


# Create your views here.
def get_nhapchitiet(request):
    phieunhapchitiet_list = Nhapchitiet_models.objects.filter().order_by('ma_phieu_nk')
    nhap_list = Nhap_models.objects.filter()
    hanghoa_list = Hanghoa_models.objects.filter()
    return render(request,'phieunhapchitiet.html',{'phieunhapchitiet_list':phieunhapchitiet_list,'nhap_list':nhap_list,'hanghoa_list':hanghoa_list})

@user_passes_test(can_add_nhapchitiet, login_url='/nhapchitiet/')

def add_nhapchitiet(request):
    if request.method == 'POST':
        Ma_hh = request.POST['ma_hh']
        Ma_phieu_nk = request.POST['ma_phieu_nhap_chi_tiet']
        So_luong = request.POST['so_luong']
        ma_phieu_nhap = Nhap_models.objects.get(ma_phieu_nk = Ma_phieu_nk)
        ma_hh = Hanghoa_models.objects.get(ma_hh = Ma_hh)
        if (Nhap_models.objects.filter(ma_phieu_nk = Ma_phieu_nk).exists() and 
            Hanghoa_models.objects.filter(ma_hh = Ma_hh).exists()):
            try:
                Nhapchitiet_models.objects.create(ma_hh = ma_hh,
                                                  ma_phieu_nk = ma_phieu_nhap,
                                                  so_luong = So_luong)
                messages.success(request,'Thêm thành công')
            except Exception as e:
                messages.error(request, 'Có lỗi xảy ra')
        else:
            messages.error(request, 'Có lỗi xảy ra')
        return redirect('nhapchitiet/')
    else:
        return render(request,'error.html')

def get_nhapchitiet_change(request,id):
    phieunhapchitiet_list = Nhapchitiet_models.objects.filter(id=id)
    nhap_list = Nhap_models.objects.filter()
    hanghoa_list = Hanghoa_models.objects.filter()
    return render(request,'phieunhapchitiet_update.html',{'phieunhapchitiet_list':phieunhapchitiet_list,'nhap_list':nhap_list,'hanghoa_list':hanghoa_list})

@user_passes_test(can_change_nhapchitiet, login_url='/nhapchitiet/')

def change_nhapchitiet(request):
    if request.method == 'POST':
        try:
            ID = request.POST['id']
            Ma_hh =request.POST['ma_hh']
            So_luong = request.POST['so_luong']
            Ma_HH = Hanghoa_models.objects.get(ma_hh = Ma_hh)
            nhapchitiet = Nhapchitiet_models.objects.get(id = ID)
            nhapchitiet.ma_hh = Ma_HH
            nhapchitiet.so_luong = So_luong
            nhapchitiet.save()
            return redirect('nhapchitiet/')
        except Exception as e:
            return render(request,'error.html')
    else:
        return render(request,'error.html')


def get_nhapchitiet_delete(request):
    phieunhapchitiet_list = Nhapchitiet_models.objects.filter()
    nhap_list = Nhap_models.objects.filter()
    hanghoa_list = Hanghoa_models.objects.filter()
    return render(request,'phieunhapchitiet.html',{'phieunhapchitiet_list':phieunhapchitiet_list,'nhap_list':nhap_list,'hanghoa_list':hanghoa_list})

@user_passes_test(can_delete_nhapchitiet, login_url='/nhapchitiet/')

def delete_nhapchitiet(request):
    if request.method == 'POST':
        Ma_phieu_nk = request.POST['mpn_chi_tiet']
        Id = request.POST['id_xoa']
        nhapchitiet = Nhapchitiet_models.objects.get(id = Id)
        nhapchitiet.delete()
        return redirect('nhapchitiet/')
    else:
        return render(request,'error.html')

def get_nhapchitiet_search(request,id):
    phieunhapchitiet_list = Nhapchitiet_models.objects.filter(ma_phieu_nk = id).order_by('id')
    nhap_list = Nhap_models.objects.filter()
    hanghoa_list = Hanghoa_models.objects.filter()
    return render(request,'phieunhapchitiet_search.html',{'phieunhapchitiet_list':phieunhapchitiet_list,'nhap_list':nhap_list,'hanghoa_list':hanghoa_list})

def search_nhapchitiet(request):
    if request.method == 'POST':
        try:
            Ma_phieu_nhap_kho = request.POST['ma_phieu_nk']
            ma_phieu_nhap = Nhap_models.objects.get(ma_phieu_nk = Ma_phieu_nhap_kho)
            nhapchitiet = Nhapchitiet_models.objects.filter(ma_phieu_nk = ma_phieu_nhap)
            if not nhapchitiet.exists():
                respone = HttpResponse()
                respone.writelines('<h1>Phiếu nhập không tồn tại</h1>')
                respone.writelines('<a href="/nhapchitiet">Trở về trang nhập chi tiết</a>')
            return redirect('nhapchitietSearch/'+Ma_phieu_nhap_kho+'/')
        except Exception as e:
            respone = HttpResponse()
            respone.writelines('<h1>Có lỗi xảy ra</h1>')
            respone.writelines('<a href="/nhapchitiet">Trở về trang nhập chi tiết</a>')
            return respone
    else:
        return render(request,'error.html')


    # print(request.user.get_all_permissions())
    # lệnh kiểm tra phân quyền