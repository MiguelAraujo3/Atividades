class Pilha:
    def __init__(self):
        self.__itens = []
    def vazia(self):
        return self.__itens == []

    def empilhar(self, valor):
        self.__itens.append(valor)

    def desempilhar(self):
        if self.vazia():
            return None
        valor = self.__itens[-1]
        self.__itens.pop()
        return valor
    def topo(self):
        if self.vazia():
            return None
        return self.__itens[-1]
    
    def esvaziar(self):
        self.__itens.clear()
    def __str__(self):
        return f'{self.__itens}'
p = Pilha()
print(p)
p.empilhar('a')
print(p)
p.empilhar('b')
print(p)
p.empilhar('c')
print(p)
print(p.topo())
p.desempilhar()
p.desempilhar()
print(p)
print(p.topo())
p.esvaziar()
print(p)
