#bora
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


    def topo(self):
        if self.vazia():
            return None
        return self.__topo.dado
    
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
            print(teste.dado, end = '')
            teste = teste.proximo
            tamanho -= 1
        print()

pilha = Pilha()

numero_fixo = 13
numero_usado = numero_fixo
resto = 1321312312312313123123123123123123123123123
while numero_usado > 0:
    resto = numero_usado % 2
    numero_usado = numero_usado // 2
    pilha.empilhar(resto)

print(f'{numero_fixo} = ', end='')
pilha.imprimir()
print(pilha.tamanho())