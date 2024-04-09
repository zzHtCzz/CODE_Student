def do_dai_nhat(string):
    stringMax = ""
    for i in string:
        if len(i) >= len(stringMax) or (len(i) == len(stringMax) and i < stringMax):
            stringMax = i
    print(stringMax)


try:
    string = str(input("Nhập: "))
    string = string.split()
    do_dai_nhat(string)
except:
    print("Dinh dang dau vao khong hop le!!!")