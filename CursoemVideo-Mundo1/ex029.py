# le velocidade do carro
# se maior que 80km/h recebe multa = R$7 a cada km/h acima de 80
velocidade = float(input('digite a velocidade: '))
if velocidade > 80:
    multa = 7*(velocidade - 80)
    print('pague uma multa de R${:.2f}'.format(multa))
else:
    print('tudo ok')
