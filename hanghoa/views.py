from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Hanghoa as Hanghoa_models
from nhapchitiet.models import Nhapchitiet as Nhapchitiet_models
# Kiểm soát quyền truy cập
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
# Hàm xác thực quyền truy cập để xem dữ liệu 
def can_view_hanghoa(user):
    return user.has_perm('hanghoa.get_hanghoa')

# Hàm xác thực quyền truy cập để thêm dữ liệu 
def can_add_hanghoa(user):
    return user.has_perm('hanghoa.add_hanghoa')

# Hàm xác thực quyền truy cập để chỉnh sửa dữ liệu 
def can_change_hanghoa(user):
    return user.has_perm('hanghoa.change_hanghoa')

# Hàm xác thực quyền truy cập để xóa dữ liệu 
def can_delete_hanghoa(user):
    return user.has_perm('hanghoa.delete_hanghoa')



# Create your views here.
def get_hanghoa(request):
    hanghoa_list = Hanghoa_models.objects.filter().order_by('ma_hh')
    return render(request,'hanghoa.html',{'hanghoa_list':hanghoa_list})

@user_passes_test(can_add_hanghoa, login_url='/hanghoa/')

def add_hanghoa(request):
    if request.method == 'POST':
        Ma_hh = request.POST['ma_hh']
        Ten_hh = request.POST['ten_hh']
        Don_gia = request.POST['don_gia']
        if Hanghoa_models.objects.filter(ma_hh = Ma_hh).exists():
            messages.error(request, 'Mã hàng hóa đã tồn tại')
        else:
            if Ma_hh != '' and len(Ma_hh) == 10:
                hanghoa = Hanghoa_models.objects.create(ma_hh = Ma_hh,
                                                        ten_hh = Ten_hh,
                                                        don_gia = Don_gia)
                messages.success(request,'Thêm người giao hàng thành công')
            else:
                messages.error(request, 'Mã hàng hóa sai định dạng')
        return redirect('hanghoa/')
    else:
        return render(request,'error.html')

def get_hanghoa_change(request,id):
    hanghoa_list = Hanghoa_models.objects.filter(ma_hh = id)
    return render(request,'hanghoa_update.html',{'hanghoa_list':hanghoa_list})

@user_passes_test(can_change_hanghoa, login_url='/hanghoa/')

def change_hanghoa(request):
    if request.method == 'POST':
        try:
            Ma_hh = request.POST['ma_hh']
            Ten_hh = request.POST['ten_hh']
            Don_gia = request.POST['don_gia']
            hanghoa = Hanghoa_models.objects.get(ma_hh = Ma_hh)
            hanghoa.ten_hh = Ten_hh
            hanghoa.don_gia = Don_gia
            hanghoa.save()
            return redirect('hanghoa/')
        except Exception as e:
            return render(request,'error.html')
    else:
        return render(request,'error.html')

def get_hanghoa_delete(request):
    hanghoa_list = Hanghoa_models.objects.filter()
    nhapchitiet_list = Nhapchitiet_models.objects.filter()
    return render(request,'hanghoa.html',{'hanghoa_list':hanghoa_list, 'nhapchitiet_list':nhapchitiet_list})

@user_passes_test(can_delete_hanghoa, login_url='/hanghoa/')

def delete_hanghoa(request):
    if request.method == 'POST':
        try:
            Ma_hh = request.POST['ma_hang_hoa_xoa']
            hanghoa = Hanghoa_models.objects.get(ma_hh = Ma_hh)
            if Nhapchitiet_models.objects.filter(ma_hh = Ma_hh).exists():
                messages.error(request, 'Mã hàng hóa đang được sử dụng trong phiếu nhập chi tiết')
            else:
                hanghoa.delete()
            return redirect('hanghoa/')
        except Exception as e:
            return render(request,'error.html')
    else:
        return render(request,'error.html')
    
def get_hanghoa_search(request,id):
    hanghoa_list = Hanghoa_models.objects.filter(ten_hh= id).order_by('ma_hh')
    return render(request,'hanghoa_search.html',{'hanghoa_list':hanghoa_list})

def search_hanghoa(request):
    if request.method == 'POST':
        try:
            Ten_hang_hoa = request.POST['ten_hh']
            hanghoa = Hanghoa_models.objects.filter(ten_hh = Ten_hang_hoa)
            if hanghoa.exists():
                return redirect('hanghoaSearch/'+Ten_hang_hoa+'/')
            else:
                respone = HttpResponse()
                respone.writelines('<h1>Hàng hóa không tồn tại</h1>')
                respone.writelines('<a href="/hanghoa">Trở về trang hàng hóa</a>')
                return respone    
        except Exception as e:
            respone = HttpResponse()
            respone.writelines('<h1>Hàng hóa không tồn tại</h1>')
            respone.writelines('<a href="/hanghoa">Trở về trang hàng hóa</a>')
            return respone
    else:
        return render(request,'error.html')