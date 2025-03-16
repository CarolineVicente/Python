from typing import Union

from fila_normal import Filanormal
from fila_prioritaria import FilaPrioritaria
from constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA

class FabricaFila:
    def pega_fila(self, tipo_fila) -> Union[Filanormal,FilaPrioritaria]:
        if tipo_fila == TIPO_FILA_NORMAL:
            return Filanormal()
        elif tipo_fila == TIPO_FILA_PRIORITARIA:
            return FilaPrioritaria()
        else:
            raise NotImplementedError('Tipo de Fila Não Existe!!')