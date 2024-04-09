def tao(number, string):
    ds = dict(zip(number, string))
    print(ds)
    for value, chu in ds.items():
        print("{}:{}".format(value, chu))

number = input("Nhập: ").split()
string = input("Nhập: ").split()
tao(number, string)