def xu_ly(string, ds, dem):
    for i in string:
            for j in ds:
                if i == j:
                    dem += ds.count(i)
                    string = string.replace(i, "$")
    print(dem)
    print(string)

try:
    string = str(input("Nhập: "))
    ds = str('AaEeOoIiUu')
    dem = 0
    xu_ly(string, ds, dem)
except:
    print("Dinh dang dau vao khong hop le!!!")