
try:
    a, b = map(int, input("Nhập số: ").split())
    sum = 0
    if a > b:
        print("Số thứ 2 lớn hơn số thứ nhất!")
    else:
        for i in range(a, b+1):
            sum = sum + i
        print(sum)
        #while
        tong = 0
        i = a
        while i < (b+1):
            tong = tong + i
            i = i + 1
        print(tong)
   
except:
    print("Lỗi mất rồi!")

#else:
   #print("Done!")