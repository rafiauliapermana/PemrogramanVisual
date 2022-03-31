#Nama : Rafi Aulia Permana
#NIM  : 20051397071
#Prodi: D4 Manajemen Informatika (2020A)

class Stack(list):
    push = list.append

def modify_stack(symbolString):
    stack=Stack()
    result = []
    for character in symbolString:
        if character != '*':
            stack.push(character)
        else:
            result.append(stack.pop())
    return ''.join(result)
print(modify_stack('EAS*Y*QUE***ST***IO*N***'))