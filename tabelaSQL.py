import sqlite3

nome = input('Nome : ')
idade = int(input('Idade :'))
profissao = input('Profissão : ')

conn = sqlite3.connect('teste_de_banco.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    profissao TEXT NOT NULL
)
''')

cursor.execute('INSERT INTO CLIENTES (NOME,IDADE,PROFISSAO) VALUES (?,?,?)',(nome , idade ,profissao))

conn.commit()

cursor.execute('SELECT * FROM clientes')
dados = cursor.fetchall()

print("\n=== Lista de Clientes ===")
for cliente in dados:
    print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Idade: {cliente[2]} | Profissão: {cliente[3]}")
    
conn.close()