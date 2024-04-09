def xu_ly(ds):
    setX = ds.copy()
    for i in setX:
        if i.isdigit():
            ds.remove(i)
    print(ds)

ds = set(input("Nhập: ").split())
xu_ly(ds)