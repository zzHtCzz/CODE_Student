def nhap():
    try:
        key =  list(map(int,input("Nhập: ").split()))
    except:
        print("Vui long nhap key la so nguyen!")
        return None
    value = input("Nhập value: ").split()

    if len(key) != len(value):
        print("Vui long nhap so luong key va value bang nhau!")
        return None
    
    dictA = dict(zip(key, value))
    return dictA

def xu_ly(dictA):
    dictkey = sorted(dictA.keys())
    dictketqua = {}
    for i in dictkey:
        dictketqua[i] = dictA[i]
    print(dictketqua)
dictA = nhap()
xu_ly(dictA)