CREATE DATABASE TESTDB;
USE TESTDB;

/*TẠO TRIGGER CHO KHO TẠO TRIGGER KHI THÊM KHO*/

create or alter trigger tgADD_KHO
on Kho
instead of insert
as
begin
	declare @makho_insert varchar(10) = (select isnull(Ma_kho,'null') from inserted)
	if exists (select 1 from Kho where Ma_kho = @makho_insert)
	begin
		print N'Mã kho đã tồn tại'
		rollback
	end
	else
	begin
		if @makho_insert = 'null' or @makho_insert = '' or len(@makho_insert) != 10
		begin
			print N'Mã kho Sai định dạng!'
			rollback
		end
		else
		begin
			insert into Kho (Ma_kho,Dia_diem_kho)
			select Ma_kho, Dia_diem_kho
			from inserted
		end
	end
end
--TEST CASE CHO TRƯỜNG HỢP THÊM KHO THÀNH CÔNG
INSERT INTO Kho VALUES ('KHO0000006',N'Hà Nội')
--TEST CASE CHO TRƯỜNG HỢP THÊM KHO THẤT BẠI
INSERT INTO Kho (Dia_diem_kho) VALUES (N'Kon Tum')

GO

/*TẠO TRIGGER KHI SỬA KHO*/

create or alter trigger tgUPDATE_KHO
on Kho
for update
as
begin
	declare @makho_insert varchar(10) = (select Ma_kho from inserted)
	if not exists (select 1 from Kho where Ma_kho = @makho_insert)
	begin
		print N'Mã kho chưa tồn tại'
		rollback
	end
end
--TEST CASE CHO TRƯỜNG HỢP CHỈNH SỬA KHO THÀNH CÔNG
UPDATE Kho
SET Dia_diem_kho = N'Đồng Nai'
WHERE Ma_kho = 'KHO0000005'
--TEST CASE CHO TRƯỜNG HỢP CHỈNH SỬA KHO THẤT BẠI
UPDATE Kho
SET Dia_diem_kho = N'Đồng Nai'
WHERE Ma_kho = 'KHO0000100'

GO

--TẠO TRIGGER KHI XÓA KHO

create or alter trigger tgDELETE_KHO
on Kho
instead of delete
as
begin
	declare @makho_delete varchar(10) = (select Ma_kho from deleted)
	if not exists (select 1 from Kho where Ma_kho = @makho_delete)
	begin
		print N'Mã kho chưa tồn tại'
		rollback
	end
	else
	begin
		if exists (select 1 from Nhap where Ma_kho = @makho_delete)
		begin
			print N'Mã kho đang được sử dụng trong phiếu nhập'
			rollback
		end
		else
		begin
			delete Kho
			where Ma_kho = @makho_delete
		end
	end
end
--TEST CASE CHO TRƯỜNG HỢP XÓA KHO THÀNH CÔNG
DELETE FROM Kho
WHERE Ma_kho = 'KHO0000006'
--TEST CASE CHO TRƯỜNG HỢP XÓA KHO THẤT BẠI
DELETE FROM Kho
WHERE Ma_kho = 'KHO0000008'
DELETE FROM Kho
WHERE Ma_kho = 'KHO0000048'
select * from Nhap
GO

--___________________________________________________________________________________________________________________________
--TẠO TRIGGER CHO NGƯỜI GIAO HÀNG--------------------------------------------------------------------------------------------
--TẠO TRIGGER KHI THÊM NGƯỜI GIAO HÀNG

