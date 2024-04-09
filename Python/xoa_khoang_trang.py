def xu_ly(string):
    while "  " in string:
        string = string.replace("  ", " ")
    return string

try:
    string = str(input("Nhập: "))
    string = string.strip()
    string = xu_ly(string)
    print(string)
except:
    print ("Dinh dang dau vao khong hop le!!!")