# le tres retas e diz se podem formar um triangulo
r1 = float(input('reta 1: '))
r2 = float(input('reta 2: '))
r3 = float(input('reta 3: '))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('podem formar triangulo!')
else:
    print('nao podem formar triangulo!')
