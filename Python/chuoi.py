def tra_ve(n1, n2):
    if len(n1) <= 5:
        n1 = n1*3
    else:
        n1 = n1

    if len(n2) <= 5:
        n2 = n2 * 3
    else:
        n2 = n2

    print(n1 + n2)
    

try:
    n1, n2 = map(str,input("Nhập chuỗi: ").split())
    tra_ve(n1, n2)
except:
    print("Dinh dang dau vao khong hop le!!!")