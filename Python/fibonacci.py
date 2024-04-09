
def fibonacii(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacii(n-1) + fibonacii(n-2)

try:
    n = int(input("Nhập số: "))
    if n < 0:
        print("Vui lòng nhập số nguyên dương")
    else:
        print(fibonacii(n))
except:
    print("Dinh dang dao vao khong hop le!!!")