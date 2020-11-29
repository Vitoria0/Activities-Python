import sqlite3
from Var import variaveis
from Var import linha
from Var import esse_id_existe

#-------------------------Menu--------------------------------
while True:
    try:
        var = linha('MENU')

        valor = int(input('Digite a operação desejada: '))
        print('-' * 35)

#-----------------Cadastrar-Pessoa----------------------------
        if valor == 1:
            var = variaveis()
            print('-' * 35)
            print('Pessoa cadastrada com sucesso!')

            conn = sqlite3.connect('clientes.db')
            cursor = conn.cursor()

            #---Inserindo os valores
            cursor.executemany("""
            INSERT INTO clientes(nome, idade, cpf, email, celular, cidade, estado, genero)
            VALUES(?,?,?,?,?,?,?,?) 
            """, var)

            #---Grava no Banco de Dados
            conn.commit()

            conn.close()

#----------------------ler-dados------------------------------
        # ver se tem alguem cadastrado
        elif valor == 2:
            conn = sqlite3.connect('clientes.db')
            cursor = conn.cursor()

            # Seleciona os dados do banco de dados
            # SELECT * FROM para selecionar todos os dados
            cursor.execute("""
            SELECT id, nome FROM clientes;
            """)

            for dados in cursor.fetchall():
                print(*dados, sep=' - ')
                conn.close()
            print('-' * 35)
            print('1- Ver mais informações')
            print('2- Voltar')
            print('-' * 35)
            while True:
                try:
                    valor2 = int(input('Digite a operação desejada: '))

                    if valor2 == 1:
                        conn = sqlite3.connect('clientes.db')
                        cursor = conn.cursor()

                        while True:
                            #Pede um id
                            id_cliente = input('Informe o id que deseja ver: ')
                            var = (str(id_cliente))
                            cursor.execute(f'SELECT id FROM clientes WHERE id = {var}')
                            if cursor.fetchall() == []:
                                print('id inexistente!')

                            else:
                                print('-' * 35)

                                # Seleciona o id informado
                                cursor.execute(f"""
                                SELECT * FROM clientes
                                WHERE id = {id_cliente};
                                """)
                                # Printa o id informado

                                print(*cursor.fetchone(), sep='\n')
                                break
                        break

                    elif valor2 != 2:
                        print('Opção invalida! tente novamente')

                    elif valor == 2:
                        break

                except ValueError:
                    print('Valor invalido! tente novamente')


#-----------------------Deletar-Dados---------------------------
        # Ver se tem alguém cadastrado
        elif valor == 3:
            conn = sqlite3.connect('clientes.db')
            cursor = conn.cursor()
            print('')
            cursor.execute('SELECT * FROM clientes')
            if cursor.fetchall() == []:
                print('Ninguém foi cadastrado no momento')

            else:
                id_cliente = int(input('ID da pessoa que deseja deletar: '))

                esse_id_existe(cursor, id_cliente)
                cursor.execute("""
                DELETE FROM clientes
                WHERE id = ?
                """, (id_cliente,))

                conn.commit()
                print('Pessoa Excluida com sucesso!')

                conn.close()

#---------------------Atualizar-Dados--------------------------------------
        elif valor == 4:
            conn = sqlite3.connect('clientes.db')
            cursor = conn.cursor()

            # alterando os dados da tabela
            cursor.execute('SELECT * FROM clientes')
            if cursor.fetchall() == []:
                print('Ninguém foi cadastrado no momento')

            else:
                id_cliente = int(input('Digite o ID: '))

                esse_id_existe(cursor, id_cliente)
                novo = input('O que quer mudar: ')
                valor = input('Valor: ')
                var = [(valor, id_cliente)]

                cursor.executemany(f"""
                UPDATE clientes
                SET {novo} = ?
                WHERE id = ?
                """, var)

                conn.commit()

                print('Dados atualizados com sucesso.')
                conn.close()
                #Tem que retornar p menu

#---------------------------------Nova-Coluna----------------------------------
        elif valor == 5:
            conn = sqlite3.connect('clientes.db')
            cursor = conn.cursor()

            cursor.execute('SELECT * FROM clientes')
            if cursor.fetchall() == []:
                print('Ninguém foi cadastrado no momento')

            else:
                novo = input('Adcione o nome da nova coluna: ')
                tipo = input('Qual o tipo? [TEXT] [INTEGER] [VARCHAR( )]: ').upper()

                 # adicionando uma nova coluna na tabela clientes
                cursor.execute(f"""
                ALTER TABLE clientes
                ADD COLUMN {novo} {tipo};
                """)

                conn.commit()
                print('Novo campo adicionado com sucesso.')

                conn.close()

#----------------------------Maiores-de-Idade----------------------------------
        elif valor == 6:
            # Seleciona tudos que tem idade maior q 18
            conn = sqlite3.connect('clientes.db')
            cursor = conn.cursor()
            cursor.execute("""
            SELECT id, nome FROM clientes
            WHERE idade >= ?;
            """, (18,))

            # Printa int(*cursor.fetchall(), sep=' ')
            for i in cursor.fetchall():
                print(*i, sep='- ')

#----------------------------Pessoas-de-Blumenau--------------------------------
        elif valor == 7:
            conn = sqlite3.connect('clientes.db')
            cursor = conn.cursor()

            # Seleciona todo mundo que tem 'Belo' na coluna cidades
            cursor.execute("""
            SELECT id, nome FROM clientes
            WHERE cidade like '%Blumenau%';
            """)

            # Printa todo mundo que tem 'Belo' na coluna cidades
            for i in cursor.fetchall():
                print(*i, sep='- ')

            conn.close()

#---------------------------------Chamada---------------------------------------
        elif valor == 8:
            conn = sqlite3.connect('clientes.db')
            cursor = conn.cursor()
            # Seleciona todos mas ordenado pelo nome de forma decrescente
            cursor.execute("""
            SELECT id, nome FROM clientes ORDER BY nome ASC;
            """, )

            # Printa separado todos os valores
            for i in cursor.fetchall():
                print(*i, sep='- ')

            conn.close()

#-----------------------------------Sair---------------------------------------
        elif valor == 9:
            print('Obrigada volte sempre!')
            break

#----------------------Se-for um número que não tem ali--------------------------

        elif valor != 9:
            print('Opção inválida! Tente novamente')

#---------Tratando-erro

    except ValueError:
        print('Opção invalida! Tente novamente')

