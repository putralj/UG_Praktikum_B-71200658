import json

#baca data
with open('karyawan.json','r') as file:
    data = json.load(file)

#ambil data baru
jumlahInput = int(input('Masukkan jumlah karyawan baru : '))
for i in range(jumlahInput):
    daftarKolega = []
    nama = input('Masukan nama : ')
    alamat = input('Masukan alamat : ')
    jumlahKolega = int(input('Masukan jumlah kolega : '))
    for kolega in range(1,jumlahKolega+1):
        namaKolega = input('Masukan nama kolega ke-'+str(kolega)+": ")
        daftarKolega.append(namaKolega)
        newData = {nama : [{'Alamat':alamat},{'Kolega':daftarKolega}]}
        data.update(newData)
    print('=== Data berhasil ditambahkan ===\n')


# print(data)

#masukkan data ke file json
with open('karyawan.json','w') as dataKaryawan:
    json.dump(data,dataKaryawan)