create or alter trigger tgADD_NGUOIGIAOHANG
on NguoiGiaoHang
instead of insert
as
begin
	declare @manguoigiaohang_insert varchar(10) = (select isnull(Ma_nguoi_giao_hang,'null') from inserted)
	if exists (select 1 from NguoiGiaoHang where Ma_nguoi_giao_hang = @manguoigiaohang_insert)
	begin
		print N'Mã người giao hàng đã tồn tại'
		rollback
	end
	else
	begin
		if @manguoigiaohang_insert = 'null' or @manguoigiaohang_insert = '' or len(@manguoigiaohang_insert) != 10
		begin
			print N'Mã người giao hàng sai định dạng!'
			rollback
		end
		else
		begin
			insert into NguoiGiaoHang (Ma_nguoi_giao_hang,Ten_nguoi_giao_hang)
			select Ma_nguoi_giao_hang,Ten_nguoi_giao_hang
			from inserted
		end
	end
end
--TEST CASE CHO TRƯỜNG HỢP THÊM NGƯỜI GIAO HÀNG THÀNH CÔNG
INSERT INTO NguoiGiaoHang VALUES ('NGH0000001',N'Công ty TNHH Sản xuất, lắp ráp Tuấn Nghĩa')
--TEST CASE CHO TRƯỜNG HỢP THÊM NGƯỜI GIAO HÀNG THẤT BẠI
INSERT INTO NguoiGiaoHang VALUES ('',N'Công ty TNHH Sản xuất, lắp ráp Tuấn Nghĩa')

GO

--TẠO TRIGGER KHI CHỈNH SỬA NGƯỜI GIAO HÀNG

create or alter trigger tgUPDATE_NGUOIGIAOHANG
on NguoiGiaoHang
for update
as
begin
	declare @manguoigiaohang_insert varchar(10) = (select Ma_nguoi_giao_hang from inserted)
	if not exists (select 1 from NguoiGiaoHang where Ma_nguoi_giao_hang = @manguoigiaohang_insert)
	begin
		print N'Mã người giao hàng chưa tồn tại'
		rollback
	end
end
--TEST CASE CHO TRƯỜNG HỢP CHỈNH SỬA NGƯỜI GIAO HÀNG THÀNH CÔNG
UPDATE NguoiGiaoHang
SET Ten_nguoi_giao_hang = N'Công ty Tuấn Nghĩa'
WHERE Ma_nguoi_giao_hang = 'NGH0000001'
--TEST CASE CHO TRƯỜNG HỢP CHỈNH SỬA NGƯỜI GIAO HÀNG THẤT BẠI
UPDATE NguoiGiaoHang
SET Ten_nguoi_giao_hang = N'Công ty Tuấn Minh'
WHERE Ma_nguoi_giao_hang = 'NGH0000002'

GO

--TẠO TRIGGER KHI XÓA NGƯỜI GIAO HÀNG

create or alter trigger tgDELETE_NGUOIGIAOHANG
on NguoiGiaoHang
instead of delete
as
begin
	declare @manguoigiaohang_delete varchar(10) = (select Ma_nguoi_giao_hang from deleted)
	if not exists (select 1 from NguoiGiaoHang where Ma_nguoi_giao_hang = @manguoigiaohang_delete)
	begin
		print N'Mã người giao hàng chưa tồn tại'
		rollback
	end
	else
	begin
		delete NguoiGiaoHang
		where Ma_nguoi_giao_hang = @manguoigiaohang_delete
	end
end
--TEST CASE CHO TRƯỜNG HỢP XÓA KHO THÀNH CÔNG
DELETE FROM NguoiGiaoHang
WHERE Ma_nguoi_giao_hang = 'NGH0000005'
--TEST CASE CHO TRƯỜNG HỢP XÓA KHO THẤT BẠI
DELETE FROM NguoiGiaoHang
WHERE Ma_nguoi_giao_hang = 'NGH0000006'

GO

--___________________________________________________________________________________________________________________________
--TẠO TRIGGER CHO HÀNG HÓA---------------------------------------------------------------------------------------------------
--TẠO TRIGGER KHI THÊM HÀNG HÓA

