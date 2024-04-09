def tinh_tong(*args):
    tong = 0
    for i in args:
        tong += i
    return tong

print("1 + 2 + 3 + 4 = {}".format(tinh_tong(1, 2, 3, 4)))