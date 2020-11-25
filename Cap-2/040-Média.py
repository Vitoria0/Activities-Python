n1 = float(input('Primeira nota: '))
n2 = float(input('Seguunda nota: '))
m = (n1 + n2) /2
print('\033[36mTirando {:.1f} e {:.1f} a média do aluno é {}'.format(n1, n2, m))
if 7 > m >= 5:
    print('\033[33mO aluno está em recuperação')
elif m < 5:
    print('\033[31mO aluno está reprovado!')
else:
    print('\033[35mO aluno foi aprovado!')