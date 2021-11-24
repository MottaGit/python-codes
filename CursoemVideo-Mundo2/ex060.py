# fatorial do numero
n = int(input('numero: '))
num = 1

while n != 1:
    num *= n
    n -= 1

print(num)
