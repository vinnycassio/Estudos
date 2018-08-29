distancia = int(input('Qual a distância da sua viagem?'))
limite = int(200)
if distancia <= limite:
    print('A sua tarifa de viagem será de R$ {:.2f}'.format(distancia*0.5))
else:
    print('A sua tarifa de viagem será de R$ {:.2f}'.format(distancia*0.45))
