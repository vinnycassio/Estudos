
n = str(input('Qual o seu nome?')).strip()
print('Analisando seu nome...')
print('Seu nome em maíusculas é{}'.format(n.upper()))
print('Seu nome em minusculas é{}'.format(n.lower()))
print('Seu nome tem ao todo {} letras'.format(len(n)-n.count(' ')))
print('Seu primeiro nome é {} letras'.format(n.find(' ')))

separa = n.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))