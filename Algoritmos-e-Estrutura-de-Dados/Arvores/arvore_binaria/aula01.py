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
        if pai == self.raiz:
            if self.esq is None:    
                self.esq = Arvore()
                self.esq.adicionar_raiz(dado)
                return True
            return False
        if self.esq is not None:
            if self.esq.adicionar_esq(pai, dado):
                return True
        if self.dir is not None:
            if self.dir.adicionar_esq(pai, dado):
                return True
        return False
    
    def adicionar_dir(self, pai, dado):
        if self.vazia():
            return False
        if pai == self.raiz:
            if self.dir is None:
                self.dir = Arvore()
                self.dir.adicionar_raiz(dado)
                return True
            return False
        if self.esq is not None:
            if self.esq.adicionar_dir(pai, dado):
                return True
        if self.dir is not None:
            if self.dir.adicionar_dir(pai, dado):
                return True
        return False 
    
    def imprimir(self, nivel=0):
        if self.vazia():
            print("ÁRvore Vazia")
            return
        print(" -" * nivel + str(self.raiz))
        if self.esq is not None:
            self.esq.imprimir(nivel+1)
        elif self.dir is not None:                    
            print(' -'*(nivel+1) + '*')
        if  self.dir is not None:
            self.dir.imprimir(nivel+1)
        elif self.esq is not None:
            print(' -'*(nivel+1) + '*')
    def pre_ordem(self):
        if self.vazia():
            return 
        print(self.raiz, end=' ')
        if self.esq is not None:
            self.esq.pre_ordem()
        if self.dir is not None:
            self.dir.pre_ordem()
    def em_ordem(self):
        if self.vazia():
            return
        if self.esq is not None:
            self.esq.em_ordem()
        print(self.raiz, end=' ')
        if self.dir is not None:
            self.dir.em_ordem()
    def pos_ordem(self):
        if self.vazia():
            return 
        if self.esq is not None:
            self.esq.pos_ordem()
        if self.dir is not None:
            self.dir.pos_ordem()
        print(self.raiz, end=' ')

    def em_nivel(self):
        if self.vazia():
            return
        fila = [self]
        while fila:
            arvore = fila.pop(0)
            print(arvore.raiz,end=' ')
            if arvore.esq is not None:
                fila.append(arvore.esq)
            if arvore.dir is not None:
                fila.append(arvore.dir)

a = Arvore()
a.adicionar_raiz('A')
a.adicionar_esq('A', 'B')
a.adicionar_dir('A', 'C')
a.adicionar_esq('B', 'D')
a.adicionar_dir('B', 'E')
a.adicionar_dir('C', 'F')
a.imprimir()