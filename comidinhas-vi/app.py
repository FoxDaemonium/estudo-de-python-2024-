import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                    {'nome':'Pizzando', 'categoria':'Pizza', 'ativo':True},
                    {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_titulos(texto):
    '''Função que limpa o menu e exibe os titulos das categorias selecionadas
    input: -texto personalizado para cada categoria
    -quantidade de * com base no numero de caractere do texto 
    output:
    texto personalizado
    '''
    os.system('cls')
    linha= '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_menu():
    '''função de voltar ao menu principal do aplicativo'''
    input ('\nDigite uma tecla para voltar ao menu principal.')
    main()

def nome_app():
    '''função de exibição do nome do aplicativo'''
    print("""

    █▀▀ █▀█ █▀▄▀█ █ █▀▄ █ █▄░█ █░█ ▄▀█ █▀   █░█ █
    █▄▄ █▄█ █░▀░█ █ █▄▀ █ █░▀█ █▀█ █▀█ ▄█   ▀▄▀ █
        
    """)

def opcoes_de_escolha():
    '''função que mostra as opções de escolha do aplicativo
    output: ass categorias são mostradas em forma de texto na tela'''
    print('1, cadastrar restaurante')
    print('2, listar restaurante')
    print('3, alterar status do restaurante')
    print('4, sair\n')

# dentro do escolhido

def fechar():
    '''funçao que finaliza o aplicativo'''
    exibir_titulos('fechando app')

def invalida():
    '''função que mostra uma escolha ou palavra invalida'''
    print('opção invalida!\n')
    voltar_menu()

def cadas_rest():
    '''
    função que faz o cadastro de novos restaurantes no aplicativo
    input:
    -nome do restaurante
    -categorias
    output:
    -adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_titulos('cadastro de novos restaurantes')
    nome_rest = input('Digite o nome do restaurante que deseja cadastrar:')
    categoria= input(f'Digite a categoria do restaurante {nome_rest}:')
    dados_rest={'nome':nome_rest, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_rest)
    print(f'O restaurante {nome_rest} foi cadastrado com sucesso!')
    voltar_menu()

def listar_res():
    '''função que lista todos os restaurantes existentes no aplicativo
    procura todos os restaurantes com o loop e os mostra na tela'''
    exibir_titulos('listando restaurantes')
    print(f'{'nome do restaurante'.ljust(22)} | {'categoria'.ljust(20)} | status do restaurante\n')
    for restaurante in restaurantes:
        nome_rest = restaurante['nome' ]
        categoria = restaurante['categoria' ]
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_rest.ljust(20)} | {categoria.ljust(20)} | {ativo}')
        
    voltar_menu()

def alternar_status():
    '''função que muda o status do restaurante para ativado ou desativado
    input:
    -nome do restaurante
    output:
    -restaurante encontrado muda o status independente de qual seja
    -indica restaurante não encontrado
    '''
    exibir_titulos('mudar status para ativado ou desativado')
    nome_rest=input('qual nome do restaurante que deseja alterar o status?')
    rest_in_list=False

    for restaurante in restaurantes:
        if nome_rest ==restaurante['nome']:
            rest_in_list= True
            restaurante['ativo']= not restaurante['ativo']
            mensagem= f'o status do restaurante {nome_rest} esta ativado' if restaurante['ativo'] else f'o status do restaurante {nome_rest} esta desativado'
            print(mensagem)
    if not rest_in_list:
        print('O restaurante não foi encontrado')
    voltar_menu()

# dentro do escolhido

def escolhido():
    '''função que pede a escolha das categorias do aplicativo para o usuario
    input numero de escolha do usuario
    output direciona para tela da categoria desejada
    '''
    try:
        escolha = int(input('Escolha uma opcao:'))
        # escolha = int(escolha)

        if escolha == 1:
            cadas_rest()
        elif escolha == 2:
            listar_res()
        elif escolha == 3:
            alternar_status()
        elif escolha ==4:
            fechar()
        else:
            invalida()
    except:
        invalida

def main():
    '''função principal do aplicatiovo'''
    os.system('cls')
    nome_app()
    opcoes_de_escolha()
    escolhido()

if __name__ =='__main__':
    main()
