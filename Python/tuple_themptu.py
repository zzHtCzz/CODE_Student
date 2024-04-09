def xu_ly(tuple1, tuple2, n):
    ketqua = tuple1[:n] + tuple2 + tuple1[n:]
    print(ketqua)


tuple1 = tuple(input("Nhập tuple1: ").split())
tuple2 = tuple(input("Nhập tuple2: ").split())
n = int(input("Nhập n: "))
xu_ly(tuple1, tuple2, n)