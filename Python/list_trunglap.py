def xuly(ds1, ds2):
    dsnw1 = [pt for pt in ds1 if pt not in ds2]
    dsnw2 = [pt for pt in ds2 if pt not in ds1]
    ketqua = dsnw1 + dsnw2
    print(*ketqua)


ds1 = list(input("Nhập1: ").split())
ds2 = list(input("Nhập2: ").split())

xuly(ds1, ds2)

