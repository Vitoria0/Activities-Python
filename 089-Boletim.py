alunos = []
al = []

while True:

    al.append(str(input('Nome: ')).strip())
    al.append(float(input('Nota 1: ')))
    al.append(float(input('Nota 2: ')))

    alunos.append(al[:])
    al.clear()

    while True:

        resp = str(input('Deseja continuar? (S/N): ')).strip().upper()[0]

        if resp in 'SN':
            break

    if resp == 'N':
        break

print('\n')
print(f'{"Nº":<10} {"NOME":<30} {"MÉDIA":^10}')
print('-'*50)

for p, aluno in enumerate(alunos):
    print(f'{p:<10} {aluno[0]:<30} {((aluno[1] + aluno[2]) / 2):^10.2f}')

print()

while True:

    m = int(input('Mostrar notas de qual aluno? (999 - Finalizar): '))

    if m == 999:

        print()
        print('PROGRAMA FINALIZADO!')
        break

    else:

        print(f'As notas de {alunos[m][0]} são {alunos[m][1:]}')
        print()


