import math

a = int(input("a="))
a = a/255
b = int(input("b="))
b = b/255
c = int(input("c="))
c = c/255
alpha = a - (0.5*(b+c))
beta = (math.sqrt(3)/2)*(b-c)
print(alpha)
print(beta)
h = math.degrees(math.atan(beta/alpha))
print("h = "+str(h))
s = math.sqrt(alpha*alpha + beta*beta)
print("s = "+str(s))
v = a + b + c
print("V = "+str(v))