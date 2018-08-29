velocidade = float(input('Qual foi a velocicade do carro?'))
limite = float(80)
if velocidade > limite:
    print('Você ultrapassou o limite de velociade e será multado no valor de R$ {:.2f}!'.format((velocidade-limite)*7.00))
