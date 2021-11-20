# le numero de 0 a 9999, exibe digitos separados
num = int(input('digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: ', u)
print('Dezena: ', d)
print('Centena: ', c)
print('Milhar: ', m)
