from dataclasses import replace

#cach 1
"""def thay_the(n):
    if "ing" in n:
        print(n.replace("ing", "ly"))
    else:
        print(n+"ing")"""
    
def thay_the(n):
    if "ing" == n[-3:]:
        print(n[:-3]+"ly")
    else:
        print(n+"ing")

try:
    n = str(input('Nhập chuỗi: '))
    thay_the(n)
except:
    print("Dinh dang dau vao khong hop le!!!")