try:
    a, b, c = map(float, input("Nhập 3 cạnh của tam giác: ").split())
    if a+b>c and a+c>b and b+c>a:
        if a == b and b == c:
            print("{}, {}, {} là ba cạnh tam giác đều!".format(a, b, c))
        elif a == b or a == c or c == b:
            print("{}, {}, {} là ba cạnh tam giác cân!".format(a, b, c))
        elif a*a == b*b + c*c or a*a + b*b == c*c or b*b == a*a + c*c:
            print("{}, {}, {} là ba cạnh tam giác vuông!".format(a, b, c))
        elif a*a > b*b+c*c or b*b > a*a+c*c or c*c > a*a+b*b:
            print("{}, {}, {} là ba cạnh tam giác tù!".format(a, b, c))
        else:
            print("{}, {}, {} là ba cạnh tam giác nhọn!".format(a, b, c))
    else:
        print("Không phải là 3 cạnh của 1 tam giác")
except:
    print("Lỗi mất rồi!!!")