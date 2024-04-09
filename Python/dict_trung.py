def nhap():
    key = input("Nhập: ").split()
    value = input("Nhập: ").split()
    if len(key) != len(value):
        print("Vui long nhap kich thuoc key va value bang")
    dictA = dict(zip(key, value))
    return dictA

def xoa_trung(dictA):
    listValue = list()
    dictketqua = dictA.copy()
    for key, value in dictA.items():
        if value in listValue:
            dictketqua.pop(key)
        else:
            listValue.append(value)
    return dictketqua

dictA = nhap()
if dictA is not None:
    dictKetQua = xoa_trung(dictA)
    print(dictKetQua)
