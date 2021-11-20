# recebe distancia da viagem
# até de 200km R$0.5 por km, e RS0.45 por km para mais longas
distancia = float(input('digite a distancia: '))
if distancia > 200:
    valor = distancia*0.45
    print('valor será R${:.2f}'.format(valor))
else:
    valor = distancia*0.5
    print('valor será R${:.2f}'.format(valor))
