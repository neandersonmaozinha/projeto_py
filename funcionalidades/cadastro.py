
from csv import DictReader, DictWriter

def cadastrar_cliente ():
    contador = quantidade = 0
    arquivo = str(input('informe o nome do arquivo: ')).strip().lower()
    if arquivo [:-4] == '.csv':
        arquivo_nome = arquivo
    else:
        arquivo_nome = arquivo .replace(' ', '_')+ '.csv'
        



    

    try:
        with open(arquivo_nome) as documento:
            leitura = DictReader(documento)
            
            print('| NOME | IDADE | PROFISÃO | SALARIO' )
            
            for linha in leitura:
                print(f'| {linha['NOME']} | {linha['IDADE']} | {linha['PROFISÃO']}' | {linha['SALARIO']})
        parametro = 'a'    
    except FileNotFoundError:
        parametro = 'w'
        
    # CONDIÇÃO

    condicao = str(input('Inserir novo cadastro [S / N] ou não?  ')).strip().lower()

    print(condicao)
    if condicao == 's':
        quantidade = int(input('Quantos: '))

    #Criando ou alternando o arquivo

    with open(arquivo_nome, parametro, encoding='utf-8') as documento:
        cabecario = ['NOME', 'IDADE', 'PROFISSÃO', 'SALARIO']
        escrita = DictWriter(documento, fieldnames=cabecario)
        
        if parametro == 'w':
            escrita.writeheader()
        
        while contador < quantidade:
            for contador in range (quantidade):
                print('\n', '{:-^34}'.format(f'{contador+1}° Cliente'))
                
                nome = input ('Digite o NOME ou  para encerrar: ').title()
                    
                if nome != 'Sair':
                    idade = int(input('idade'))
                    profissao = str(input('Profisão: '))
                    salario = float(input('Salário: '))
                print('{:-^34}'.format('\033[32mCadastro incluido com sucesso[m'))    
                
                
                #populando os dados
                
                escrita.writerow(
                    {'NOME': nome, 
                    'IDADE': idade, 
                    'PROFISSÃO': profissao,
                    'SALARIO':salario
                    }
                )
                contador += 1
    print('{:-^34}'.format('\033[32mArquivo Salvo!!![m'))