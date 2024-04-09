def xuly(ds):
    demktu = ds.count('0')
    dem0 = [pt.count('0') for pt in ds]
    return demktu, sum(dem0)

ds = tuple(input("Nhập: ").split())
dem0 = xuly(ds)
print(dem0)