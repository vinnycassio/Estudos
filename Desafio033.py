a = int(input('Digite o primeiro valor:'))
b = int(input('Digite o segundo valor:'))
c = int(input('Digite o terceiro valor'))

# VERIFICANDO O MENOR
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# VERIFICANDO O MAIOR
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O valor menor é {} e valor maoir é {}!'.format(menor, maior))
