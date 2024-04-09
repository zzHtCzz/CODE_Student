def pt_le(s):
    ds = []
    for i in s:
        if i % 2 != 0:
            ds.append(i)
    return ds

s = list(map(float, input("Nhập: ").split()))
if len(s) == 0:
    print("Danh sach rong")
else:
    try:
        ds = pt_le(s)
        print(*ds)
    except:
        print("Dinh dang dau vao khong hop le!!!")