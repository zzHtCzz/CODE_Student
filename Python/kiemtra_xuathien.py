def kiemtra(n, a):
    if a in n:
        print(n.count(a))
    else:
        print("{} khong xuat hien trong chuoi {}".format(a, n))

try:
    n = str(input("Nhap chuỗi: "))
    a = str(input("Nhap ki tu can dem: "))
    kiemtra(n, a)
except:
    print("Dinh dang dau vao khong hop le!!!")