create or alter trigger tgADD_HANGHOA
on HangHoa
instead of insert
as
begin
	declare @mahanghoa_insert varchar(10) = (select isnull(Ma_hang_hoa,'null') from inserted)
	if exists (select 1 from HangHoa where Ma_hang_hoa = @mahanghoa_insert)
	begin
		print N'Mã hàng hóa đã tồn tại'
		rollback
	end
	else
	begin
		if @mahanghoa_insert = 'null' or @mahanghoa_insert = '' or len(@mahanghoa_insert) != 10
		begin
			print N'Mã hàng hóa sai định dạng!'
			rollback
		end
		else
		begin
			insert into HangHoa (Ma_hang_hoa,Ten_hang_hoa,So_luong,Don_gia)
			select Ma_hang_hoa,Ten_hang_hoa,So_luong,Don_gia
			from inserted
		end
	end
end
--TEST CASE CHO TRƯỜNG HỢP THÊM HÀNG HÓA THÀNH CÔNG
INSERT INTO HangHoa(Ma_hang_hoa,Ten_hang_hoa,Don_gia) 
VALUES ('XMAYAIRBLA',N'Xe máy Air Blade',45000000)
INSERT INTO HangHoa VALUES ('XMAYATTILA',N'Xe máy Attila','',45000000)
--TEST CASE CHO TRƯỜNG HỢP THÊM HÀNG HÓA THẤT BẠI
INSERT INTO HangHoa(Ma_hang_hoa,Ten_hang_hoa,Don_gia) 
VALUES ('',N'Xe máy Air Blade',45000000)

GO

--TẠO TRIGGER KHI CHỈNH SỬA HÀNG HÓA

create or alter trigger tgUPDATE_HANGHOA
on HangHoa
for update
as
begin
	declare @mahanghoa_insert varchar(10) = (select Ma_hang_hoa from inserted)
	if not exists (select 1 from HangHoa where Ma_hang_hoa = @mahanghoa_insert)
	begin
		print N'Mã hàng hóa chưa tồn tại'
		rollback
	end
end
--TEST CASE CHO TRƯỜNG HỢP CHỈNH SỬA HÀNG HÓA THÀNH CÔNG
UPDATE HangHoa
SET Ten_hang_hoa = N'Xe máy Suzuki'
WHERE Ma_hang_hoa = 'XMAYATTILA'
--TEST CASE CHO TRƯỜNG HỢP CHỈNH SỬA HÀNG HÓA THẤT BẠI
UPDATE HangHoa
SET Ten_hang_hoa = N'Xe máy Suzuki'
WHERE Ma_hang_hoa = 'XMAYSUZUKI'

GO

--TẠO TRIGGER KHI XÓA HÀNG HÓA

create or alter trigger tgDELETE_HANGHOA
on HangHoa
instead of delete
as
begin
	declare @mahanghoa_delete varchar(10) = (select Ma_hang_hoa from deleted)
	if not exists (select 1 from HangHoa where Ma_hang_hoa = @mahanghoa_delete)
	begin
		print N'Mã hàng hóa chưa tồn tại'
		rollback
	end
	else
	begin
		delete HangHoa
		where Ma_hang_hoa = @mahanghoa_delete
	end
end
--TEST CASE CHO TRƯỜNG HỢP XÓA HÀNG HÓA THÀNH CÔNG
DELETE FROM HangHoa
WHERE Ma_hang_hoa = 'XMAYATTILA'
--TEST CASE CHO TRƯỜNG HỢP XÓA HÀNG HÓA THẤT BẠI
DELETE FROM HangHoa
WHERE Ma_hang_hoa = 'XMAYSUZUKI'

GO

--___________________________________________________________________________________________________________________________
--TẠO TRIGGER CHO PHIẾU NHẬP-------------------------------------------------------------------------------------------------
--TẠO TRIGGER KHI THÊM PHIẾU NHẬP

