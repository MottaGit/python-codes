# le o sexo de uma pessoa, só aceita 'M' ou 'F'
sexo = str(input('informe o sexo [M/F]: ')).strip().upper()[0]

while sexo != 'M' and sexo != 'F':
    sexo = str(input('inválido! sexo [M/F]: ')).strip().upper()[0]

if sexo == 'M':
    print('sexo masculino [M] registrado!')
if sexo == 'F':
    print('sexo feminino [F] registrado!')
