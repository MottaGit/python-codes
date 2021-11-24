# le varios numeros inteiros, exibe o maior e menor
# vai perguntando ao usuario quando ele quer parar

soma = media = quant = maior = menor = 0

continuar = 'S'
while continuar in 'Ss':
    num = int(input('numero: '))
    soma += num
    quant += 1

    continuar = str(input('continuar? [S/N] ')).strip().upper()[0]

    if quant == 1:
        maior = menor = num

    if num > maior:
        maior = num
    if num < menor:
        menor = num

media = soma / quant
print('maior: {}, menor: {} e media: {}'.format(maior, menor, media))
