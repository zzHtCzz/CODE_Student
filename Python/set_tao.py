def xu_ly(ds):
    maxds = max(ds)
    minds = min(ds)
    sumds = sum(ds)
    print(maxds)
    print(minds)
    print(sumds)

ds = set(map(float,input("Nhập: ").split()))
if len(ds) == 0:
    print("Danh sach rong")
else:
    xu_ly(ds)