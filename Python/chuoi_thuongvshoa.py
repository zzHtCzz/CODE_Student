
def hoa_thuong(n):
    if   n[0] >= "A" and  n[0] < "Z":
        print(n.upper())
    elif n[0] >= "a" and  n[0] < "z":
        print(n.lower())
    else:
        print(n)

#Cach 2
"""def bien_doi_chuoi(s):
   #Neu la chuoi rong thi tra ve chuoi rong
   if len(s) == 0:
       return ""
   #Su dung phuong thuc islower() de kiem tra ky tu viet thuong
   if s[0].islower():
       #Su dung phuong thuc lower() de tra ve chuoi voi cac ky tu viet thuong
       return s.lower()
   #Su dung phuong thuc isupper() de kiem tra ky tu in hoa
   if s[0].isupper():
       #Su dung phuong thuc upper() de tra ve chuoi voi cac ky tu viet hoa
       return s.upper()
   #Neu ky tu dau cua chuoi khong phai alphabet thi tra ve chuoi s
   return s"""

n = str(input("Nhập chuỗi: "))
hoa_thuong(n)