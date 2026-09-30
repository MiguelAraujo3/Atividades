class _No:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

class ListaEncadeada:
    def __init__(self):
        self.__inicio = None

    def vazia(self):
        return self.__inicio == None

    def adicionar(self, dado):
    # insere um novo elemento no final da lista, sendo dado o valor
    # retorna True sempre (p/ manter a compatibilidade com a implementação sequencial)
        novo = _No(dado)
        if self.vazia():
            self.__inicio = novo
            return True
        atual = self.__inicio
        while atual.prox != None:
            atual = atual.prox
        atual.prox = novo
        return True

    def imprimir(self, nome=None):
    # imprime os elementos da lista
        if nome != None:
            print(nome, end=' -> ')
        print('[', end='')
        atual = self.__inicio
        while atual != None:
            if atual.prox != None:
                print(atual.dado, end=', ')
            else:
                print(atual.dado, end='')
            atual = atual.prox
        print(']')

    def busca_sequencial(self, valor):
        atual = self.__inicio
        posicao =0
        while atual != None:
            if atual.dado == valor:
                return posicao
            atual = atual.prox
            posicao += 1
        return None
    def busca_sequencial_ordenada(self, valor):
        atual = self.__inicio
        posicao = 0
        while atual != None:
            if atual.dado == valor:
                return posicao
            if atual.dado > valor:
                break
            atual = atual.prox
            posicao += 1
        return None
    def busca_transposicao(self, valor):
        if self.vazia():
            return None
        atual = self.__inicio
        posicao = 0

        if atual.dado == valor:
            return posicao
        while atual.prox != None:
            if atual.prox.dado == valor:
                atual.dado, atual.prox.dado = atual.prox.dado, atual.dado
                return posicao + 1
            atual = atual.prox
            posicao += 1
        return None
    def busca_mover_para_frente(self, valor):
        atual = self.__inicio
        anterior = None
        posicao = 0
        while atual != None:
            if atual.dado == valor:
                if atual.prox is not None:
                    anterior.prox = atual.prox
                    atual.prox = self.__inicio
                    self.__inicio = atual
                return posicao
            anterior = atual
            atual = atual.prox
            posicao += 1
        return None

lista = ListaEncadeada()
lista.adicionar('A')
lista.adicionar('B')
lista.adicionar('C')
lista.adicionar('D')
lista.adicionar('E')
lista.imprimir()
print('Sequencial:', lista.busca_sequencial('D'))
print('Seq. Ordenada:', lista.busca_sequencial_ordenada('D'))
print('Transposicao:', lista.busca_transposicao('D'))
lista.imprimir()
print('Mover-para-frente:', lista.busca_mover_para_frente('D'))
lista.imprimir()