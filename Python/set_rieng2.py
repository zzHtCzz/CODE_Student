def ktr(ds1, ds2):
    print(ds1-ds2)
    print(ds2-ds1)


ds1 = set(input("Nhập 1: ").split())
ds2 = set(input("Nhập 2: ").split())
ktr(ds1, ds2)