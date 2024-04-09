def nhap():
    listKey = input().split()
    try:
        listValue = list(map(int, input().split()))
    except:
        print("Vui long nhap value la so nguyen!")
        return None

    if len(listKey) != len(listValue):
        print("Vui long nhap so luong key va value bang nhau!")
        return None

    dictKetQua = dict(zip(listKey, listValue))
    return dictKetQua

def xu_ly(dictA):
    key = dictA.keys()
    value = dictA.values()
    print(dictA)
    print("-".join(key))
    print(sum(map(int, value)))

dictA = nhap()
xu_ly(dictA)