# recebe dois valores e faz a operação selecionada
n1 = int(input('numero 1: '))
n2 = int(input('numero 2: '))
n = 0

print('''[1] somar
[2] multiplicar
[3] maior
[4] novo numeros
[5] sair do programa''')

while n > 5 or n < 1:
    n = int(input('opção: '))
    if n == 1:
        soma = n1+n2
        print('{} + {} = {}'.format(n1, n2, soma))
    if n == 2:
        mult = n1*n2
        print('{} * {} = {}'.format(n1, n2, mult))
    if n == 3:
        if n1 > n2:
            print('maior é o:', n1)
        else:
            print('maior é o:', n2)
    if n == 4:
        n1 = int(input('numero 1: '))
        n2 = int(input('numero 2: '))
        n = 0
    if n == 5:
        break
