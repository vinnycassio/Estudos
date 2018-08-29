p = float(input('Qual o preço do produto?'))
d = float(input('Qual o desconto aplicado?'))
pf = p - (p*(d/100))

print('O valor do produto com desconto é {}'.format(pf))