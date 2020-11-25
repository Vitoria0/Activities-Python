from math import sqrt
print('Calculando a Hipotenusa \n')
co = float(input('Insira o valor do cateto oposto: '))
ca = float(input('Insira o valor do cateto adjacente: '))

hi = (co ** 2) + (ca ** 2)

hi = sqrt(hi)
print('A hipotenusa desse triângulo é: {:.2f}'.format(hi))