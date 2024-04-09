def them_list(ds1, ds2):
    for i in ds2:
        ds1.add(i)
    print(ds1)


ds1 = set(input("Nhập set: ").split())
ds2 = list(input("Nhập list: ").split())
them_list(ds1, ds2)