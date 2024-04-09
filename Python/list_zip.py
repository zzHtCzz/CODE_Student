def xoa_khoang_trang(ds):
    ds =  ds.strip()
    while "  " in ds:
        ds =  ds.replace("  ", " ")
    return ds

def xu_ly(ds1, ds2):
    ds1 = [xoa_khoang_trang(i) for i in ds1]
    ds2 = [xoa_khoang_trang(j) for j in ds2]
    for ten, quoctich in zip(ds1, ds2):
        print("{} - {}".format(ten, quoctich))


ds1 = input("Nhập: ").split(",")
ds2 = input("Nhập: ").split(",")

if len(ds1) != len(ds2):
    print("Vui long nhap kich thuoc 2 danh sach giong nhau!!!")
else:
    xu_ly(ds1, ds2)
