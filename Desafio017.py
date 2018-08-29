import math
c1 = float(input('Digite o cateto 01:'))
c2 = float(input('Digite o cateto 02:'))
h = math.hypot(c1,c2)

print('A hipotenusa dos catetos {} e {} é igual a {}'.format(c1,c2,h))