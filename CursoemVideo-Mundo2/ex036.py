# Le valor da casa, salario e quantos anos vai pagar
# calcula mensalidade, porem nao pode ser maior que 30% salario
valor = float(input('valor da casa: '))
salario = float(input('salario: '))
anos = int(input('anos para pagar: '))

mensalidade = valor/(anos*12)

if mensalidade > salario*0.3:
    print('voce não pode comprar essa casa!')
else:
    print('mensalidade será de R${:.2f}'.format(mensalidade))