create or alter trigger tgADD_NHAP
on Nhap
instead of insert
as
begin
	declare @manguoigiaohang varchar(10) = (select Ma_nguoi_giao_hang from inserted),
			@maphieunhapkho varchar(10) = (select isnull(Ma_phieu_nhap_kho,'null') from inserted)
	--KIỂM TRA MÃ KHO
	if not exists (select 1 from inserted join Kho on inserted.Ma_kho = Kho.Ma_kho)
	begin
		print N'Mã kho không tồn tại'
		rollback
	end
	else
	begin
		--KIỂM TRA MÃ NGƯỜI GIAO HÀNG
		if not exists(select 1 from inserted join NguoiGiaoHang on inserted.Ma_nguoi_giao_hang = NguoiGiaoHang.Ma_nguoi_giao_hang)
		begin
			print N'Mã người giao hàng không tồn tại'
			rollback
		end
		else
		begin
			--KIỂM TRA MÃ PHIẾU NHẬP KHO
			if exists (select 1 from inserted join Nhap on inserted.Ma_phieu_nhap_kho = Nhap.Ma_phieu_nhap_kho)
			begin
				print N'Mã phiếu nhập kho đã tồn tại'
				rollback
			end
			else
			begin
				if @maphieunhapkho = 'null' or @maphieunhapkho = '' or len(@maphieunhapkho) != 10
				begin
					print N'Mã phiếu nhập sai định dạng!'
					rollback
				end
				else
				begin
					insert into Nhap (Ma_phieu_nhap_kho,Ma_nguoi_giao_hang,Thuc_nhap,Tong_cong,Ma_kho)
					select Ma_phieu_nhap_kho,Ma_nguoi_giao_hang,Thuc_nhap,Tong_cong,Ma_kho
					from inserted
				end
			end
		end
	end
end
--TEST CASE CHO TRƯỜNG HỢP THÊM NHẬP THÀNH CÔNG
INSERT INTO Nhap (Ma_phieu_nhap_kho,Ma_nguoi_giao_hang,Ma_kho)
VALUES ('PNHAP00004','NGH0000001','KHO0000001')
--TEST CASE CHO TRƯỜNG HỢP THÊM NHẬP THẤT BẠI
--TRƯỜNG HỢP MÃ KHO CHƯA TỒN TẠI
INSERT INTO Nhap (Ma_phieu_nhap_kho,Ma_nguoi_giao_hang,Ma_kho)
VALUES ('PNHAP00010','NGH0000004','KHO0000010')
--TRƯỜNG HỢP MÃ NGƯỜI GIAO HÀNG CHƯA TỒN TẠI
INSERT INTO Nhap (Ma_phieu_nhap_kho,Ma_nguoi_giao_hang,Ma_kho)
VALUES ('PNHAP00007','NGH0000010','KHO0000002')
--TRƯỜNG HỢP MÃ PHIẾU NHẬP KHO ĐÃ TỒN TẠI
INSERT INTO Nhap (Ma_phieu_nhap_kho,Ma_nguoi_giao_hang,Ma_kho)
VALUES ('PNHAP00001','NGH0000004','KHO0000002')

GO

--TẠO TRIGGER KHI CHỈNH SỬA PHIẾU NHẬP

create or alter trigger tgUPDATE_NHAP
on Nhap
instead of update
as
begin
	declare @makho varchar(10) = (select Ma_kho from inserted),
			@manguoigiaohang varchar(10) = (select Ma_nguoi_giao_hang from inserted),
			@maphieunhapkho varchar(10) = (select Ma_phieu_nhap_kho from inserted),
			@thucnhap int = (select Thuc_nhap from inserted),
			@tongcong numeric(12,0) = (select Tong_cong from inserted),
			@error bit = 1
	--KIỂM TRA MÃ PHIẾU NHẬP KHO
	if not exists (select 1 from Nhap where Ma_phieu_nhap_kho = @maphieunhapkho)
	begin
		print N'Mã phiếu nhập kho không tồn tại'
		set @error = 0
		rollback
		return
	end
	--KIỂM TRA MÃ KHO
	if not exists (select 1 from Kho where Ma_kho = @makho)
	begin
		print N'Mã kho không tồn tại'
		set @error = 0
		rollback
	end
	--KIỂM TRA MÃ NGƯỜI GIAO HÀNG
	if not exists (select 1 from NguoiGiaoHang where Ma_nguoi_giao_hang = @manguoigiaohang)
	begin
		print N'Mã người giao hàng không tồn tại'
		set @error = 0
		rollback
	end
	--THỰC HIỆN CẬP NHẬT
	if @error = 1
	begin
		update Nhap
		set Ma_nguoi_giao_hang = @manguoigiaohang, 
			Ma_kho = @makho,
			Thuc_nhap = @thucnhap,
			Tong_cong = @tongcong
		where Ma_phieu_nhap_kho = @maphieunhapkho
	end
