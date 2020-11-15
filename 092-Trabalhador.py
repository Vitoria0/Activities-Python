dados = dict()
dados['nome'] = str(input('Nome: '))
dados['idade'] = 2020 - int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados["ctps"] <= 0:
    print('-='*30)
    print(f'nome tem o valor {dados["nome"]}')
    print(f'idade tem o valor {dados["idade"]}')
    print(f'ctps tem o valor {dados["ctps"]}')
else:
    dados['contrataçao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = 35 - (2020 - dados['contrataçao']) + dados['idade']
    print('-' * 40)
    print(f'nome tem o valor {dados["nome"]}')
    print(f'idade tem o valor {dados["idade"]}')
    print(f'ctps tem o valor {dados["ctps"]}')
    print(f'contratação tem o valor {dados["contrataçao"]}')
    print(f'aposentadoria tem o valor {dados["aposentadoria"]}')