# le valores até que 999 seja digitado, soma eles e exibe
n = 0
soma = 0
digitados = 0

while n != 999:
    n = int(input('n = '))
    if n != 999:
        digitados += 1
        soma += n
print('foram digitado {} numeros, soma deles é {}'.format(digitados, soma))
