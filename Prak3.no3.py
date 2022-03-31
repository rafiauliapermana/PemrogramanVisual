#Nama : Rafi Aulia Permana
#NIM  : 20051397071
#Prodi: D4 Manajemen Informatika (2020A)

class stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def IsEmpty(self):
        return self.items == []

    def peek (self):
        if not self.IsEmpty():
            return self.items[-1]

    def get_stack (self):
        return self.items

def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])

    rev_str = ""
    while not stack.IsEmpty():
        rev_str += stack.pop()

    return rev_str

stack = stack()
input_str = "Rafi Aulia Permana"
print("Kata yang dimasukkan : ",input_str)
print("Jika dibalik menjadi : ",reverse_string(stack, input_str))