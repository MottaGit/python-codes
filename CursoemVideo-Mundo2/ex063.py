# recebe um valor n e exibe essa quantidade de termos de Fibonacci
n = int(input('termos Fibonacci: '))
t1 = 0
t2 = 1

if n == 1:
    print('{} -> FIM'.format(t1))
if n == 2:
    print('{} -> {} -> FIM'.format(t1, t2))

cont = 0
if n >= 3:
    print('{} -> {}'.format(t1, t2), end='')
    while cont < n-2:
        t3 = t1 + t2
        print(' -> {}'.format(t3), end='')
        t1 = t2
        t2 = t3
        cont += 1
print(' -> FIM')