def minT(s):
    ngan = s[0]
    for i in s:
        if ngan > i:
            ngan = i
    return ngan

s = list(map(float, input("Nhập: ").split()))

if len(s) == 0:
    print("Danh sach rong")
else:
    try:
        ngan = minT(s)
        print(ngan)
    except:
        print("Dinh dang dau vao khong hop le!!!")