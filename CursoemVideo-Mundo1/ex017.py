# Le cateto oposto e adjacente e calcula hipotenusa
from math import sqrt
ca = float(input('digite cateto adjacente: '))
co = float(input('digite cateto oposto: '))
hip = sqrt(ca**2 + co**2)
print('valor da hip vale: {:.2f}'.format(hip))
