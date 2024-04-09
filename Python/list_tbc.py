def xuly(ds):
    dodai = len(ds)
    tong = sum(ds)
    tbc = tong/dodai
    chuoibe = [so for so in ds if so <= tbc]
    chuoilon = [so for so in ds if so > tbc]
    print(tbc)
    print(*chuoibe)
    print(*chuoilon)

ds = list(map(float, input("Nhập: ").split()))
if len(ds) == 0:
    print("Danh sach rong")
else:
    xuly(ds)
