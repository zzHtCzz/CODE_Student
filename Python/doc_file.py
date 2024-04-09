try:
    with open('Bai1.10.inp', 'r') as fileInp:
        #ten = fileInp.readline().rstrip('\n')
        #tuoiHientai = int(fileInp.readline())
        note = fileInp.read().splitlines()

    with open('bai1.10.out', 'w') as fileOut:
        #fileOut.write("Vao 20 nam nua, tuoi cua {} se la {}".format(ten, tuoiHientai + 20))
        fileOut.write(' '.join(note))

except:
    with open('bai1.10.out', 'w') as fileOut:
        fileOut.write("Khong tim thay file!!!")