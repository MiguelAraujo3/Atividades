class Arvore:
    def __init__(self):
        self.raiz = None
        self.dir = None
        self.esq = None
    def vazia(self):
        return self.raiz == None
    def adicionar_raiz(self, dado):
        if not self.vazia():
            return False
        self.raiz = dado
        return True
    def adicionar_esq(self, pai, dado):
        if self.vazia():
            return False
        if pai == self.raiz and self.esq == None:
            self.esq = Arvore()
            self.esq.adicionar_raiz(dado)
            return True
        if pai == self.raiz and not self.esq == None:
            if self.esq.adicionar_esq(pai, dado):
                return True
        if pai == self.raiz and not self.dir == None:
            if self.dir.adicionar_esq(pai, dado):
                return True
        return False
    def adicionar_dir(self, pai, dado):
            if self.vazia():
                return False
            if pai == self.raiz and self.dir == None:
                self.dir = Arvore()
                self.dir.adicionar_raiz(dado)
                return True
            if pai == self.raiz and not self.esq == None:
                if self.esq.adicionar_esq(pai, dado):
                    return True
            if pai == self.raiz and not self.dir == None:
                if self.dir.adicionar_esq(pai, dado):
                    return True
            return False 
    def imprimir(self, nivel=0):
        if self.vazia():
            print("ÁRvore Vazia")
            return
        print("-" * nivel + str(self.raiz))
        if not self.esq == None:
            self.esq.imprimir(nivel+1)
        elif not self.dir.imprimir(nivel+1):
            print('-'*nivel)