def xu_ly(string):
    string = string.strip()
    while "  " in string:
        string = string.replace("  "," ")
    string = string.split(".")
    for i in string:
        i = i.strip()
        i = i.title()
        print(i)

try:
    string = str(input("Nhập: "))
    xu_ly(string)

except:
    print("Dinh dang dau vao khong hop le!!!")