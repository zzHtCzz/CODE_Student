n = str(input("Nhap chuoi: "))
if len(n) % 2 == 0:
    print(n[1::2])
else:
    print(n[::2])

#cach 2
"""def xoa_ky_tu(s):
   chuoiKetQua = ""
   doDaiChuoi = len(s)
   #Su dung vong lap for de duyet cac ky tu cua chuoi
   for i in range(doDaiChuoi):
       #Neu do dai chuoi la so chan thi giu lai ky tu le
       #Neu do dai chuoi la so le thi giu lai ky tu chan
       if i % 2 != doDaiChuoi % 2:
           chuoiKetQua += s[i]
   return chuoiKetQua"""
