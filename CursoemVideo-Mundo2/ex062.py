# le primeira razao de uma PA
# mostra os 10 primeiros termos da PA
# pergunta quantos tempos mais

primeiro = int(input('primeiro termo: '))
razao = int(input('razao: '))

n = 0
termo = 0

while n != 10:
    termo += razao
    n += 1
    print(termo)

mais = 1
while mais != 0:
    mais = int(input('quantos termos a mais: '))
    a = 0
    if mais != 0:
        while a != mais:
            a += 1
            termo += razao
            print(termo)
