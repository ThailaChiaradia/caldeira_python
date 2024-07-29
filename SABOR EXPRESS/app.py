import os #biblioteca

restaurantes = [{'nome': 'TOKIOMAKI', 'categoria': 'Joponesa', 'ativo': False},
                {'nome': 'Buguer King', 'categoria': 'Fast Food', 'ativo': True},                
                {'nome': 'Vakirias Pizza', 'categoria': 'Pizzaria', 'ativo': False}
               ]

def exibir_nome_programa():
        
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░

    """)

def exibir_opcoes():
    print('1 - Cadastrar restaurante')
    print('2 - Listar restaurante')
    print('3 - Alterar status do restaurante')
    print('4 - Sair')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('\nEscolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def cadastrar_restaurante():    
    '''Essa função é responsável por cadastrar um novo restaurante
    Inputs: 
    - Nome restaurante
    - categoria

    Output:
    -Adiciona um novo restaurante  a uma nova lista de restaurantes
    '''
    exibir_subtitulo('CADASTRAR RESTAURANTE')
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria = input('Digite a categoria do restaurante: ')
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'\n--- O RESTAURANTE {nome_restaurante} FOI CADASTRADO COM SUCESSO ---')
    voltar_menu_principal()

def listar_restaurantes():
    '''Essa função é responsável por listar os restaurantes cadastrados'''
    exibir_subtitulo('LISTA DE RESTAURANTES CADASTRADOS')  

    print(f'{'NOME RESTAURANTE'.ljust(23)} | {'CATEGORIA'.ljust(20)} | {'STATUS'}')  
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'-> {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_menu_principal()

def alterar_status_restaurante():
    '''Essa função é responsável por ativar ou desativar o restaurante selecionado'''
    exibir_subtitulo('ALTERAL STATUS RESTAURANTE')

    nome_restaurante = input('\nDgitie o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurente {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_menu_principal()        

def finalizar_app():
   exibir_subtitulo('ENCERRANDO O PROGRAMA')

def opcao_invalida():
    print('Opção invalida\n')
    voltar_menu_principal()

def voltar_menu_principal():
    input('\nDgite uma tecla para voltar ao menu principal: ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
