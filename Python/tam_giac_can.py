try:
    n = int(input("Nhập độ dài: "))
    if(n < 0):
        print("Vui long nhap so tu nhien!")
    else:
        maAscii = 65
        for i in range(n):
            khoangtrang = " "*((n-i)*2-1)
            print(khoangtrang, end = '')
            for j in range(2*i + 1):
                chuCai = chr(maAscii)
                print(chuCai, end =' ')
                maAscii += 1
                if chr(maAscii) > "Z":
                    maAscii = 65
            print()
                

except:
    print("Dinh dang dau vao khong hop le!!!")
