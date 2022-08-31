def tambah(num1,num2):
    hasil = num1 + num2
    print(hasil)

def kurang(num1,num2):
    hasil = num1 - num2
    print(hasil)

def kali(num1,num2):
    hasil = num1 - num2
    print(hasil)

def bagi(num1,num2):
    hasil = num1 - num2
    print(hasil)

def menu():
    print('========== KALKULATOR SEDERHANA ==========')

    print('1. Penjumlahan')
    print('2. Pengurangan')
    print('3. Perkalian')
    print('4. Pembagian')
    print('Keluar (Q)')

def proses(pilihan):
    if pilihan == 1:
        bil1 = int(input('Bilangan 1 : '))
        bil2 = int(input('Bilangan 2 : '))
        tambah(bil1,bil2)

    elif pilihan == 2:
        bil1 = int(input('Bilangan 1 : '))
        bil2 = int(input('Bilangan 2 : '))
        kurang(bil1,bil2)

    elif pilihan == 3:
        bil1 = int(input('Bilangan 1 : '))
        bil2 = int(input('Bilangan 2 : '))
        kali(bil1,bil2)

    elif pilihan == 4:
        bil1 = int(input('Bilangan 1 : '))
        bil2 = int(input('Bilangan 2 : '))
        bagi(bil1,bil2)

    elif pilihan == 'q' or 'Q':
        print('Program berhenti....')

def tanya():
    inputUser = int(input('Masukkan Pilihan Anda : '))
    return inputUser


menu()
tanya()
proses(tanya)