from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Nguoigiaohang as Nguoigiaohang_models
from nhap.models import Nhap as Nhap_models
# Kiểm soát quyền truy cập
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.http import HttpResponse
# Hàm xác thực quyền truy cập để xem dữ liệu 
def can_view_nguoigiaohang(user):
    return user.has_perm('nguoigiaohang.get_nguoigiaohang')

# Hàm xác thực quyền truy cập để thêm dữ liệu 
def can_add_nguoigiaohang(user):
    return user.has_perm('nguoigiaohang.add_nguoigiaohang')

# Hàm xác thực quyền truy cập để chỉnh sửa dữ liệu 
def can_change_nguoigiaohang(user):
    return user.has_perm('nguoigiaohang.change_nguoigiaohang')

# Hàm xác thực quyền truy cập để xóa dữ liệu 
def can_delete_nguoigiaohang(user):
    return user.has_perm('nguoigiaohang.delete_nguoigiaohang')

# Create your views here.
def get_nguoigiaohang(request):
    nguoigiaohang_list = Nguoigiaohang_models.objects.filter().order_by('ma_ngh')
    return render(request,'nguoigiaohang.html',{'nguoigiaohang_list':nguoigiaohang_list})

@user_passes_test(can_add_nguoigiaohang, login_url='/nguoigiaohang/')

def add_nguoigiaohang(request):
    if request.method == 'POST':
        Ma_NGH = request.POST['ma_nguoi_giao_hang']
        Ten_NGH = request.POST['ten_nguoi_giao_hang']
        if Nguoigiaohang_models.objects.filter(ma_ngh = Ma_NGH).exists():
            messages.error(request, 'Mã người giao hàng đã tồn tại')
        else:
            if Ma_NGH != '' and len(Ma_NGH) == 10:
                nguoigiaohang = Nguoigiaohang_models.objects.create(ma_ngh = Ma_NGH,
                                                        ten_ngh = Ten_NGH)
                messages.success(request,'Thêm người giao hàng thành công')
            else:
                messages.error(request, 'Mã người giao hàng sai định dạng')
        return redirect('nguoigiaohang/')
    else:
        return render(request,'error.html') 

def get_nguoigiaohang_change(request,id):
    nguoigiaohang_list = Nguoigiaohang_models.objects.filter(ma_ngh = id)
    return render(request,'nguoigiaohang_update.html',{'nguoigiaohang_list':nguoigiaohang_list})

@user_passes_test(can_change_nguoigiaohang, login_url='/nguoigiaohang/')

def change_nguoigiaohang(request):
    if request.method == 'POST':
        try:
            Ma_NGH = request.POST['ma_nguoi_giao_hang']
            Ten_NGH = request.POST['ten_nguoi_giao_hang']
            nguoigiaohang = Nguoigiaohang_models.objects.get(ma_ngh = Ma_NGH)
            nguoigiaohang.ten_ngh = Ten_NGH
            nguoigiaohang.save()
            return redirect('nguoigiaohang/')
        except Exception as e:
            return render(request,'error.html')
    else:
        return render(request,'error.html')

    
def get_nguoigiaohang_delete(request):
    nguoigiaohang_list = Nguoigiaohang_models.objects.filter().order_by('ma_ngh')
    nhap_list = Nhap_models.objects.filter()
    return render(request,'nguoigiaohang.html',{'nguoigiaohang_list':nguoigiaohang_list, 'nhap_list':nhap_list})

@user_passes_test(can_delete_nguoigiaohang, login_url='/nguoigiaohang/')

def delete_nguoigiaohang(request):
    if request.method == 'POST':
        try:
            Ma_NGH = request.POST['ma_nguoi_giao_hang_xoa']
            nguoigiaohang = Nguoigiaohang_models.objects.get(ma_ngh = Ma_NGH)
            if Nhap_models.objects.filter(ma_nguoi_giao_hang = Ma_NGH).exists():
                messages.error(request, 'Mã kngười giao hàng đang được sử dụng trong phiếu nhập')
            else:
                nguoigiaohang.delete()
            return redirect('nguoigiaohang/')
        except Exception as e:
            return render(request,'error.html')
    else:
        return render(request,'error.html')

def get_nguoigiaohang_search(request,id):
    nguoigiaohang_list = Nguoigiaohang_models.objects.filter(ma_ngh = id).order_by('ma_ngh')
    return render(request,'nguoigiaohang_search.html',{'nguoigiaohang_list':nguoigiaohang_list})

def search_nguoigiaohang(request):
    if request.method == 'POST':
        try:
            Ma_nguoi_giao_hang = request.POST['ma_nguoi_giao_hang']
            kho = Nguoigiaohang_models.objects.get(ma_ngh = Ma_nguoi_giao_hang)
        except Exception as e:
            respone = HttpResponse()
            respone.writelines('<h1>Mã người giao hàng không tồn tại</h1>')
            respone.writelines('<a href="/nguoigiaohang">Trở về trang người giao hàng</a>')
            return respone
        return redirect('nguoigiaohangSearch/'+Ma_nguoi_giao_hang+'/')
    else:
        return render(request,'error.html')