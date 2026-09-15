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
            self.filhs.append(filho)
            return True
        for filho in filhos:
            if filho.adicionar_filho(pai, dado):
                return True
        return False
    def imprimmir(self, nivel=0):
        if self.vazia():
            print("ÁRvore Vazia")
            return False
        print('-' *nivel+str(self.raiz))
        for filho in filhos:
            filho.imprimir(nivel+1)
            
