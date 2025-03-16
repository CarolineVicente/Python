import os

restaurantes = [{'nome': 'Praça', 'categoria' : 'Japonesa', 'ativo' : False},
                {'nome' : 'Pizza Suprema', 'categoria' : 'Italiana' , 'ativo' : True},
                {'nome' : 'Cantina', 'categoria' : 'Italiana' , 'ativo' : False}]

def exibir_nome_do_programa():
    print('Sabor Express\n')

def exibir_opcoes():
    print('1. Cadastrar Restaurantes')
    print('2. Listar Restaurantes')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def finalizar_app():
   exibir_subtitulo('Encerrando o programa')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal!')
    main()

def opcao_invalida():
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()


def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restautante = input('Coloque o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do {nome_do_restautante} :')
    dados_do_restaurante = {'nome': nome_do_restautante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restautante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')

    #print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'}'.ljust(20) | {'Status'}) 
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternar estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True  
            restaurante['ativo'] = not restaurante['ativo'] 
            mensagem = f'O restaurante foi {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante { nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()

def escolher_opcao():

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção: {opcao_escolhida}')
        #opcao_escolhida =  int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()



# print('Python na Escola de Programação da Alura')

# nome = input('Qual o sue nome?')
# idade = input ('Qual sua idade?')

# print(f'Meu nome é {nome} e tenho {idade} anos')