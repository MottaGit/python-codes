# le peso e altura, calcula o IMC e mostra o status
altura = float(input('altura: '))
peso = float(input('peso: '))

imc = peso / altura**2

if imc < 18.5:
    print('abaixo do peso')
elif imc < 25:
    print('peso ideal')
elif imc < 30:
    print('sobrepeso')
elif imc < 40:
    print('obeso')
else:
    print('obeso mórbido')
