def dict_so_chinh_phuong(n):
    #Cach 1: Them thu cong mot phan tu vao dict
    # dictKetQua = dict()
    # for i in range(n):
    #     dictKetQua[i] = i*i

    #Cach 2: Su dung Dict Comprehension
    dictKetQua = {i:i*i for i in range(n)}
    return dictKetQua

#Khoi lenh co the phat sinh loi
try:
    #Nhap gia tri tu ban phim
    #Ep kieu du lieu sang so nguyen
    n = int(input())    
    if n < 0:
        print("Vui long nhap so nguyen duong!")
    else:
        #Goi ham va truyen cac tham so can thiet
        dictKetQua = dict_so_chinh_phuong(n)
        print(dictKetQua)
#Khoi lenh duoc thuc thi khi loi xay ra
except:
    print("Dinh dang dau vao khong hop le!")