end
--TEST CASE CHO TRƯỜNG HỢP CHỈNH SỬA NHẬP THÀNH CÔNG
UPDATE Nhap
SET Ma_nguoi_giao_hang = 'NGH0000001', Ma_kho = 'KHO0000005'
WHERE Ma_phieu_nhap_kho = 'PNHAP00001'
--TEST CASE CHO TRƯỜNG HỢP CHỈNH SỬA NHẬP THẤT BẠI
--TRƯỜNG HỢP MÃ KHO CHƯA TỒN TẠI
UPDATE Nhap
SET Ma_kho = 'KHO0000010'
WHERE Ma_phieu_nhap_kho = 'PNHAP00002'
--TRƯỜNG HỢP MÃ NGƯỜI GIAO HÀNG CHƯA TỒN TẠI
UPDATE Nhap
SET Ma_nguoi_giao_hang = 'NGH0000010'
WHERE Ma_phieu_nhap_kho = 'PNHAP00002'
--TRƯỜNG HỢP MÃ PHIẾU NHẬP KHO CHƯA TỒN TẠI
UPDATE Nhap
SET Ma_kho = 'KHO0000002'
WHERE Ma_phieu_nhap_kho = 'PNHAP00005'

GO 

--TẠO TRIGGER KHI XÓA PHIẾU NHẬP

create or alter trigger tgDELETE_NHAP
on Nhap
instead of delete
as
begin
	declare @maphieunhapkho_delete varchar(10) = (select Ma_phieu_nhap_kho from deleted)
	if not exists (select 1 from Nhap where Ma_phieu_nhap_kho = @maphieunhapkho_delete)
	begin
		print N'Mã phiếu nhập không tồn tại'
		rollback
	end
	else
	begin
		delete Nhap
		where Ma_phieu_nhap_kho = @maphieunhapkho_delete
	end
end
--TEST CASE CHO TRƯỜNG HỢP XÓA HÀNG HÓA THÀNH CÔNG
DELETE FROM Nhap
WHERE Ma_phieu_nhap_kho ='PNHAP00005'
--TEST CASE CHO TRƯỜNG HỢP XÓA HÀNG HÓA THẤT BẠI
DELETE FROM Nhap
WHERE Ma_phieu_nhap_kho ='PNHAP00010'

GO


