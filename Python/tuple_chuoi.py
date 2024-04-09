def xu_ly(ds):
    chuoi = all(i.isdigit() for i in ds)
    print(int(''.join(ds)))

ds = tuple(input("Nhập: ").split())
xu_ly(ds)
