def ma_tran(m, n):
    matran = []
    for i in range(m):
        row = input("Nhập phần tử: ").split()
        if len(row) != n:
            print("Nhập không đủ phần tử")
            break
        else:
            matran.append(row)
    for i in range(m):
        for j in range(n):
            print(matran[i][j], end = " ")
        print()
    

m, n = map(int, input("Nhập: ").split())
ma_tran(m, n)
