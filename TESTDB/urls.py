"""TESTDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from trangchu import views as trangchu
from kho import views as kho
from hanghoa import views as hanghoa
from nguoigiaohang import views as nguoigiaohang
from nhap import views as nhap
from nhapchitiet import views as nhapchitiet

urlpatterns = [
    path('admin/', admin.site.urls),
# ĐỊA CHỈ TRẢ VỀ TRANG CHỦ
    path('',trangchu.get_trangchu),

# ĐỊA CHỈ TRẢ VỀ CỦA KHO
    # địa chỉ trả về cho trang kho
    path('kho/',kho.get_kho),
    # địa chỉ trả về trong quá trình thêm thông tin kho
    path('addKho',kho.add_kho),
    # địa chỉ trả về trong quá trình cập nhập kho
    path('kho/<id>/',kho.get_kho_change),
    path('changeKho',kho.change_kho),
    # path('kho/',kho.update_kho),
    # địa chỉ trả về trong quá trình xóa kho 
    path('kho/',kho.get_kho_delete),
    path('deleteKho',kho.delete_kho),
    # địa chỉ trả về trong quá trình tìm kiếm kho 
    path('khoSearch/<id>/',kho.get_kho_search),
    path('searchKho',kho.search_kho),

# ĐỊA CHỈ TRẢ VỀ CỦA HÀNG HÓA
    # địa chỉ trả về cho trang Hàng hóa
    path('hanghoa/',hanghoa.get_hanghoa),
    # địa chỉ trả về trong quá trình thêm thông tin hàng hóa
    path('addHanghoa',hanghoa.add_hanghoa),
    # địa chỉ trả về trong quá trình cập nhập hàng hóa
    path('hanghoa/<id>/',hanghoa.get_hanghoa_change),
    path('changeHanghoa',hanghoa.change_hanghoa),
    # địa chỉ trả về trong quá trình xóa hàng hóa
    path('hanghoa/',hanghoa.get_hanghoa_delete),
    path('deleteHanghoa',hanghoa.delete_hanghoa),
    # địa chỉ trả về trong quá trình tìm kiếm hàng hóa
    path('hanghoaSearch/<id>/',hanghoa.get_hanghoa_search),
    path('searchHanghoa',hanghoa.search_hanghoa),

# ĐỊA CHỈ TRẢ VỀ CỦA NGƯỜI GIAO HÀNG
    # địa chỉ trả về cho trang người giao hàng
    path('nguoigiaohang/',nguoigiaohang.get_nguoigiaohang),
    # địa chỉ trả về trong quá trình thêm thông tin nguoigiaohang
    path('addNguoigiaohang',nguoigiaohang.add_nguoigiaohang),
    # địa chỉ trả về trong quá trình cập nhập nguoigiaohang
    path('nguoigiaohang/<id>/',nguoigiaohang.get_nguoigiaohang_change),
    path('changeNguoigiaohang',nguoigiaohang.change_nguoigiaohang),
    # địa chỉ trả về trong quá trình xóa nguoigiaohang 
    path('nguoigiaohang/',nguoigiaohang.get_nguoigiaohang_delete),
    path('deleteNguoigiaohang',nguoigiaohang.delete_nguoigiaohang),
    # địa chỉ trả về trong quá trình tìm kiếm nguoigiaohang 
    path('nguoigiaohangSearch/<id>/',nguoigiaohang.get_nguoigiaohang_search),
    path('searchNguoigiaohang',nguoigiaohang.search_nguoigiaohang),

# ĐỊA CHỈ TRẢ VỀ CỦA NHẬP
    # địa chỉ trả về trang nhập
    path('nhap/',nhap.get_nhap),
    # địa chỉ trả về khi thêm phiếu nhập kho
    path('addNhap',nhap.add_nhap),
    # địa chỉ trả về khi chỉnh sửa phiếu nhập kho
    path('nhap/<id>/',nhap.get_nhap_change),
    path('changeNhap',nhap.change_nhap),
    # địa chỉ trả về khi xóa thông tin phiếu nhập kho
    path('nhap/',nhap.get_nhap_delete),
    path('deleteNhap',nhap.delete_nhap),
    # địa chỉ khi bấm vào sẽ hiện phiếu nhập chi tiết
    path('nhap/<id>/chitiet/',nhap.get_nhapchitiet),
    # địa chỉ trả về khi xóa thông tin phiếu nhập kho
    path('nhapSearch/<id>/',nhap.get_nhap_search),
    path('searchNhap',nhap.search_nhap),

# ĐỊA CHỈ TRẢ VỀ CỦA NHẬP CHI TIẾT
    # địa chỉ trả về trang nhập chi tiết
    path('nhapchitiet/',nhapchitiet.get_nhapchitiet),
    # địa chỉ trả về khi thêm phiếu nhập kho
    path('addNhapchitiet',nhapchitiet.add_nhapchitiet),
    # địa chỉ trả về khi chỉnh sửa phiếu nhập kho
    path('nhapchitiet/<id>/',nhapchitiet.get_nhapchitiet_change),
    path('changeNhapchitiet',nhapchitiet.change_nhapchitiet),
    # địa chỉ trả về khi xóa thông tin phiếu nhập kho
    path('nhapchitiet/',nhapchitiet.get_nhapchitiet_delete),
    path('deleteNhapchitiet',nhapchitiet.delete_nhapchitiet),
    # địa chỉ trả về khi xóa thông tin phiếu nhập kho
    path('nhapchitietSearch/<id>/',nhapchitiet.get_nhapchitiet_search),
    path('searchNhapchitiet',nhapchitiet.search_nhapchitiet),
]
admin.site.site_header = "Tùng Linh"