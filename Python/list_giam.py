def ktr_ds_giam(s):
    ketqua = all(s[i] >= s[i+1] for i in range(len(s)-1))
    return ketqua

s = list(map(float, input("Nhập: ").split()))
if len(s) == 0:
    print("Danh sach rong")
else:
    try:
        ketqua = ktr_ds_giam(s)
        print(ketqua)
    except:
        print("Dinh dang dau vao khong hop le!!!")