#fila encadeada
class _No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class Fila:
    def __init__(self):
        self.__inicio = None
        self.__fim = None
        self.__tamanho = 0

    def vazio(self):
        return self.__tamanho == 0

    def primeiro(self):
        if self.vazio():
            return None
        return self.__inicio.dado
    def inserir(self, dado):
        novo = _No(dado)
        if self.vazio():
            self.__inicio = novo
        else:
            self.__fim.proximo = novo
        self.__fim = novo
        self.__tamanho +=1
        return True
    def retirar(self):
        if self.vazio():
            return False
        self.__inicio = self.__inicio.proximo
        self.__tamanho -=1
        if self.vazio():
            self.__final = None
        return True
    def imprimir(self):
        print("[", end=' ')
        atual = self.__inicio
        for i in range(self.__tamanho):
            print(atual.dado, end=' ')
            atual = atual.proximo
        print("]")
fila = Fila()
print(fila)
fila.inserir('A')
fila.imprimir()
fila.inserir('B')
fila.imprimir()
fila.inserir('C')
fila.imprimir()
fila.retirar()
fila.imprimir()
fila.inserir('D')
fila.imprimir()
