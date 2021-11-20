# Le um numero inteiro, converte para bin, octal ou hexa
num = int(input('digite numero inteiro: '))
n = int(input('''escolha uma das opções
1-binario
2-octal
3-hexadecimal
digite a opção: '''))

if n == 1:
    print('convertido em BINARIO: {}'.format(bin(num)))
elif n == 2:
    print('convertido em OCTAL: {}'.format(oct(num)))
elif n == 3:
    print('convertido em HEXADECIMAL: {}'.format(hex(num)))
