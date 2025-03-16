from fila_base import FilaBase
from constantes import CODIGO_PRIORITARIO

class FilaPrioritaria(FilaBase):   
    def gera_senha_atual(self):
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)

    def chama_cliente(self,caixa:int) -> str:
        cliente_atual:str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return(f'Cliente atual: {cliente_atual}, dirija-se ao caixa {caixa}')
    
    def estatistica(self, dia:str, agencia: int, retorna_estatistica) -> dict:
        estatistica = retorna_estatistica(dia, agencia)
        return estatistica.roda_estatistica(self.clientes_atendidos)
    
