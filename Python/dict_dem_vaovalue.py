def xu_ly(n):
    dictA = dict()
    for i in n:
        if i in dictA:
            dictA[i] += 1
        else:
            dictA[i] = 1
    print(dictA)

n = input("Chuoi: ")
xu_ly(n)