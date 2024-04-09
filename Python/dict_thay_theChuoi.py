def nhap_dict():
    listKey = input().split()
    listValue = input().split()
    if len(listKey) != len(listValue):
        print("Vui long nhap so luong key va value bang nhau!")
        return None
    dictA = dict(zip(listKey, listValue))
    return dictA

def xu_ly(dictA, chuoi):
    chuoinew = chuoi.split()
    listKey = dictA.keys()
    for i in listKey:
        for j in chuoinew:
            if j == i:
                chuoi = chuoi.replace(j, dictA[i])
    print(dictA)
    print(chuoi)

chuoi = input()
dictA = nhap_dict()
xu_ly(dictA,chuoi)
