def tt_va_kt(s):
    for count, value in enumerate(s):
        print(count, value)

try:
    s = input("Nhập: ").split()
    tt_va_kt(s)
except:
    print("Dinh dang dau vao khong hop le!!!")