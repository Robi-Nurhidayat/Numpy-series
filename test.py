
from typing import Counter



isTrue = True

listDonat = []
listToping = []
diskon = 0
potongan = 0
hasilSemetaraBayar = 0
totalPembayaran = 0

while(isTrue):

    inputNama = input("masukkan nama : ")
    inputJumlahPembelian = int(input('jumlah Pembelian : '))
    for i in range(1,4):
        inputListDonat = input(f"List donat madu pavorite ke-{i} : ")
        listDonat.append(inputListDonat)
    
    for j in range(1,4):
        inputListToping = input(f"List toping pavorit ke-{j} : ")
        listToping.append(inputListToping)

    inputTawaran = input('apakah anda ingin beli donut baru lagi ? y/n  : ')
    if(inputTawaran == 'y'):
        hargaDonutBaru = int(input('Harga Donut Baru : '))
        inputJumlahPembelianBaru = int(input('jumlah yang dibeli : '))
        print('jumlah pembelian sebelum nya : ',inputJumlahPembelian)
        totalJumlahPembelian = inputJumlahPembelian + inputJumlahPembelianBaru
        hasilSemetaraBayar = hargaDonutBaru * totalJumlahPembelian

        if( totalJumlahPembelian > 10 ):
            diskon = 0.25
            potongan = diskon * hasilSemetaraBayar
            totalPembayaran = hasilSemetaraBayar - potongan

        elif(totalJumlahPembelian >= 5):
            diskon = 0.1
            potongan = diskon * hasilSemetaraBayar
            totalPembayaran = hasilSemetaraBayar - potongan
        elif(totalJumlahPembelian >= 25):
            diskon = 0.3
            potongan = diskon * hasilSemetaraBayar
            totalPembayaran = hasilSemetaraBayar - potongan
        
        print('harga donut : ',hargaDonutBaru)
        print('total pembeliann',totalJumlahPembelian)
        print('diskon', diskon)
        print('total bayar ', totalPembayaran)

    cekRepeatOrNo = input('ulangi lagi ? y/n : ')
    if(cekRepeatOrNo == 'n'):
        isTrue = False

    

    
customer = {
    'nama' : inputNama,
    'jumlahBeli ' : inputJumlahPembelian + 1,
    'donat' : listDonat,
    'toping' : listToping
}


for key in customer.keys():
    print(f": {customer[key]}")



# for cus in customer:
#     print(customer['donat'])
# listDonat.append('donat')

# print(customer['nama'])
# print(customer['jumlahBeli '])
# print("donat",customer['donat'])
# print(customer['toping'])

# print(listDonat)