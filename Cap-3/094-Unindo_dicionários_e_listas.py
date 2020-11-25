dados = dict()
dadoslist = list()
mulheres = list()
idade = 0
while True:
    nome = str(input('Nome: '))
    dados['nome'] = nome
    sexo = str(input('Sexo: [M/F] ')).lower()
    dados['sexo'] = sexo
    if sexo == 'f':
        mulheres.append(nome)
    idade += int(input('Idade: '))
    dados['idade'] = idade
    dadoslist.append(dados.copy())
    p = str(input('Continuar? [S/N] ')).lower().strip()
    if p == 'n':
        break
mediadeidade = idade/len(dadoslist)
print('=*' * 15)
print(f'{"Resultado!":^30}')
print('=*' *15)
print(f'\n{len(dadoslist)} pessoas foram cadastradas.')
print(f'A idade média foi de {mediadeidade:.1f}.')
print(f'As seguintes pessoas foram mulheres: {mulheres}')
print('As pessoas com idade acima da média são: ')
for p in dadoslist:
    if p['idade'] >= mediadeidade:
        print(f'{p["nome"]}',end=', ')
        break