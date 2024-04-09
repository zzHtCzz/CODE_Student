def demktu(ds):
    ktu = set(ds)
    for i in ktu:
        dem =  ds.count(i)
        print("'{}' : {}".format(i, dem), end = ",")

ds = input("Nhập: ")
demktu(ds)