--________________________________________________________________________________________________________________________________
--TẠO TRIGGER CHO PHIẾU NHẬP CHI TIẾT---------------------------------------------------------------------------------------------
--TẠO TRIGGER KHI THÊM PHIẾU NHẬP CHI TIẾT VÀ TẠO STT MỚI KHI NHẬP THÊM SẢN PHẨM
--THÊM MỚI DỮ LIỆU VÀO BẢNG PHIẾU NHẬP CHI TIẾT
create or alter trigger tgADD_PHIEUNHAPCHITIET
on NhapChiTiet
instead of insert
as 
begin
	declare @stt int = (select isnull(max(So_thu_tu),0)+1 from NhapChiTiet),
			@soluong int = (select So_luong from inserted),
			@maphieunhapkho varchar(10) = (select Ma_phieu_nhap_kho from inserted),
			@mahanghoa varchar(10) = (select Ma_hang_hoa from inserted),
			@thanhtien numeric(12,0),
			@error bit = 1
	set @thanhtien = (select (inserted.So_luong*Don_gia)
						from inserted join HangHoa on inserted.Ma_hang_hoa = HangHoa.Ma_hang_hoa)
	--KIỂM TRA MÃ HÀNG HÓA
	if not exists(select 1 from HangHoa where Ma_hang_hoa = @mahanghoa)
	begin
		print N'Mã hàng hóa không tồn tại'
		set @error = 0
		rollback
	end
	--KIỂM TRA MÃ PHIẾU NHẬP KHO
	if not exists(select 1 from Nhap where Ma_phieu_nhap_kho = @maphieunhapkho)
	begin
		print N'Mã phiếu nhập kho không tồn tại'
		set @error = 0
		rollback
	end
	if @error = 1
	begin
		insert into NhapChiTiet values(@stt,@soluong,@thanhtien,@mahanghoa,@maphieunhapkho)
	end
end
go
--KHI THÊM MỚI DỮ LIỆU VÀO BẢNG PHIẾU NHẬP CHI TIẾT THÌ THỰC NHẬP, TỔNG CỘNG CỦA BẢNG NHẬP VÀ SỐ LƯỢNG CỦA BẢNG HÀNG HÓA CŨNG SẼ NHẢY THEO
create or alter trigger tgCHANGE_INSERT_NHAP_HANGHOA
on NhapChiTiet
for insert
as
begin
	declare @maphieunhapkho varchar(10) = (select Ma_phieu_nhap_kho from inserted),
			@mahanghoa varchar(10) = (select Ma_hang_hoa from inserted),
			@thucnhap int,
			@tongcong numeric(12,0),
			@tongsoluong int
	set @thucnhap = (select sum(NhapChiTiet.So_luong) 
					 from NhapChiTiet join inserted on NhapChiTiet.Ma_phieu_nhap_kho = inserted.Ma_phieu_nhap_kho
					 where NhapChiTiet.Ma_phieu_nhap_kho = @maphieunhapkho)
	set @tongcong = (select sum(NhapChiTiet.Thanh_tien) 
					 from NhapChiTiet join inserted on NhapChiTiet.Ma_phieu_nhap_kho = inserted.Ma_phieu_nhap_kho
					 where NhapChiTiet.Ma_phieu_nhap_kho = @maphieunhapkho)
	set @tongsoluong = (select sum(NhapChiTiet.So_luong) 
						from NhapChiTiet join inserted on NhapChiTiet.Ma_hang_hoa = inserted.Ma_hang_hoa)
	--THỰC HIỆN CẬP NHẬT BẢNG NHẬP
	update Nhap
	set Thuc_nhap = @thucnhap, Tong_cong = @tongcong
	where Ma_phieu_nhap_kho = @maphieunhapkho
	--THỰC HIỆN CẬP NHẬT BẢNG HÀNG HÓA
	update HangHoa
	set So_luong = @tongsoluong
	where Ma_hang_hoa = @mahanghoa
end
--TEST CASE CHO TRƯỜNG HỢP THÊM PHIẾU NHẬP CHI TIẾT THÀNH CÔNG
INSERT INTO NhapChiTiet(So_luong,Ma_hang_hoa,Ma_phieu_nhap_kho)
VALUES(5,'XDAPMARTIN','PNHAP00001')
INSERT INTO NhapChiTiet(So_luong,Ma_hang_hoa,Ma_phieu_nhap_kho)
VALUES(10,'XDAPMARTIN','PNHAP00002')
--TEST CASE CHO TRƯỜNG HỢP THÊM PHIẾU NHẬP CHI TIẾT THẤT BẠI
--TEST CASE CHO TRƯỜNG HỢP MÃ HÀNG HÓA ĐÃ TỒN TẠI TRONG PHIẾU NHẬP
INSERT INTO NhapChiTiet(So_luong,Ma_hang_hoa,Ma_phieu_nhap_kho)
VALUES(5,'XDAPMARTIN','PNHAP00001')
--TEST CASE CHO TRƯỜNG HỢP MÃ HÀNG HÓA KHÔNG TỒN TẠI
INSERT INTO NhapChiTiet(So_luong,Ma_hang_hoa,Ma_phieu_nhap_kho)
VALUES(5,'XDAPLEONUI','PNHAP00001')
--TEST CASE CHO TRƯỜNG HỢP MÃ PHIẾU NHẬP KHO KHÔNG TỒN TẠI
INSERT INTO NhapChiTiet(So_luong,Ma_hang_hoa,Ma_phieu_nhap_kho)
VALUES(5,'XDAPMARTIN','PNHAP00010')

