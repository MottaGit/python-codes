# computador gera um aleatório entre 0 e 5 e o usuario tenta acertar
import random
n = random.randint(0,5)
num = int(input('digite um n entre 0 e 5: '))
if n == num:
    print('parabens!')
else:
    print('voce errou! o numero era {}'.format(n))
