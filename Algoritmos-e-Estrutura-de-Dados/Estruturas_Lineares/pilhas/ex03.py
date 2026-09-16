#pilha encadeada
class _No:
    def __init__(self, dado):
        self.dado = dado;
        self.proximo = None;
class Pilha:
    def __init__(self):
        self.__topo = None;
        self.__tamanho = 0;
        self.__abertos = 0;
        self.__fechados = 0;
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
        if novo.dado == "(":
            self.__abertos += 1
        if novo.dado == ")":
            self.__fechados += 1
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

    def desimpilhar(self):
        if self.vazia():
            return None
        self.__topo = self.__topo.proximo;
        self.__tamanho -= 1;

    def verificar(self):
        if self.__abertos == self.__fechados:
            return True
        return False

pilha = Pilha()
frase = "(A + B) * C)"
for letra in frase:
    if letra == "(" or letra == ")":
        pilha.empilhar(letra)
if pilha.verificar():
    print(f'{frase} -> correta')
else:
    print(f'{frase} -> incorreta')
