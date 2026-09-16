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
        print (self.__tamanho)
        return self.__tamanho;

    def topo(self):
        if self.vazia():
            return None
        print(self.__topo.dado)
        return True
    
    def empilhar(self, dado):
        novo = _No(dado);
        self.__tamanho += 1;
        novo.proximo = self.__topo
        self.__topo = novo
        return True
    
    def desimpilhar(self):
        if self.vazia():
            return None
        self.__topo = self.__topo.proximo;
        self.__tamanho -= 1;
    
    def esvaziar(self):
        if self.vazia():
            return None
        while self.__tamanho != 0:
            self.__topo = self.__topo.proximo
            self.__tamanho -= 1
        self.__topo = None
        return True
    def imprimir(self):
        if self.vazia():
            print("Pilha Vazia")
        tamanho = self.__tamanho
        teste = self.__topo
        while tamanho != 0:
            print(teste.dado, end = ', ')
            teste = teste.proximo
            tamanho -= 1
        print()

pilha = Pilha()
choose = -1
while choose != 0:
    choose = int(input("Digite sua opção: "))
    
    if choose == 1:
        pilha.imprimir()
    elif choose == 2:
        numero = input("Digite o que vai ser empilhado: ")
        pilha.empilhar(numero)

    elif choose == 3:
        pilha.desimpilhar()
    elif choose == 4:
        pilha.esvaziar()
    elif choose == 5:
        pilha.topo()
    elif choose == 6:
        pilha.tamanho()
    elif choose == 0:
        break
    else:
        print("Escolha Inválida")