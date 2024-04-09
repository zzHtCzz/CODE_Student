def nhap_matran(m, n):
    ds = []
    for i in range(m):
        row = set(input("Nhập hàng {}: ".format(i)).split())
        ds.append(row)
        if len(row) != n:
            print("Nhập hàng đúng kích thước")
            return 
    return ds
#C1
"""def ktra(m, n):
    ds = nhap_matran(m,n)
    ds0 = set(ds[0])
    ptuchung = ds0.intersection(*[ptu for ptu in ds])
    print(ptuchung)"""

def ktra(m,n):
    ds =  nhap_matran(m, n)
    ds0 = set(ds[0])
    for i in ds:
        ptu = ds0 & i
    print(ptu)
    
m, n =  map(int, input("Nhập: ").split())
ktra(m,n)
