import requests
from acesso_cep import BuscaEndereco

cep = '01226001'
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)

'''r = requests.get('https://viacep.com.br/ws/01001000/json/')
print(r.text)'''

bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf)

'''from datas_br import DatasBr
from datetime import datetime, timedelta

hoje = DatasBr()
print(hoje.tempo_cadastro())
cadastro = DatasBr()
print(cadastro)

hoje = datetime.today()
hoje_formatada = hoje.strftime("%d/%m/%Y %H:%M")
print(hoje)
print(hoje_formatada)'''

'''from telefones_br import TelefonesBr
import re

telefone = '5511977200042'
telefone1 = TelefonesBr(telefone)

print(telefone1) '''

'''from validate_docbr import CPF
from cpf_cnpj import Documento
from validate_docbr import CNPJ


cpf_exemplo= '34679423005'
#print(cpf)

cnpj_exemplo = '80274546000170'
#cnpj = CNPJ()
#print(cnpj.validate(cnpj_exemplo))

documento = Documento.cria_documento(cnpj_exemplo)
print(documento)

documento2 = Documento.cria_documento(cpf_exemplo)
print(documento2) '''