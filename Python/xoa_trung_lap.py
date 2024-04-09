def xoa(string):
    strN = ""
    for i in string:
        if i not in strN:
            strN += i

    print (strN)

try:
    string = str(input("Nhập: "))
    xoa(string)
except:
    print("Dinh dang dau vao khong hop le!!!")