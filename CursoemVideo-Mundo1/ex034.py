# le salario
# maior que 1250 aumento de 10%, menor que isso 15%
salario = float(input('digite o salario: '))
if salario < 1250:
    print('com o aumento será de: R${:.2f}'.format(salario*0.15))
else:
    print('com o aumento será de: R${:.2f}'.format(salario * 0.1))
