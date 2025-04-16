from tabela import escolha
from rota import linhas
from time import sleep
linhas()
print('Coloque suas informações')
sleep(1)
nome = input('Nome : ')
idade = int(input('Idade :'))
profissao = input('Profissão :')
print('''Quer colocar seu salário ? : R$
	  [ 1 ] SIM
	  [ 2 ] NÃO''')
opçao = int(input('Escolha :'))
if opçao == 1:
	salario = float(input('R$ ')) 
else:
	print('Opção não registrada')
	salario = 'Não informado'

sleep(1)
print('Registro adicionado')
print('--------------------')
print(f'Cliente: {nome}\nIdade: {idade} anos\nProfissão: {profissao}\nSalário: R$ {salario}')
linhas()