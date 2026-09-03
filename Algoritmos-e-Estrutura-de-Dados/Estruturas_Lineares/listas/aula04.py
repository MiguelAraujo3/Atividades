class _No: 
    def __init__(self, dado):
        self.dado = dado;
        self.proximo = None;
class Lista:
    def __init__(self):
        self.__inicio = None;
        self.__tamanho = 0;
    def tamanho(self):
        return self.__tamanho

    def vazia(self):
        return self.__inicio == None

    def imprimir(self): 
        atual = self.__inicio
        while atual != None:
            if atual.dado == None:
                print(end='')
            else:
                print(atual.dado, end=', ')
            atual = atual.proximo
        print()

    def inserir(self, posicao, dado):
        novo = _No(dado)
        self.__tamanho += 1
        if self.vazia():
            self.__inicio = novo
            return 
        
        if posicao <= 0:
            novo.proximo = self.__inicio
            self.__inicio = novo
            return
        i = 0 
        atual = self.__inicio
        while atual.proximo is not None and i < posicao - 1:
            atual = atual.proximo
            i += 1
        novo.proximo = atual.proximo
        atual.proximo = novo 
    def buscar(self, posicao):
        if posicao < 0 or posicao >= self.__tamanho:
            raise IndexError("Posição Inválida");
        atual = self.__inicio
        for i in range(posicao):
            atual = atual.proximo
        return atual.dado
    def remover_posicao(self, posicao):
        if posicao < 0 or posicao >= self.__tamanho:
            raise IndexError("Posição Inválida");
        if self.vazia():
            return "lista vazia"
        atual = self.__inicio
        for i in range(posicao-1):
            atual = atual.proximo
        while atual.proximo != None: 
            atual.dado = atual.proximo.dado        
            atual = atual.proximo
        atual.dado = None
        return

lista = Lista()

lista.inserir(0,5)
lista.inserir(1,10)
lista.inserir(1,15)
lista.inserir(2,8)
lista.imprimir()
print(lista.buscar(2))
print(lista.buscar(1))
print(lista.buscar(3))
print("--------------")
lista.imprimir()
lista.remover_posicao(1)
lista.imprimir()
lista.remover_posicao(3)
lista.imprimir()
lista.remover_posicao(1)
lista.imprimir()
lista.remover_posicao(1)
lista.imprimir()

print(lista.tamanho())
