from datetime import datetime 

print(datetime.now().strftime('%d/%m/%Y, %H:%M'))
print('Menu Principal\n')

print('1. Cadastrar aluno')
print('2. Listar alunos')
print('3. Atualizar aluno')
print('4. Exlcuir alunos')
print('5. Sair\n')

opcao_escolhida = input('Digite uma opção: ')
print(f'você escolheu a opção: {opcao_escolhida}')