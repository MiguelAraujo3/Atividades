class _No:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None

class ABB:
    def __init__(self):
        self.__raiz = None

    def vazia(self):
        return self.__raiz == None

    def buscar(self, dado):
        atual = self.__raiz
        while atual is not None:
            if atual.dado == dado:
                return True
            if valor > atual.dado:
                atual = atual.dir
            else: 
                atual = atual.esq
        return False
    
    def inserir(self,dado):
        atual = self.__raiz
        anterior = None
        while atual is not None:
            if atual.dado == dado:
                return False
            if valor > atual.dado:
                anterior = atual
                atual = atual.dir
            else: 
                anterior = atual
                atual = atual.esq
        if anterior.dado > dado:
            anterior.esq = _No(dado)
        else:
            anterior.dir = _No(dado)
            