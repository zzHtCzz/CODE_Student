def xu_ly(string):
    if string.startswith('*') and string.endswith('*'):
        return string.title()
    elif string.startswith('-') and string.endswith('-'):
        return string.swapcase()
    return string.capitalize()
    
try:
    string = str(input("Nhập: "))
    string = xu_ly(string)
    print(string)
except:
    print("Dinh dang dau vao khong hop le!!!")