def gom_nhom_tu(danhSach):
    dictKetQua = {}
    for tu in danhSach:
        if tu in dictKetQua:
            dictKetQua[tu].append(tu)
        else:
            dictKetQua[tu] = [tu]
    return dictKetQua

danhSach = input().split()

dictKetQua = gom_nhom_tu(danhSach)
print(dictKetQua)