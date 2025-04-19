from tabela import escolha
from rota import linhas
from time import sleep
from tabulate import tabulate

linhas()
print('Coloque suas informações')
sleep(1)

nome = input('Nome : ')
idade = int(input('Idade :'))
profissao = input('Profissão :')

print('''Quer colocar seu salário ? : R$
	  [ 1 ] SIM
	  [ 2 ] NÃO''')
opcao = int(input('Escolha :'))

if opcao == 1:
	salario = f"R$ {float(input('R$ ')):.2f}"
else:
	print('Opção não registrada')
	salario = 'Não informado'

sleep(1)
print('Registro adicionado')
print('--------------------')

dados = [
	['Cliente ', nome],
	['Idade ', f'{idade} anos'],
	['Profissão ', profissao],
	['Salário ', salario]
]

print(tabulate(dados, tablefmt='grid'))
linhas()
