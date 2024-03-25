# Métodos uteis set

#add, upate, clear, discard

set1 = set()

#adicionar um valor por vez ao set
set1.add('Luiz')
set1.add(1)

set1.update(('Olá mundo', 2,3,4))

#clear (limpar)
#set1.clear()

# eliminar um item ( colocar o valor)
set1.discard('Luiz')
#print(set1)

# Operadores uteis:
# União : união (união) - Une
# interseção & (intersection) - itens presentes em ambos
# diferença - itens presentes apenas no set da esquerda
# diferença simétrica ^- itens que não estão em ambos 
set2 = {1,2,3}
set3 = {2,3,4}
set4 = set2 | set3 # uniao de dois sets
set5 = set2 & set3 # itens presentes em ambos
set6 = set2 - set3 # itens exclusivo presentes no set da esquerda (ordem importa)
set7 = set2 ^ set3 # itens que não estão em ambos
#print(set7)

# teste 
l_A = [1,2,1,3]
l_B = [1,2,3]
set_B = set(l_B)
set_C = set(l_A)
l_C = list(set_C)

print(l_D)

if l_C != l_A:
    print(set_C, set_B)
    print('Houve repetição!')
    
else:
    print(l_C)
    print('Não houve repetição.')
