
from typing import Counter



isTrue = True

listDonat = []
listToping = []

while(isTrue):

    inputNama = input("masukkan nama : ")
    inputJumlahPembelian = int(input('jumlah Pembelian : '))
    for i in range(1,4):
        inputListDonat = input(f"List donat madu pavorite ke-{i} : ")
    
    for j in range(1,4):
        inputListToping = input(f"List toping pavorit ke-{j} : ")

    listDonat.append(inputListDonat)
    listToping.append(inputListToping)
    cekRepeatOrNo = input('ulangi lagi ? y/n : ')
    if(cekRepeatOrNo == 'n'):
        isTrue = False


customer = {
    'nama' : inputNama,
    'jumlahBeli ' : inputJumlahPembelian,
    'donat' : listDonat,
    'toping' : inputListToping
}

for cus in customer:
    pass

# listDonat.append('donat')

# print(customer['nama'])
# print(customer['jumlahBeli '])
# print("donat",customer['donat'])
# print(customer['toping'])

# print(listDonat)