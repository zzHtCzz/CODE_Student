import numpy as np
import math

def favorable(v, x):
    return x@v

def f_z(z):
    f = []
    for i in range(0, len(z)):
        f_value = round(1/(1+math.e**(-z[i])), 2)
        f.append(f_value)
    return f
    
def f_der(z):
    return (math.e**(-z))*(1/((1+math.e**(-z))**2))

def out(f, w):
    return f@w

def e_y(ynew, y):
    return (1/2)*(y - ynew[len(ynew)-1])**2

def w_update(w, ynew, y, f, n):
    w_new = []
    for i in range(0, len(w)):
        for j in range(0, len(w[i])):
            w_t = w[i][j] + n*(y-ynew)*f[i]
            w_new.append(w_t)
    return np.array(w_new).reshape(3, 1)

def v_update(v, ynew, y, z, n, x, w):
    v_new = []
    for i in range(0, len(v)):
        for j in range(0, len(v[i])):
            v_t = v[i][j] + n*(y-ynew)*w[j][0]*f_der(z[j])*x[i]
            v_new.append(v_t)
    return np.array(v_new).reshape(2, 3)

# khoi tao thong so mang
print("Khởi tạo thông số mạng: ")
v = np.array([-0.1, 0.1, 0.3, -0.2, 0.2, 0.4]).reshape(2, 3)
print("v: \n", v)
w = np.array([0.2, 0.4, 0.6]).reshape(3, 1)
w.shape
print("w: \n", w)
x = np.array([0, 1])
print("x: \n", x)
y = 1
n = 0.1
print("Đầu ra mong muốn:", y)
print("Thông số học: ", n)
i = 0
while True:
    print("===============================================LẶP LẦN {}=======================================================".format(i))
    #Lan truyen thuan
    print("Thực hiện lan truyền thuận: ")
    z = favorable(v, x)
    print("Z =", z)
    f = f_z(z)
    print("F =", f)
    y_out = out(f, w)
    print("y = ", y_out)
    e = e_y(y_out, y)
    print("E =", e)
    if e > 0.0000001:
        #Thực hiện lan truyền ngược
        w = w_update(w, y_out, y, f, n)
        print("Cập nhập W =", w)
        v = v_update(v, y_out, y, z, n, x, w)
        print("Cập nhập V =", v)
        i=i+1
    else:
        print("Kết thúc")
        break



