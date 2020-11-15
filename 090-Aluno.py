aluno = {}
aluno['nome'] = str(input('Nome do aluno: '))
aluno['nota'] = float(input('Nota do aluno: '))
print(f'O nome do aluno é {aluno["nome"]}')
print(f'Sua média é {aluno["nota"]}')
if aluno['nota'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['nota'] < 7:
    aluno['situação'] = 'Em recuperação'
else:
    aluno['situação'] = 'Reprovado'
print(f'O aluno está {aluno["situação"]}')