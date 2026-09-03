#pilha encadeada
class _No:
    def __init__(self, dado):
        self.dado = dado;
        self.proximo = None;
class Pilha:
    def __init__(self):
        self.__topo = None;
        self.__tamanho = 0;
    def vazia(self):
        return self.__topo == None

    def tamanho(self):
        return self.__tamanho;

    def empilhar(self, dado):
        novo = _No(dado);
        self.__tamanho += 1;
        novo.proximo = self.__topo
        self.__topo = novo
        return True
    
    def desimpilhar(self):
        while self.__tamanho != 0:
            self.__topo = self.__topo.proximo
            self.__tamanho -= 1;
    
    def imprimir(self):
        tamanho = self.__tamanho
        teste = self.__topo
        while tamanho != 0:
            print(teste.dado, end = ', ')
            teste = teste.proximo
            tamanho -= 1
        print()
         
pilha = Pilha()
pilha.empilhar("a")
pilha.empilhar("b")
pilha.empilhar("c")
pilha.imprimir()
print(pilha)
pilha.desimpilhar()
pilha.imprimir()