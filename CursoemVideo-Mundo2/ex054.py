# le 7 anos de nascimento, mostra quantas pessoas sao menor de idade
from datetime import date
maior = 0
atual = date.today().year
for i in range(0, 7):
    ano = int(input('digite ano: '))
    if (2021 - ano) < 18:
        maior+=1

print('{} pessoas são menor de idade'.format(maior))
