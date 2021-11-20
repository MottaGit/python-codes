# le idade e mostra a categoria
idade = int(input('digite a idade do atleta: '))

if idade <= 9:
    print('categoria MIRIM')
elif idade <= 14:
    print('categoria INFANTIL')
elif idade <= 19:
    print('categoria JUNIOR')
elif idade <= 20:
    print('categoria SÊNIOR')
else:
    print('categoria MASTER')
