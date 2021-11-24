# le nome, idade e sexo de 4 pessoas
# exibe medias das idades, nome homem mais velho e quantas mulheres sub20
soma = 0
idadevelho = 0
nomevelho = ''
sub20 = 0

for c in range(1, 5):
    nome = str(input('nome: ')).strip()
    idade = int(input('idade:'))
    sexo = str(input('sexo [M/F]: ')).strip()
    soma += idade
    if (sexo == 'F' or sexo == 'f') and idade < 20:
        sub20 += 1
    if (sexo == 'M' or sexo == 'm') and idade > idadevelho:
        idadevelho = idade
        nomevelho = nome

media = soma/4
print('homem mais velho:', nomevelho)
print('idade homem mais velho:', idadevelho)
print('total de mulher com menos de 20: ', sub20)
print('media das idade: ', media)
