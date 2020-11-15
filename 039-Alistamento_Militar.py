from datetime import date
a = date.today().year
n = int(input('Ano de nascimento: '))
i = a - n
print('Quem nasceu em {} tem {} anos em {}.'.format(n, i, a))
if i == 18:
    print('Você precisa se alistar IMEDIATAMENTE!')
elif i < 18:
    s = 18 - i
    ano = a + s
    print('Você ainda não tem 18 anos. Faltam {} anos para o alistamento.'.format(s))
    print('Seu alistamento será em {}'.format(ano))
elif i > 18:
    s = i - 18
    ano = a - s
    print('Você já deveria ter se alistado há {} anos.'.format(s))
    print('Seu alistamento foi em {}'.format(ano))