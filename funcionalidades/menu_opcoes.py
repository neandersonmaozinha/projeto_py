from datetime import datetime
from funcionalidades import finalizar
from funcionalidades import cadastro
import pandas as pd


def menu_principal ():
    print(datetime.now().strftime('%d/%m/%Y, %H:%M'))
    print('Menu Principal\n')

    print('1. Cadastrar cliente')
    print('2. Listar clientes')
    print('3. Sair\n')

    opcao_escolhida = int(input('Escolha uma opção: '))

    if opcao_escolhida == 1:
        cadastro.cadastrar_cliente()
    elif opcao_escolhida == 2:
        df = pd.read_csv('base_de_clientes.csv', encoding='utf8', sep=',')
        print(df)
    else: 
        finalizar.encerrar_app()
    