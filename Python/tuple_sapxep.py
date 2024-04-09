#C1
"""def xu_ly(ds):
    for i in range(len(ds)):
        for j in range(i, len(ds)):
            if ds[i] < ds[j]:
                temp = ds[i]
                ds[i] = ds[j]
                ds[j] = temp
    print(tuple(ds))"""
#C2
def xu_ly(ds):
    ketqua = sorted(ds, reverse=True)
    print(ketqua)

ds = tuple(map(float, input("Nhập: ").split()))
xu_ly(ds)