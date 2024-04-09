
def xen(s1, s2):
    dodai =  len(s1) + len(s2)
    s2 = s2[::-1]
    chuoi = ""
    for i in range(dodai):
        if i < len(s1):
            chuoi += s1[i]
        if i < len(s2):
            chuoi += s2[i]
    print(chuoi)


try:
    s1 = str(input("Nhập chuỗi 1: "))
    s2 = str(input("Nhập chuỗi 2: "))
    xen(s1, s2)
except:
    print("Dinh dang dau vao khong hop le!!!")