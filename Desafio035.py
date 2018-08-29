s1 = int(input('Digite o segmento 1:'))
s2 = int(input('Digite o segmento 2:'))
s3 = int(input('Digite o segmento 3:'))

if s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2:
    print('Sim, esses segmentos formam um triangulo!')
else:
    print('Não, esses segmentos não formam um triangulo!')