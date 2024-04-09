def ds_kitu(string):
    ds_kt = ""
    for i in string:
        if i not in ds_kt:
            ds_kt += i
    return ds_kt

def dem(string):
    chuoi_kt = ds_kitu(string)
    for i in chuoi_kt:
        dem = string.count(i)
        print("'{}':{}; ".format(i, dem), end ='')

try:
    string = input("Nhập: ")
    dem(string)
except:
    print("Dinh dang dau vao khong hop le!!!")