def lap(ds, dd):
    dodai =  len(ds)
    nhanban = dd // dodai+ 1
    ds = ds*nhanban
    print(*ds[:dd])


ds = input("Nhập: ").split()
dd = int(input("Nhập độ dài cần lặp: "))
lap(ds, dd)