try:
    n = int(input('Nhập số: '))
    ketqua = 0
    if n < 0:
            print("Nhập số tự nhiên")
    else:
        while n > 0: 
            so = n%10
            n = n//10
            ketqua = ketqua*10 + so
        print(ketqua)

except:
    print("Dinh dang dau vao khong hop le!!!")