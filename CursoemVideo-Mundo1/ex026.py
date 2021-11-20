# le uma frase
# informa quantos 'A' aparecem, posição da primeira  e ultima
frase = str(input('digite a frase: ')).upper().strip()
print('A aparece {} vezes'.format(frase.count('A')))
print('o primeiro A está na posição: {}'.format(frase.find('A')+1))
print('o ultimo A está na posição: {}'.format(frase.rfind('A')+1))
