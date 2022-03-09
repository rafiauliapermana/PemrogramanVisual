# Nama  : Rafi Aulia Permana
# NIM   : 20051397071
# Prodi : D4 Manajemen Informatika (2020A)

kata = input ("Masukkan kata :")
kunci = int (input ("Masukkan kunci :"))

def caesar_cipher(kata,kunci):
    hasil = ""
    for i in range(len(kata)):
        if (kata[i] == " "):
            hasil += " "
        else:
            hasil += chr(ord(kata[i]) + kunci)
    return hasil
print(caesar_cipher('kata',kunci))
