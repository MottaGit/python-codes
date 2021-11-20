# le um nome, exibe o primeiro e o ultimo nome
nome = str(input('digite seu nome: ')).strip()
lista = nome.split()
print('primeiro nome: {}'.format(lista[0]))
print('ultimo nome: {}'.format(lista[len(lista)-1]))
