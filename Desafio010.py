n1 = str(input('Qual o seu nome?'))
v1 = float(input('Qual valor em reais você tem em sua carteira?'))
d = float(3.27)
d1 = float (v1/d)

print('Olá{} tudo bem? Você tem ${:.2f} Dolares!'.format(n1,d1))


