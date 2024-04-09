def list_ky_tu_dao_nguoc(s):
   #Su dung constructor list de khoi tao list tu chuoi
   dsKyTu = list(s)
   #Dao nguoc cac phan tu cua list
   dsKyTuDaoNguoc = dsKyTu[::-1]
   return dsKyTuDaoNguoc

#Nhap gia tri tu ban phim
s = input()

#Goi ham va truyen cac tham so can thiet
dsKyTuDaoNguoc = list_ky_tu_dao_nguoc(s)

#Su dung Unpacking arguments de hien thi danh sach
print(*dsKyTuDaoNguoc)