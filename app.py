import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiana', 'ativo':False}]

def exibir_nome_do_programa():
    '''Utilizada para mostrar o nome do programa, logo antes das opções do menu principal.'''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    '''Função usada apenas para mostrar as opções do menu principal.'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar/desativar restaurante')
    print('4. Sair\n')

def encerrar_app():
    '''Essa função é apenas para encerrar as atividades do aplicativo.'''
    exibir_subtitulo('Encerrando o App...')

def voltar_ao_menu_principal():
    '''Utilizada para voltar ao menu principal pressionando qualquer tecla.
    
    Outputs:
    - Retorna ao menu principal
    '''
    input('\nDigite uma tecla para voltar ao menu. ')
    main()

def opcao_invalida():
    '''Utilizada pra quando o usuário digita alguma opção/número que não está do menu.
    
    Outputs:
    - Retorna ao menu principal
    '''
    print('Opção inválida!\n')

    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Exibe um subtitulo estilizado em todas as opções selecionadas.
    
    Inputs:
    - texto: str - o texto do subtitulo
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Função utilizada para cadastrar novos restaurantes.

    Inputs:
    - Nome do restaurante
    - Categoria do restaurante

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo('CADASTRO DE RESTAURANTE')

    nome_do_restaurante = input('Digite o nome do resturante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')

    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria_do_restaurante, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Lista todos os restaurantes e dá a opção de voltar ao menu após isso.
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    - Retorna ao menu principal
    '''
    exibir_subtitulo('RESTAURANTES CADASTRADOS')

    print(f'{'Nome dos restaurantes'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante.ljust(20)}')

    voltar_ao_menu_principal()

def alterar_estado_restaurante():
    '''Altera o estado do restaurante de 'True' para 'False', ou vice-versa.
    
    Inputs:
    - Nome do restaurante (que quer encontrar)

    Outputs:
    - Exibe a mensagem indicando sucesso da operação
    - Retorna ao menu principal
    '''
    exibir_subtitulo('ATIVAÇÃO/DESATIVAÇÃO DE RESTAURANTE')

    nome_restaurante = input('Digite o nome do Restaurante que deseja ativar/desativar: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)

    if restaurante_encontrado == False:
        print('Restaunte não encontrado.')

    voltar_ao_menu_principal()


def escolher_opcoes():
    '''Menu de escolha das opções.
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:         
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_estado_restaurante()
        elif opcao_escolhida == 4:
            encerrar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Função que inicia o programa.'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()