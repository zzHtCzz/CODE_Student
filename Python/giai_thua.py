
"""def giai_thua(n):
    if n > 0:
        return n*giai_thua(n-1)
    else:
        return 1"""

#Khoi lenh co the phat sinh loi
try:
    #Nhap gia tri tu ban phim
    #Ep kieu du lieu sang so nguyen
    x = float(input())
    n = int(input())
   
    #Su dung cau truc re nhanh xu ly truong hop n < 0
    if n<0:
        print("Vui long nhap n la so tu nhien!")
    elif n == 0:
        print(1)
    else:
        ketQua = 1
        giaiThua = 1
        #Su dung vong lap for duyet cac so tu 1 toi n
        for i in range(1, 2*n+1):
            giaiThua *= i
            if i % 2 == 0:
                ketQua += pow(x, i)/giaiThua
            else:
                ketQua -= pow(x, i)/giaiThua 
        print('{:.5f}'.format(ketQua))
        
#Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")