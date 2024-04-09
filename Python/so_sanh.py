ten1, cc1 = input("Nhập thông tin người 1: ").split()
ten2, cc2 = input("Nhâp thông tin người 2: ").split()

try:
    cc1 = int(cc1)
    cc2 = int(cc2)
    if cc1 <= 0 or cc2 <= 0:
        print("chieu cao khong duoc be hon 0")
    else:
        if cc1 > cc2:
            print("{} cao hon {}".format(ten1, ten2))
        elif cc1 < cc2:
            print("{} thap hon {}".format(ten1, ten2))
        else:
            print("{} bang {}".format(ten1, ten2))
except:
    print("Lỗi rồi !!!")