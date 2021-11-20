# le o nome de uma cidade e diz se ela começa com o nome 'santo'
city = input('digite o nome da cidade: ')
lista = city.split()

print('começa com "SANTO"? ')
print(lista[0].upper() == 'SANTO')
