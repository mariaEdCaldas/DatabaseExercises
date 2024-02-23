import sqlite3

def conectar_banco():
    conn = sqlite3.connect('banco.db')
    return conn

# 1. Crie uma tabela chamada "alunos" com os seguintes campos: id
#(inteiro), nome (texto), idade (inteiro) e curso (texto).
def criar_tabela_alunos(conn):
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS alunos ( id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER, curso TEXT)')
    conn.commit()

# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no
#exercício anterior.
def inserir_alunos(conn, registros):
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO alunos (nome, idade, curso) VALUES (?, ?, ?)', registros)
    conn.commit()

# 3. Consultas Básicas
def consultar(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def executar_atualizacao(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

def remover_registro(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

conn = conectar_banco()
criar_tabela_alunos(conn)

registros_alunos = [
    ('Marcos', 21, 'Cozinheiro'),
    ('João', 19, 'Medicina'),
    ('José', 29, 'Ciências'),
    ('Lígia', 27, 'Engenharia'),
    ('Roberto', 40, 'Professor')
]
inserir_alunos(conn, registros_alunos)

# 3. Consultas Básicas
# a) Selecionar todos os registros da tabela "alunos"
resultado_a = consultar(conn, 'SELECT * FROM alunos')
print("a) Todos os registros da tabela 'alunos':", resultado_a)

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos
resultado_b = consultar(conn, 'SELECT nome, idade FROM alunos WHERE idade > 20')
print("b) Nome e idade dos alunos com mais de 20 anos:", resultado_b)

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética
resultado_c = consultar(conn, 'SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome')
print("c) Alunos do curso de 'Engenharia' em ordem alfabética:", resultado_c)

# d) Contar o número total de alunos na tabela
resultado_d = consultar(conn, 'SELECT COUNT(*) FROM alunos')
print("d) Número total de alunos na tabela:", resultado_d[0][0])

# 4. Atualização e Remoção
# a) Atualizar a idade de um aluno específico na tabela
executar_atualizacao(conn, 'UPDATE alunos SET idade = 23 WHERE nome = "João"')

# b) Remover um aluno pelo seu ID (por exemplo, ID = 3)
remover_registro(conn, 'DELETE FROM alunos WHERE id = 3')

# Fechar a conexão com o banco de dados
conn.close()

#5. Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave
#primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns
#registros de clientes na tabela.

def criar_tabela_clientes(conn):
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER, saldo REAL)')
    conn.commit()

def inserir_clientes(conn, registros):
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO clientes (nome, idade, saldo) VALUES (?, ?, ?)', registros)
    conn.commit()
    
criar_tabela_clientes(conn)
registros_clientes = [
    ('Cliente1', 35, 1500.50),
    ('Cliente2', 28, 2000.75),
    ('Cliente3', 40, 300.00),
    ('Cliente4', 45, 5000.00),
    ('Cliente5', 50, 10000.25)
]
inserir_clientes(conn, registros_clientes)


#6. Consultas e Funções Agregadas
#Escreva consultas SQL para realizar as seguintes tarefas:

# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
resultado_a = consultar(conn, 'SELECT nome, idade FROM clientes WHERE idade > 30')
print("a) Nome e idade dos clientes com mais de 30 anos:", resultado_a)

# b) Calcule o saldo médio dos clientes.
resultado_b = consultar(conn, 'SELECT AVG(saldo) FROM clientes')
print("b) Saldo médio dos clientes:", resultado_b[0][0])

# c) Encontre o cliente com o saldo máximo.
resultado_c = consultar(conn, 'SELECT * FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)')
print("c) Cliente com o saldo máximo:", resultado_c[0])

# d) Conte quantos clientes têm saldo acima de 1000.
resultado_d = consultar(conn, 'SELECT COUNT(*) FROM clientes WHERE saldo > 1000')
print("d) Número de clientes com saldo acima de 1000:", resultado_d[0][0])

# 7. Atualização e Remoção com Condições

#a) Atualize o saldo de um cliente específico.
executar_atualizacao(conn, 'UPDATE clientes SET saldo = 2000.00 WHERE nome = "Cliente1"')

# b) Remova um cliente pelo seu ID.
remover_registro(conn, 'DELETE FROM clientes WHERE id = 3')


#8. Junção de Tabelas

#Crie uma segunda tabela chamada "compras" com os campos: id
#(chave primária), cliente_id (chave estrangeira referenciando o id
#da tabela "clientes"), produto (texto) e valor (real). Insira algumas
#compras associadas a clientes existentes na tabela "clientes".
#Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
def criar_tabela_compras(conn):
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS compras (id INTEGER PRIMARY KEY,cliente_id INTEGER,produto TEXT, valor REAL, FOREIGN KEY(cliente_id) REFERENCES clientes(id))')
    conn.commit()

def inserir_compras(conn, registros):
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO compras (cliente_id, produto, valor) VALUES (?, ?, ?)', registros)
    conn.commit()

criar_tabela_compras(conn)
registros_compras = [
    (1, 'Produto1', 150.00),
    (2, 'Produto2', 20.00),
    (3, 'Produto3', 50.00),
    (4, 'Produto4', 190.00),
    (5, 'Produto5', 75.00)
]
inserir_compras(conn, registros_compras)

resultado_juncao = consultar(conn, 'SELECT c.nome, p.produto, p.valor FROM clientes c JOIN compras p ON c.id = p.cliente_id')
print("Clientes e suas compras:")
for linha in resultado_juncao:
    print(linha)
