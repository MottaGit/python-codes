# le ano de nascimento e diz sobre o alistamento militar
ano = int(input('ano nascimento: '))
ano_atual = 2021
idade = ano_atual - ano
if idade == 18:
    print('precisa se alistar')
elif idade > 18:
    print('ja passou do tempo de alistamento em {} anos'.format(idade-18))
elif idade < 18:
    print('ainda vai se alistar, daqui a {} anos'.format(18-idade))
