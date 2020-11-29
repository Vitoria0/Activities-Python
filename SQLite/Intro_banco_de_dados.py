#SQLite3 é um banco de dados que já vem no Python
#Importar
import sqlite3

#Criar um banco, caso  não exista
conn = sqlite3.connect('clientes.db') #  .db = data base

#Para fazer Operações precisa do cursor
cursor = conn.cursor()

#Criando a Tabela
cursor.execute("""
CREATE TABLE clientes (
           id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
           nome TEXT NOT NULL,
           idade INTERGER,
           cpf VARCHAR(14) NOT NULL,
           email TEXT NOT NULL,
           celular INTERGER NOT NULL,
           cidade TEXT NOT NULL,
           estado TEXT NOT NULL,
           genero TEXT
);
""")


#Print só p dizer que ta tudo certo
print('Tabela criada com sucesso!')

#Fecha a conexão
conn.close()