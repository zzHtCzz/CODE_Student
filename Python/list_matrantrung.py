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

def xu_ly(m, n):
    matran = ma_tran(m, n)
    maxrow = []
    
    for i in matran:
        dodaimax = 0
        for j in i:
            if dodaimax < len(j):
                dodaimax = len(j)
            
        for j in i:
            if len(j) == dodaimax:
                maxrow.append(j)
                break
    print(*maxrow)
            

m, n = map(int, input("Nhập kích thước: ").split())
if m < 0 or n < 0:
    print("Vui long nhap kich thuoc danh sach la so nguyen duong!")
else:
    xu_ly(m, n)