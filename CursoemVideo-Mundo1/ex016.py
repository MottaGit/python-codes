#le numero real, exibe apenas parte inteira
import math
num = float(input('digite um numero real: '))
intnum = math.trunc(num)
print('o numero {} tem a parte inteira {}'.format(num,intnum))
