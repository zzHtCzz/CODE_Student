
a, pt, b = input("Nhập phép tính: ").split()

a = float(a)
b = float(b)

if pt == "+":
    print("{} {} {} = {}".format(a, pt, b, a+b))
elif pt == "-":
    print("{} {} {} = {}".format(a, pt, b, a-b))
elif pt == ":":
    if b == 0:
        print("Số bị chia phải khác 0!")
    else:
        print("{} {} {} = {}".format(a, pt, b, a/b))
else:
    print("{} {} {} = {}".format(a, pt, b, a*b))

