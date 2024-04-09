def tbc(s):
    chuoi = list(s)
    dodai = len(chuoi)
    tong = sum(map(float, chuoi))
    return tong/dodai

s = input("Nhap: ").split()

if len(s) == 0:
   print("Danh sach rong")
else:
    try:
        tbc = tbc(s)
        print(tbc)
    except:
        print("Dinh dang dau vao khong hop le!!!")