class Fila:
    def __init__(self, max):
        self.__dados = [None] * max
        self.__inicio = 0
        self.__fim = 0
        self.__tamanho = 0
        self.__max = max

    def vazia(self):
        return self.__tamanho == 0
    def cheia(self):
        return self.__tamanho == self.__max
    def inserir(self, dado):
        if self.cheia():
            return False
        self.__tamanho += 1
        self.__dados[self.__fim] = dado
        self.__fim = (self.__fim + 1) % self.__max
        return True
    def retirar(self):
        if self.vazia():
            return False
        dado = self.__dados[self.__inicio] 
        self.__tamanho -= 1
        self.__dados[self.__inicio] = None
        self.__inicio =  (self.__inicio + 1) % self.__max
        return dado
    def primeiro(self):
        return self.__dados[self.__inicio]
    def __len__(self):
        return self.__tamanho
    def imprimir(self):
        print("[", end=' ')
        indice = self.__inicio
        for i in range (self.__tamanho):
            print(self.__dados[indice], end=' ')
            indice = (indice +1) % self.__max
        print(']')
    def imprimir1(self):
        print(self.__dados)

fila = Fila(3)
fila.imprimir()
fila.inserir(1)
fila.inserir(2)
fila.inserir(3)
fila.imprimir()
fila.retirar()
fila.imprimir()
fila.inserir(4)
fila.imprimir()
fila.inserir(1)
fila.imprimir()
fila.retirar()
fila.imprimir()
fila.inserir(1)
fila.imprimir()