# le preco e forma de pagamento
preco = float(input('preço: '))
escolha = int(input('1-à vista\n2-à vista cartao\n3-até 2x cartão\n4-3x ou mais no cartão\nforma de pagamento: '))

if escolha == 1:
    print('preço final: R${:.2f}'.format(preco*0.9))
elif escolha == 2:
    print('preço final: R${:.2f}'.format(preco * 0.95))
elif escolha == 3:
    print('preço normal: R${:.2f}'.format(preco))
elif escolha == 4:
    print('preço final: R${:.2f}'.format(preco * 1.2))
