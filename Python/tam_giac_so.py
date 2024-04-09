try:
    a = int(input("Nhập chiều dài rộng: "))
    if a < 0:
        print("Vui long nhap gia tri tu 1 den 9!")
    else:
        for i in range(a+1, 1, -1):
            for j in range(1, i):
                print(j, end = '')
            print()
except:
    print("Lỗi mất rồi!!!")
