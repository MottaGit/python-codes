# recebe um ano e diz se ele é bissexto
ano = int(input('digite um ano: '))
if ano%4 == 0:
    print('é bissexto!')
else:
    print('não é bissexto')