GO

--TẠO TRIGGER KHI CHỈNH SỬA PHIẾU NHẬP CHI TIẾT
--CHỈNH SỬA PHIẾU NHẬP CHI TIẾT
create or alter trigger tgUPDATE_PHIEUNHAPCHITIET
on NhapChiTiet
instead of update
as 
begin
	declare @stt int = (select So_thu_tu from inserted),
			@soluong int = (select So_luong from inserted),
			@error bit = 1
	if not exists (select 1 from NhapChiTiet where So_thu_tu = @stt)
	begin
		print N'Không có thông tin trong phiếu nhập chi tiết'
		set @error = 0
		rollback
	end
	if @error = 1
	begin
		update NhapChiTiet
		set So_luong = @soluong
		where So_thu_tu = @stt 
	end
end
go
--KHI CHỈNH SỬA DỮ LIỆU VÀO BẢNG PHIẾU NHẬP CHI TIẾT THÌ THỰC NHẬP, TỔNG CỘNG CỦA BẢNG NHẬP VÀ SỐ LƯỢNG CỦA BẢNG HÀNG HÓA CŨNG SẼ NHẢY THEO
create or alter trigger tgCHANGE_UPDATE_NHAP_HANGHOA
on NhapChiTiet
for update
as
begin
	declare @maphieunhapkho varchar(10), 
			@thucnhap int, 
			@tongcongtien numeric(12,0), 
			@tongcongnhap int,
			@stt int, 
			@thanhtien numeric(12,0), 
			@tongsoluong int, 
			@mahanghoa varchar(10)
	set @mahanghoa = (select Ma_hang_hoa from inserted)
	set @tongsoluong = (select sum(NhapChiTiet.So_luong) 
						from inserted join NhapChiTiet on inserted.Ma_hang_hoa = NhapChiTiet.Ma_hang_hoa)
	set @maphieunhapkho = (select Ma_phieu_nhap_kho from inserted)
	set @stt = (select So_thu_tu from inserted)
	set @thanhtien = (select (inserted.So_luong*Don_gia)
					  from inserted join HangHoa on inserted.Ma_hang_hoa = HangHoa.Ma_hang_hoa)
	set @thucnhap = (select sum(inserted.So_luong) 
					 from NhapChiTiet join inserted on NhapChiTiet.Ma_phieu_nhap_kho = inserted.Ma_phieu_nhap_kho)
	--CẬP NHẬT CỘT THÀNH TIỀN TRONG PHIẾU NHẬP CHI TIẾT
	update NhapChiTiet
	set Thanh_tien = @thanhtien
	where So_thu_tu = @stt
	--SET LẠI BIẾN TỔNG CỘNG
	set	@tongcongtien = (select sum(NhapChiTiet.Thanh_tien) 
						 from NhapChiTiet join inserted on NhapChiTiet.Ma_phieu_nhap_kho = inserted.Ma_phieu_nhap_kho)
	set @tongcongnhap = (select sum(NhapChiTiet.So_luong) 
						 from NhapChiTiet join inserted on NhapChiTiet.Ma_phieu_nhap_kho = inserted.Ma_phieu_nhap_kho)
	--THỰC HIỆN CẬP NHẬT PHIẾU NHẬP
	update Nhap
	set Thuc_nhap = @tongcongnhap, Tong_cong = @tongcongtien
	where Ma_phieu_nhap_kho = @maphieunhapkho
	--THỰC HIÊN CẬP NHẬT BẢNG HÀNG HÓA
	update HangHoa
	set So_luong = @tongsoluong
	where Ma_hang_hoa = @mahanghoa
