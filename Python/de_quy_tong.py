def tinh_tong(n):
    if n == 0:
        return 0
    else:
        return n + tinh_tong(n-1)

try:
    n = int(input("Nhập độ dài cần tính: "))
    if n < 0:
        print("Vui long nhap so tu nhien!!!")
    else:
        print("tổng từ 1 đến {} là {}".format(n, tinh_tong(n)))
except:
    print("Dinh dang dau vao khong hop le!!!")