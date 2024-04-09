def ma_tran(m, n):
    matran = []
    for i in range(m):
        row = input("Nhập phần tử: ").split()
        if len(row) != n:
            print("Nhập không đủ phần tử")
            break
        else:
            matran.append(row)
    return matran

def ptu_chung(ds, m, n):
    ptutrung = []
    hangdau = ds[0]
    for ptu in hangdau:
        for j in ds:
            if ptu not in j:
                break      
        else:
            ptutrung.append(ptu)
    print(*ptutrung)

m, n = map(int, input("Nhập hàng cột: ").split())

if m < 0  or n < 0:
    print("Vui long nhap so nguyen duong!")
else:
    matran = ma_tran(m, n)
    ptu_chung(matran, m, n)
