# recebe 4 nomes de alunos, sorteia a ordem de apresenção
import random
a1 = input('aluno 1: ')
a2 = input('aluno 2: ')
a3 = input('aluno 3: ')
a4 = input('aluno 4: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)

print('ordem apresentação: ')
print(lista)