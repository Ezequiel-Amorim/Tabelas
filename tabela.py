from rota import linhas

while True:
    linhas()
    print('''Gostaria de fazer parte dessa tabela de mês?
      [ 1 ] SIM
      [ 2 ] Não
    ''')
    escolha = int(input('Escolha : '))
    if escolha == 1:
        print('Ok, vamos continuar')
        break
    elif escolha == 2:
        print('Ok, obrigado pela sua opinião')
    
    elif escolha >2:
        print('Essa opção,não existe')
        