def xu_ly(ds):
    maxinlist = max(ds)
    soluong = ds.count(maxinlist)
    print(maxinlist)
    print(soluong)
    for i in range(len(ds)):
        if ds[i] == maxinlist:
            print(i, end = " ")


ds = list(map(float, input("Nhập: ").split()))

if len(ds) == 0:
    print("Danh sach rong")
else:
    xu_ly(ds)
