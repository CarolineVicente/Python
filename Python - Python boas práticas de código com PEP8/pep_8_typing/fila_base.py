import abc

class FilaBase(metaclass = abc.ABCMeta):
    codigo:int = 0
    fila = []
    clientes_atendidos = []
    senha_atual:str = ''

    def reseta_fila(self)->None:
        if self.codigo >= 200:
            self.codigo = 0
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