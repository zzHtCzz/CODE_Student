def kiem_tra_set(setX):
   #Ham len() hien thi so luong phan tu cua set
   if len(setX) % 2 == 0:
       #Ham clear() xoa tat ca phan tu trong set
       setX.clear()
   return setX

#Nhap set tu ban phim
setX = set(input().split())

#Goi ham va truyen cac tham so can thiet
setX = kiem_tra_set(setX)

print(setX)