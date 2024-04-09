def list_tang(s):
    temp = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i] > s[j]:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
    return s

    

s = list(map(int, input("Nhập: ").split()))

if len(s) == 0:
    print("Danh sach rong")
else:
    ds = list_tang(s)
    print(*ds)