# jakenpô
# 1 - pedra
# 2 - papel
# 3 - tesoura
import random

j = int(input('1 - pedra\n2 - papel\n3 - tesoura\nescolha o seu: '))
c = random.randint(1,3)

if j == c:
    print('empate!')
elif j == 1:
    if c == 2:
        print('computador win!')
    else:
        print('jogador win!')
elif j == 2:
    if c == 1:
        print('jogador win!')
    else:
        print('computador win!')
elif j == 3:
    if c == 1:
        print('computador win!')
    else:
        print('jogador win!')
