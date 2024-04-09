
import math

def ktr_nguyento(s):
    if s < 0:
        return False
    else:
        for i in range(2, int(math.sqrt(s))+1):
            if s % i == 0:
                return False
    return True

def loc(s):
    ds = [so for so in danhsach if ktr_nguyento(so)]
    print(*ds) 

danhsach = list(map(int, input("Nhập: ").split()))

if len(danhsach) == 0:
    print("Danh sach rong!!!")
else:
    loc(danhsach)
