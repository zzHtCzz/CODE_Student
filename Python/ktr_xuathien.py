def ktr_xh(s):
    dem = danhsach.count(s)
    return dem

def xuat(s):
    dsnew = [pt for pt in danhsach if ktr_xh(pt) < 2]
    print(*dsnew)


danhsach = list((input("Nhập: ").split()))
if len(danhsach) == 0:
    print("Danh sach rong")
else:
    xuat(danhsach)