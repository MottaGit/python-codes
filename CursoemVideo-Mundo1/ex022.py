# .find(x) - retorna o endereço que encontra o primeiro x
# .replace('a','bbbb') - troca os 'a' por 'bbb'
# .captalize() - só o primeiro maiúsculo
# .tittle() - primeira letra de cada palavra maiúscula

# Le um nome completo exibe: em maiusculo, em minusculo,
# numero de caracteres sem os espaços, letras primeiro nome

nome = input('digite um nome: ')
n = len(nome)
espace = nome.count(' ')
letras = n - espace
lista = nome.split()    # .split() - quebra a string em uma lista de strings
nfirst = len(lista[0])

print('maisculo: ', nome.upper())   # .upper() - torna string maiúscula
print('minusculo: ', nome.lower())  # .lower() - torna string minúscula
print('letras: ', letras)
print('letras primeiro nome: ', nfirst)
