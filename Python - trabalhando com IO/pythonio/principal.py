import sys
sys.path.append('C:\dev\workspace\Alura\Python - trabalhando com IO\pythonio')
import contatos_utils

try:
    #contatos = contatos_utils.csv_para_contatos('dados/contatos.csv')
    #contatos = contatos_utils.contatos_para_pickle(contatos, 'dados/contatos.p')
    #contatos = contatos_utils.pickle_para_contatos('dados/contatos.pickle')
    #contatos = contatos_utils.contatos_para_json(contatos, 'dados/contatos.json')

    contatos = contatos_utils.json_para_contatos('dados/contatos.json')

    for contato in contatos:
        print(f'{contato.id} - {contato.nome} - {contato.email}')
except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão de escrita')
