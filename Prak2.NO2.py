#Nama : Rafi Aulia Permana
#NIM  : 20051397071
#Prodi: D4 Manajemen Informatika (2020A)


print("-------------------------------------------------")
print("Program Menghitung Volume Bangun Ruang")
print("-------------------------------------------------")

print("Silahkan pilih bangun ruang yang dihitung:))")
print(" 1. Tabung")
print(" 2. Balok")
print(" 3. Prisma Segitiga")

inp = int(input("Masukkan Pilihan Anda = "))

#Tabung
if inp == 1 :
    print("Anda Memilih : Tabung")

    jarijari = int(input("\nNilai Jari - Jari (cm) = "))
    tinggi = int(input("\nNilai Tinggi (cm) = "))
    print("\n ")
    print("-------------------------------------------------")
    pi = 22/7
    volume = pi*(jarijari*jarijari)*tinggi
    print("Hasil : ")
    inp = print("\nVolume Tabung = " , volume , "cm3")
    print("-------------------------------------------------")

elif inp == 2 :
    print("Anda Memilih : Balok")

    panjang = int(input("\nNilai Panjang (cm) = "))
    lebar = int(input("\nNilai Lebar (cm) = "))
    tinggi = int(input("\nNilai Tinggi (cm) = "))
    print("\n ")
    print("-------------------------------------------------")
    volume = panjang*lebar*tinggi
    print("Hasil : ")
    inp = print("\nVolume Balok = " , volume , "cm3")
    print("-------------------------------------------------")

elif inp == 3 :
    print("Anda Memilih : Prisma Segitiga")

    tinggiprisma = int(input("\nNilai Tinggi Prisma (cm) = "))
    tinggisegitiga = int(input("\nNilai Tinggi Segitiga (cm) = "))
    alassegitiga = int(input("\nNilai Alas Segitiga (cm) = "))
    print("\n ")
    print("-------------------------------------------------")
    volume = (1/2 * alassegitiga * tinggisegitiga) * tinggiprisma
    print("Hasil : ")
    inp = print("\nVolume Prisma Segitiga = " , volume , "cm3")
    print("-------------------------------------------------")


print("\n")
print(" SEKIAN TERIMA KASIH :)")