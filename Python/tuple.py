#cach1
from ctypes import sizeof


c1 = ("Kteam", 2021, True)
print(c1)

#cach 2
c2 = tuple([2021, 'Kteam', False])
print(c2)

n = input("Nhập: ")
ds = tuple(i for i in range(int(n)))
print(ds)

ds2 = tuple(n*int(n))
ds3 = (n, ds2)
print(ds3)

