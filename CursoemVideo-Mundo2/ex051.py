# le primeira razao de uma PA
# mostra os 10 primeiros termos da PA
primeiro = int(input('primeiro termo: '))
razao = int(input('razao: '))

# decimo = primeiro + (10-1)*razao
for c in range(1,11):
    print(primeiro + (c-1)*razao)
