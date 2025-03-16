import abc
from constantes import TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIMO
from typing import List

class FilaBase(metaclass = abc.ABCMeta):
    codigo:int = 0
    fila : List[str] = []
    clientes_atendidos : List[str] = []
    senha_atual:str = ''

    def reseta_fila(self)->None:
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += 1

    def inseri_cliente(self):
        self.fila.append(self.senha_atual)

    @abc.abstractmethod
    def gera_senha_atual(self):
        ...
    
    @abc.abstractmethod
    def atualiza_fila(self):
        self.reseta_fila()
        self.gera_senha_atual()
        self.inseri_cliente()

    @abc.abstractmethod
    def chama_cliente(self, caixa : int):
        cliente_atual:str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return(f'Cliente atual: {cliente_atual}, dirija-se ao caixa {caixa}')