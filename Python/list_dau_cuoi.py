def xu_ly(ds1, ds2):
    ds2 = ds2[::-1]
    for i, j in zip(ds1, ds2):
        print(i*j, end = " ")


ds1 = list(map(float, input("Nhập: ").split()))
ds2 = list(map(float, input("Nhập: ").split()))

if len(ds1) != len(ds2):
    print("Vui long nhap 2 chuoi cung kich thuoc")
else:
    xu_ly(ds1, ds2)
