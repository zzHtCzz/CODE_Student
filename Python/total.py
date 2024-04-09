try:
    a = int(input())
    b = int(input())
    tp = int(input())
    ten = str(input())
    print("total", a+b)
    print('xin', 'chao', 'toi', ten, sep = "--")
    print("Xin chao toi ten la {}".format("Hoà"))
    print(ten.replace(' ','--'))
    print("%o"%tp)
    #làm tròn
    print("{:.3f}".format(a/b))
    print(round(a/b, 2))
    #nhap cach khoang
    a = str(input())
    ds = map(int, a.split(' '))
    print(sum(ds))
except:
    print("Lỗi mất rồi!!!")