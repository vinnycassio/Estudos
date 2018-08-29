l = float(input('Digite a largura da parede:'))
a = float(input('Digite a altura da parede:'))
a2 = float(l * a)
t = float(a2 / 2)

print('A quantidade de tinta necessário para pintar a parede é de:{} litro(s) para pintar {} metros quadrados de parede' .format(t,a2))
