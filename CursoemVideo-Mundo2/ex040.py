# le duas notas do aluno, mostra a media
# <5 reprovado, entre 5 e 6.9 rec e >7 aprovado
n1 = float(input('nota 1: '))
n2 = float(input('nota 2: '))

media = (n1+n2)/2

if media >= 7:
    print('aprovado, com media {:.2f}'.format(media))
elif media >= 5 and media < 6.9:
    print('recuperação, com media {:.2f}'.format(media))
else:
    print('reprovado, com media {:.2f}'.format(media))
