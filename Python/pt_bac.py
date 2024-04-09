import math 


def bac_mot(a, b):
    if a == 0:
        if b == 0:
            return "Phuong trinh vo so nghiem!!!"
        return "Phuong trinh vo nghiem"
    return "phuong trinh co nghiem la x = {}".format(-b/a)

def bac_hai(a, b, c):
    delta = float(b*b - 4*a*c)
    if a == 0:
        if b == 0:
            if c == 0:
                return "Phương trình vô số nghiệm"
            else:
                return "Phương trình vô nghiệm"
        else:
            return "Phuong trinh co mot nghiem duy nhat: \nx = {}".format(-c / b)
    else:
        delta = b * b - 4 * a * c
        #Kiem tra cac truong hop cua delta
        if delta > 0:
            x1 = float((-b + math.sqrt(delta)) / (2 * a))
            x2 = float((-b - math.sqrt(delta)) / (2 * a))
            return "Phuong trinh co hai nghiem phan biet la: \nx1 = {} \nx2 = {}".format(x1, x2)
        elif delta == 0:
            x = -b / (2 * a)
            return "Phuong trinh co nghiem kep: \nx1 = x2 = {}".format(x)
        else:
            return "Phuong trinh vo nghiem"

try:
    bac = int(input("Nhập: "))
    if bac == 1:
        a, b= map(float, input("Nhập tham số phương trình: ").split())
        print(bac_mot(a, b))
    else:
        a, b, c = map(float, input("Nhập tham số phương trình: ").split())
        print(bac_hai(a, b, c))
except:
    print("Lỗi mất rồi!!!")