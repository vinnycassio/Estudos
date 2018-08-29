s = float(input('Qual o salário atual do funcionário?'))
a = float(input('Qual o aumento aplicado?'))
sf = float(s+(s*(a/100)))

print('O salário ajustado é de R${}'. format(sf))