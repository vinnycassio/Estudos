import random
n1 = int(0)
n2 = int(1)
n3 = int(2)
n4 = int(3)
n5 = int(4)
n6 = int(5)
lista = [n1,n2,n3,n4,n5]
n = random.choice(lista)
n0 = int(input('Qual número o computador escolheu?'))
if n0 == n:
    print('Você acertou, PARABÉNS!')
else:
    print("Você perdeu, o número escolhido foi {}!".format(n))