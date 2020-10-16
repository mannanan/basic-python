  
def kontaklama(kolam) :
    for kontak in kolam :
        print("-------------------------")
        print(f"Nama : {kontak['nama']}")
        print(f"Telepon : {kontak['telepon']}")


def kontakbaru():
    nama = input("Masukkan Nama : ")
    telepon = input("Masukkan Nomor Telepon : ")
    kontak = {
        "nama" : nama,
        "telepon" :telepon
    }
    return kontak


kolam = []
kolam.append ({
    "nama" : "Maman",
    "telepon" : "911"
})
 

while True :
    print("Selamat Datang di Buku Telepon")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("0. Keluar program")

    menu = input("pilih menu :")

    if menu == "0":
        break
    elif menu == "1" :
        kontaklama(kolam)
    elif menu =="2" :
        kontak = kontakbaru()
        kolam.append(kontak)
    else :
        print("Silahkan tekan 0,1,atau 2")

print("Selesai, perubahan telah tersimpan")