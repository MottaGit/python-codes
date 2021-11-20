# le dias alugados e km percorrida
# calcula o custo do aluguel: R$60 por dia + R$0.15 por km
d = int(input('dias alugados: '))
km = float(input('km rodados: '))
preco = d*60 + km*0.15
print('total a pagar é R${:.2f}'.format(preco))