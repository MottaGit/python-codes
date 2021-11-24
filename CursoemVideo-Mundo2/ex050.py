# recebe 6 numeros, soma os pares
soma = 0
for i in range(0, 6):
    n = int(input('digite: '))
    if n%2 == 0:
        soma = soma + n
print('valor da soma', soma)
