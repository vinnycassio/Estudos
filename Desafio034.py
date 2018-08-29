salario = float(input('Digite o salário:'))
a1 = 10
a2 = 15
if salario > 1250:
    print('O salário com aumento é de {}!'. format(salario + (salario * a1 / 100)))
else:
    print('O saláxlrio com aumento é de {}!'. format(salario + (salario * a2 / 100)))