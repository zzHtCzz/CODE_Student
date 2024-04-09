
def xu_ly(ds1, ds2):
    dodai1 = len(ds1)
    dodai2 = len(ds2)
    half1 = dodai1//2
    half2 = dodai2//2
    nuads_1 = ds1[half1:]
    ds1 = ds1[:half1]+ds2[half2:]
    ds2 = ds2[:half2]+nuads_1
    print(*ds1)
    print(*ds2)

ds1 = input("Nhập: ").split()
ds2 = input("Nhập: ").split()

xu_ly(ds1, ds2)
