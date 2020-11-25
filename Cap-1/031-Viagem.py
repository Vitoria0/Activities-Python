d = float(input('Qual a distancia da sua viagem? '))
print('Você está prestes a fazer uma viagem de {}Km'.format(d))
if d <= 200:
    p = d * 0.50
else:
    p = d * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(p))