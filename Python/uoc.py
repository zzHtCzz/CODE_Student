def tim_uoc(n, tong):
    for i in range(1,n):
        if n % i == 0:
            tong = tong + i
    return tong

try:
    n = int(input("Nhập: "))
    if n < 0:
        print("Vui long nhập số tự nhiên!!!")
    else:
        tong = 0
        kq = tim_uoc(n, tong)
        if n == kq:
            print("{} la so hoan thien!!!".format(n))
        else:
            print("{} khong phai la so hoan thien!!!".format(n))

except:
    print("Dinh dang dau vao khong hop le!!!")