from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
print('O atleta tem {} anos.'.format(idade))
c = 'Mirim'
if idade > 9:
    c= 'Infantil'
if idade > 14:
    c = 'Junior'
if idade > 19:
    c = 'Sênior'
if idade > 25:
    c = 'Master'
print('Classificação: {}'.format(c))