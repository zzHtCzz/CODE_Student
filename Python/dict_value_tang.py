def nhap_dict():
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

def xu_ly(n):
    dictA = {}
    dictvalue =  sorted(n.values())
    for i in dictvalue:
        for key, value in n.items():
            if i == value:
                dictA[key] = value
    print(dictA)

n = nhap_dict()
xu_ly(n)