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

    def buscar(self, diretorio):
        if self.vazia():
            return False
        if diretorio == self.raiz:
            return True
        for filho in self.filhos:
            if filho.buscar(diretorio):
                return True
        return False
    def remover(self, diretorio):
        if self.vazia():
            return False
        if diretorio == self.raiz:
            self.filhos.clear()
            self.raiz = None
            return True
        for filho in self.filhos:
            if diretorio == filho.raiz:
                self.filhos.remove(filho)
                return True
            if filho.remover(diretorio):
                return True
        return False

arvore = Arvore()

arvore.adicionar_raiz("Documentos")
arvore.adicionar_filho("Documentos", "Pessoal")
arvore.adicionar_filho("Documentos", "Trabalho")
arvore.adicionar_filho("Documentos", "Faculdade")
arvore.adicionar_filho("Pessoal", "Fotos")
arvore.adicionar_filho("Pessoal", "Viajens")
arvore.adicionar_filho("Trabalho", "Projetos")
arvore.adicionar_filho("Trabalho", "Relatórios")
arvore.adicionar_filho("Trabalho", "Reuniões")
arvore.adicionar_filho("Faculdade", "Aulas")
arvore.adicionar_filho("Faculdade", "Provas")
arvore.imprimir()
print(arvore.buscar("Vídeos"))
print(arvore.buscar("Projetos"))

arvore.remover("Trabalho")
arvore.imprimir()