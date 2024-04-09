def vitri(ds, ptu):
    vitri = tuple(i for i in range(len(ds)) if ptu == ds[i])
    print(vitri)

            

ds = tuple(input("Nhập: ").split())
ptu = input("Nhập phần tử muốn tìm: ")
vitri(ds, ptu)
