def nhap_dict():
    key = input("Nhập key: ").split()
    value = input("Nhập value: ").split()
    if len(key) != len(value):
        print("Vui long nhap so luong key va value bang nhau!")
        return None
    dict1 = dict(zip(key, value))
    return dict1

def update_dict(dictA, dictB):
    if len(dictA) < len(dictB):
        dictB.update(dictA)
        return dictB
    dictA.update(dictB)
    return dictA

dictA = nhap_dict()
dictB = nhap_dict()

dict_update = update_dict(dictA, dictB)
print(dict_update)
    



