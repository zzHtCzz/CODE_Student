from pickle import TRUE


def dem(string):
    countKT = ""
    countCH = ""
    countSo = ""
    for i in string:
        if i.islower() or i.isupper():
            countCH += i
        elif i.isdigit():
            countSo += i
        else:
            countKT += i
    chuoi = countSo + countCH + countKT
    return len(countKT), len(countCH), len(countSo), chuoi

def demchu(string):
    count1 = False
    count2 = False
    count = 0
    string = string.split()

    for i in string:
        count1 = False
        count2 = False
        for j in i:
            if j.isdigit():
                count1 = True
            if j.isalpha():
                count2 = True

        if count1 and count2:
            count = count + 1
    return count

try:
    string = input("Nhập: ")
    demz = demchu(string)
    print(demz)
except:
    print("Dinh dang dau vao khong dinh dang!!!")