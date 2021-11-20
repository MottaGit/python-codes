# le angulo, mostra sen, cos e tan
from math import sin, cos, tan, radians
ang = float(input('digite um angulo: '))
s = sin(radians(ang))
c = cos(radians(ang))
t = tan(radians(ang))
print('seno vale: {:.3f} cosseno vale: {:.3f} tangente vale: {}'.format(s, c, t))
