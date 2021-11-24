# le 5 pesos, mostra o maior e o menor
maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('digite peso: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('maior peso: {}'.format(maior))
print('menor peso: {}'.format(menor))
