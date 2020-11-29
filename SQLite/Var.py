def variaveis():
    var = [(
        input('Nome: '),
        int(input('Idade: ')),
        tratamento_cpf(input('CPF: ')),
        input('E-mail: '),
        int(input('Celular: ')),
        input('Cidade: '),
        input('Estado: '),
        input('Gênero: ')
    )]
    return var

def linha(msg=' '):
    print('-' * 35)
    print(f"{msg:^35}")
    print('-' * 35)
    print("1- Cadastrar Pessoa ")
    print('2- Ver Pessoas Cadastradas')
    print('3- Deletar Pessoa')
    print('4- Atualizar Dados')
    print('5- Adcionar nova coluna')
    print('6- Ver pessoas maiores de idade')
    print('7- Ver pessoas de Blumenau')
    print('8- Chamada')
    print('9- Sair')
    print('-' * 35)

    return

def tratamento_cpf(cpf):
    if len(cpf) != 11:
        raise AttributeError('CPF Inválido')
    else:
        try:
            int(cpf)
        except ValueError:
            raise AttributeError('CPF Inválido')
        return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'

def esse_id_existe(cursor, id_cliente):
    while True:
        var = (str(id_cliente))
        cursor.execute(f'SELECT id FROM clientes WHERE id = {var}')
        if cursor.fetchall() == []:
            id_cliente = input('Esse id não existe, informe um id válido: ')

        else:
            return id_cliente