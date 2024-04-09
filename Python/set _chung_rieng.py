
"""def ktr(ds1, ds2):
    ketquachung = set(i for i in ds1 if i in ds2)
    ketquarieng = set()
    for i in ds1:
        if i not in ds2:
            ketquarieng.add(i)
    for i in ds2:
        if i not in ds1:
            ketquarieng.add(i)
    print(ketquachung)
    print(ketquarieng)

ds1 = input("Nhập 1: ").split()
ds2 = input("Nhập 2: ").split()
ktr(ds1, ds2)"""

#C2
def ptu_chung_ptu_tieng(setX, setY):
   setRieng = setX ^ setY
   setChung = setX & setY
   return setRieng, setChung

#Nhap set tu ban phim
setX = set(input().split())
setY = set(input().split())

#Goi ham va truyen cac tham so can thiet
setRieng, setChung = ptu_chung_ptu_tieng(setX, setY)

print(setRieng)
print(setChung)
