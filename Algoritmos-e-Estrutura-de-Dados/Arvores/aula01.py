class Arvore:
    def __init__(self):
        self.raiz = None;
        self.filhos = [];
    def vazia(self):
        return self.raiz == None
    def adicionar_raiz(self, dado):
        if not self.vazia():
            return False
        self.raiz = dado
        return True
    def adicionar_filho(self, pai, dado):
        if self.vazia():
            return False
        if pai == self.raiz:
            filho = Arvore()
            filho.adicionar_raiz(dado)
            self.filhos.append(filho)
            return True
        for filho in self.filhos:
            if filho.adicionar_filho(pai, dado):
                return True
        return False
    def imprimir(self, nivel=0):
        if self.vazia():
            print("ÁRvore Vazia")
            return False
        print('-' *nivel+str(self.raiz))
        for filho in self.filhos:
            filho.imprimir(nivel+1)
            
    def percorrer(self):
        if self.vazia():
            return 
        print(self.raiz, end=' ')
        for filho in self.filhos:
            filho.percorrer()

# arvore = Arvore()
# arvore.adicionar_raiz('A')
# arvore.adicionar_filho('A','B')
# arvore.adicionar_filho('A','C')
# arvore.adicionar_filho('A','D')
# arvore.imprimir()
# arvore.adicionar_filho('B','E')
# arvore.adicionar_filho('B','F')
# arvore.adicionar_filho('D','G')
# arvore.adicionar_filho('D','H')
# arvore.adicionar_filho('D','I')
# arvore.imprimir()
# arvore.percorrer()