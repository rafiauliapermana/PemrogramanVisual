#Nama : Rafi Aulia Permana
#NIM  : 20051397019
#Prodi: D4 Manajemen Informatika (2020A)


from typing import List


class Matriks:
    def __init__(self, data):
        self.data = data

    # penjumlahan 
    def m0(self):
        try:
            matriks1 = self.data['matriks1']
            matriks2 = self.data['matriks2']
            result = []

            for x in range(0, len(matriks1)):
                for y in range(0, len(matriks1[0])):
                    result.append(matriks1[x][y] + matriks2[x][y], end=' ')

            return result
        except:
            return 'parameter tidak sesuai'

    # pengurangan 
    def m1(self):
        try:
            matriks1 = self.data['matriks1']
            matriks2 = self.data['matriks2']
            result = []
            # print('success')
            for x in range(0, len(matriks1)):
                for y in range(0, len(matriks1[0])):
                    result.append(matriks1[x][y] + matriks2[x][y], end=' ')

            # print(str(result))
            return result
        except:
            return 'parameter tidak sesuai'

    # perkalian 
    def m2(self):
        try:
            matriks1 = self.data['matriks1']
            matriks2 = self.data['matriks2']
            result = []
            # print('success')
            for x in range(0, len(matriks1)):
                row = []
                for y in range(0, len(matriks1[0])):
                    total = 0
                    for z in range(0, len(matriks1)):
                        total = total + (matriks1[x][z] * matriks2[z][y])
                    row.append(total)
                result.append(row)

            for x in range(0, len(result)):
                for y in range(0, len(result[0])):
                    print (result[x][y], end=' ')

            # print(str(result))
            return result
        except:
            return 'parameter tidak sesuai'

    # determinan 
    def m3(self):
        try:
            matriks1 = self.data['matriks1']
            matriks2 = self.data['matriks2']
            matriks3 = self.data['matriks3']

            result = (matriks1[0]*matriks2[1]*matriks3[2] + matriks1[1]*matriks2[2]*matriks3[0] + matriks1[2]*matriks2[0]*matriks3[1] - matriks3[0]*matriks2[1]*matriks1[2] - matriks3[1]*matriks2[2]*matriks1[0] - matriks3[2]*matriks2[0]*matriks1[1])
            return result
        except:
            return 'parameter tidak sesuai'

    # transpose 
    def m4(self):
        try:
            matriks1 = self.data['matriks1']
            result = []

            for i in range(len(matriks1)):
                for j in range(len(matriks1)):
                    result.append(matriks1[j][i])
            return result
        except:
            return 'parameter tidak sesuai'


matriks = Matriks({'matriks1': [[5, 3, 2, 6, 9], [4, 2, 6, 1, 8]]})
print(str(matriks.m4()))