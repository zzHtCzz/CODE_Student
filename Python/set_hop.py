def ktr(ds1, ds2):
    return ds2 <= ds1


ds1 = set(input("Nhập: ").split())
ds2 = set(input("Nhập: ").split())
ktr = ktr(ds1, ds2)
print(ktr)