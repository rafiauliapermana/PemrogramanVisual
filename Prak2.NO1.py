#Nama : Rafi Aulia Permana
#NIM  : 20051397071
#Prodi: D4 Manajemen Informatika (2020A)


print("-------------------------------------------------")
print("Program Menghitung Luas dan keliling Bangun Datar")
print("-------------------------------------------------")

print("Silahkan pilih bangun datar yang akan dihitung . . .")
print(" 1. Persegi")
print(" 2. Segitiga")
print(" 3. Jajar Genjang")

inp = int(input("Masukkan Pilihan Anda = "))

#Persegi
if inp == 1 : 
    print("Anda Memilih : Persegi")

    sisi = int(input("\nNilai Panjang Sisi (cm) = "))
    print("\n ")
    print("-------------------------------------------------") 

    luas = sisi*sisi
    keliling = 4 * sisi
    print("Hasil : ")
    inp = print("\nLuas Persegi = " , luas , "cm2")
    inp = print("\nKeliling Persegi = " , keliling , "cm")
    print("-------------------------------------------------")

#Segitiga
elif inp == 2 :
    print("Anda Memilih : Segitiga")

    alas = int(input("\nNilai Panjang Alas (cm) = "))
    tinggi = int(input("\nNilai Panjang Tinggi (cm) = "))
    sisi = int(input("\nNilai Panjang Sisi (cm) = "))
    print("\n ")
    print("-------------------------------------------------")
    luas = alas*tinggi
    keliling = 3 * sisi
    print("Hasil : ")
    inp = print("\nLuas Segitiga = " , luas , "cm2")
    inp = print("\nKeliling Segitiga = " , keliling , "cm")
    print("-------------------------------------------------")

#JajarGenjang
elif inp == 3 :
    print("Anda Memilih : Jajar Genjang")

    alas = int(input("\nNilai Panjang Alas (cm) = "))
    tinggi = int(input("\nNilai Panjang Tinggi (cm) = "))
    sisimiring = int(input("\nNilai Panjang Sisi Miring (cm) = "))
    print("\n ")
    print("-------------------------------------------------")
    luas = alas*tinggi
    keliling = 2*(alas + sisimiring)
    print("Hasil : ")
    inp = print("\nLuas Jajar Genjang = " , luas , "cm2")
    inp = print("\nKeliling Jajar Genjang = " , keliling , "cm")
    print("-------------------------------------------------")


print("\n")
print(" SEKIAN TERIMA KASIH :))")