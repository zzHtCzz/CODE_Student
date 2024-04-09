def nhap(n):
    ds = []
    for i in range(n):
        row = map(int, input("Nhập phần tử: ").split())
        ds.append(tuple(row))
        tupleX = tuple(ds)
    return tupleX

def xu_ly(ds):
    chuoitong = []
    print(ds)
    chuoitong = tuple(sum(ptu) for ptu in ds)
    print(tuple(chuoitong))


try:
    n = int(input("Nhập: "))
    ds = nhap(n)
    xu_ly(ds)
except:
    print("Dinh dang dau vao khong hop le")