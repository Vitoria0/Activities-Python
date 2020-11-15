s = float(input('Qual o salário do funcionário? R$'))
if s <= 1250:
    novo = s + (s * 15 / 100)
else:
    novo = s + (s * 10 / 100)
print('Quem ganhava R${} passa a ganhar R${} agora!'.format(s, novo))