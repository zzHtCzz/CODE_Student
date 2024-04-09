def dao(a, b, n):
    chuoi_con = n[a:b+1]
    print(chuoi_con[::-1])

try:
    n = str(input("Nhập chuỗi: "))
    a, b = map(int,input("Nhập độ dài cần đảo: ").split())
    if a > b:
        print("Vui long nhap a < b")
    elif a<0 or b < 0:
        print("Vui long nhap so tu nhien")
    elif b > len(n):
        print("Do dai khong duoc lon hon do dai chuoi")
    else:
        dao(a, b, n)
except:
    print("Dinh dang dau vao khong hop le!!!")