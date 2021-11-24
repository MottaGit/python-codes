# le um inteiro, diz se é primo
num = int(input('digite um numero: '))
m = 0

for c in range(2, num):
    if num%c == 0:
        m += 1

if m == 0:
    print('é primo')
else:
    print('nao é primo')