end
--TEST CASE CHO TRƯỜNG HỢP CHỈNH SỬA PHIẾU NHẬP CHI TIẾT THÀNH CÔNG
UPDATE NhapChiTiet
set So_luong = 4
WHERE So_thu_tu = 9 
--TEST CASE CHO TRƯỜNG HỢP CHỈNH SỬA PHIẾU NHẬP CHI TIẾT THẤT BẠI
UPDATE NhapChiTiet
set So_luong = 5
WHERE So_thu_tu = 100

GO

--TẠO TRIGGER KHI XÓA PHIẾU NHẬP CHI TIẾT
--XÓA PHIẾU NHẬP CHI TIẾT
create or alter trigger tgDELETE_PHIEUNHAPCHITIET
on NhapChiTiet
instead of delete
as 
begin
	declare @stt int = (select So_thu_tu from deleted),
			@error bit = 1
	if not exists (select 1 from NhapChiTiet where So_thu_tu = @stt)
	begin
		print N'Không có thông tin trong phiếu nhập chi tiết'
		set @error = 0
		rollback
	end
	if @error = 1
	begin
		delete NhapChiTiet
		where So_thu_tu = @stt 
	end
end
go
--KHI XÓA DỮ LIỆU VÀO BẢNG PHIẾU NHẬP CHI TIẾT THÌ THỰC NHẬP, TỔNG CỘNG CỦA BẢNG NHẬP VÀ SỐ LƯỢNG CỦA BẢNG HÀNG HÓA CŨNG SẼ NHẢY THEO
create or alter trigger tgCHANGE_DELETE_NHAP_HANGHOA
on NhapChiTiet
for delete
as
begin
	declare @maphieunhapkho varchar(10) = (select Ma_phieu_nhap_kho from deleted),
			@mahanghoa varchar(10) = (select Ma_hang_hoa from deleted),
			@thucnhap int = (select (deleted.So_luong) from deleted),
			@tongcong numeric(12,0) = (select (deleted.Thanh_tien) from deleted),
			@soluong int = (select (deleted.So_luong) from deleted)
	--CẬP NHẬT LẠI SỐ LƯỢNG PHIẾU NHẬP
	update Nhap
	set Thuc_nhap = Thuc_nhap - @thucnhap, Tong_cong = Tong_cong - @tongcong
	where Ma_phieu_nhap_kho = @maphieunhapkho

	--CẬP NHẬT LẠI SỐ LƯỢNG BẢNG HÀNG HÓA
	update HangHoa
	set So_luong = So_luong - @soluong
	where Ma_hang_hoa = @mahanghoa
end
--TEST CASE CHO TRƯỜNG HỢP XÓA PHIẾU NHẬP CHI TIẾT THÀNH CÔNG
DELETE NhapChiTiet
WHERE So_thu_tu = 9 
--TEST CASE CHO TRƯỜNG HỢP XÓA PHIẾU NHẬP CHI TIẾT THẤT BẠI
DELETE NhapChiTiet
WHERE So_thu_tu = 100

GO


select * from auth_group

select * from auth_user

select * from auth_group_permissions

select * from auth_user_groups

select * from auth_user_user_permissions

select * from django_admin_log

select * from django_content_type

select * from django_migrations

select * from django_session

SELECT * FROM Kho
GO

SELECT * FROM Nhap
GO

SELECT * FROM HangHoa
GO

SELECT * FROM NguoiGiaoHang
GO

SELECT * FROM NhapChiTiet ORDER BY Ma_phieu_nhap_kho
GO
