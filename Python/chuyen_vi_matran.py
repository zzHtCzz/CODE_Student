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

def chuyenvi(m, n):
    matran = ma_tran(m, n)
    matran_CV = []
    row = []
    m = len(matran[0])
    n = len(matran)
    for i in range(m):
        row = [matran[j][i] for j in range(n)]
        matran_CV.append(row)
    
    for i in range(m):
        for j in range(n):
            print(matran_CV[i][j], end = " ")
        print()
        
m, n = map(int, input("Nhập: ").split())
if m < 0 or n < 0:
    print("Vui long nhap kich thuoc danh sach la so nguyen duong!")
else:
    chuyenvi(m,n)