customer = {}

inputJumlahCustomer = int(input('Masukkan jumlah customer : '))

counts = 1
listDonutPavorite = []
listTopingpavorite = []

while(counts <= inputJumlahCustomer):
    inputNama = input('Nama Customer : ')
    inputJumlahBeli = int(input('jumlah beli : '))
    inputJumlahDonutPavorit = int(input('Masukkan jumlah donut pavorit : '))
    print('isi list donut pavorit anda dibawah ini ')
    for i in range(1,inputJumlahDonutPavorit+1):
        donutPav = input('Donut Pavorit ke-1 : ')
        listDonutPavorite.append(donutPav)
    
    inputJumlahTopingPavorit = int(input('Masukkan jumlah toping pavorit : '))
    print('isi list topping pavorit anda dibawah ini')
    for i in range(1,inputJumlahTopingPavorit+1):
        topingPav = input('Toping Pavorit ke-1 : ')
        listTopingpavorite.append(topingPav)

    counts += 1



customer['nama'] = inputNama
customer['jumlah'] = inputJumlahBeli
customer['donut'] = listDonutPavorite
customer['toping'] = listTopingpavorite

print(customer)