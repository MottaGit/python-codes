# tenta adivinhar um numero de 0 a 10
import random
n = random.randint(0,10)
num = -1
tentativas = 0
while num != n:
    num = int(input('digite um nº entre 0 e 10: '))
    tentativas += 1
    if n == num:
        print('parabens! voce acertou em {} tentativa(s)'.format(tentativas))
    else:
        print('voce errou!'.format(n))
