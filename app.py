from datetime import datetime 

print(datetime.now().strftime('%d/%m/%Y, %H:%M'))
print('Menu Principal\n')

print('1. Cadastrar cliente')
print('2. Listar clientes')
print('3. Atualizar cliente')
print('4. Exlcuir cliente')
print('5. Sair\n')

opcao_escolhida = input('Digite uma opção: ')
print(f'você escolheu a opção: {opcao_escolhida}')

if opcao_escolhida == 1:
    print('Cadastrar cliente')
elif opcao_escolhida == 2:
    print('Listar clientes')
elif opcao_escolhida == 3:
    print('Atualizar cliente')
elif opcao_escolhida == 4:
    print('Atualizar cliente')
else:
    print('Finalizar programa')
