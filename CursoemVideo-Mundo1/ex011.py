# recebe largura e altura, calcula area
# quanta tinta para pintar, se 1L de tinta = 2m^2
h = float(input('altura: '))
l = float(input('largura: '))
area = h*l
tinta = area/2
print('para pintar a área de {}, precisa de {} litros de tinta'.format(area, tinta))
