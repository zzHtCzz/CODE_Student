def them_phan_tu(danhSach, n):
   ketQua = []
   #Duyet cac phan tu cua danh sach voi buoc nhay la n
   for thuThu in range(0, len(danhSach), n):
       #Ham extend() them tung phan tu cua mot iterable vao cuoi danh sach
       ketQua.extend(danhSach[thuThu:thuThu+n])
       #Ham append() them phan tu vao cuoi danh sach
       ketQua.append('Kteam')
   #Ham pop() bo di mot phan trong dach sach, mac dinh la phan tu cuoi cung
   ketQua.pop()   
   return ketQua

#Nhap danh sach tu ban phim
danhSach = input().split()
#Kiem tra xem danh sach co rong hay khong
if len(danhSach) == 0:
   print("Danh sach rong")
else:
   #Khoi lenh co the phat sinh loi
   try:
       #Nhap gia tri n tu ban phim
       #Ep kieu du lieu sang so nguyen
       n = int(input())
       #Goi thuc thi ham va truyen tham so cho ham
       dsKetQua = them_phan_tu(danhSach, n)
       #Unpacking arguments
       print(*dsKetQua)

   #Khoi lenh duoc thuc thi khi loi xay ra
   except:
       print("Dinh dang dau vao khong hop le!")