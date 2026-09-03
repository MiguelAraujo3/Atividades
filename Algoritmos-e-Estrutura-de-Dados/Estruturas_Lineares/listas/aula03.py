#Lista Sequencial
class Lista:

    def __init__(self, max):
    # cria uma lista vazia (um array de tamanho max contendo None em cada elemento)
        self.__dados = [None] * max
        self.__tamanho = 0

    def vazia(self):
    # retorna True se a lista está vazia ou False caso contrário
        return self.__tamanho == 0

    def cheia(self):
    # retorna True se a lista está cheia ou False caso contrário
        return self.__tamanho == len(self.__dados)

    def valor(self, indice):
    # retorna o valor de um índice
    # se a posição for inválida retorna None
        if indice < 0 or indice > self.__tamanho - 1:
            return None
        return self.__dados[indice]

    def posicao(self, dado):
    # retorna o índice de um valor (da 1ª ocorrência)
        for i in range(self.__tamanho):
            if self.__dados[i] == dado:
                return i
        return None

    def inserir(self, dado, indice):
    # insere um novo elemento sendo dados o valor e o índice
    # retorna True se a inserção for realizada ou False caso contrário
        if self.cheia():
            return False # erro: lista cheia
        if indice < 0 or indice > self.__tamanho:
            return False # erro: índice inválido
        for i in range(self.__tamanho, indice, -1):
            self.__dados[i] = self.__dados[i - 1]
        self.__dados[indice] = dado
        self.__tamanho += 1
        return True

    def adicionar(self, dado):
    # insere um novo elemento no final da lista, sendo dado o valor
    # retorna True se a inserção for realizada ou False caso contrário
        if self.cheia():
            return False
        self.__dados[self.__tamanho] = dado
        self.__tamanho += 1
        return True

    def retirar(self, indice):
    # remove um elemento sendo passado o índice
    # retorna o valor do elemento removido
    # se o índice for inválido não haverá remoção e retorna None
        if indice < 0 or indice > self.__tamanho - 1:
            return None
        dado = self.__dados[indice]
        for i in range(indice, self.__tamanho-1):
            self.__dados[i] = self.__dados[i + 1]
        self.__dados[self.__tamanho - 1] = None
        self.__tamanho -= 1
        return dado

    def remover(self, dado):
    # remove um elemento sendo passado o dado
    # retorna True se a remoção for realizada ou False caso contrário
        indice = self.posicao(dado)
        if indice == None:
            return False
        self.retirar(indice)
        return True

    def __str__(self):
    # método associado à função print (para fins de testes)
    # imprime o array que armazena a lista
        return str(self.__dados)

    def imprimir(self):
        for dado in self.__dados:
            print(dado, end='; ')
            
lista = Lista(5)
lista.adicionar('A')
lista.adicionar('B')
lista.adicionar('C')

while True:
    print('\n[1] Imprimir \n[2] Inserir \n[3] Adicionar \n[4] Retirar \n[5] Remover \n[6] Valor \n[7] Posição \n[0] Encerrar')
    opcao = int(input("Digite sua opção: "))
    if opcao == 0:
        break
    elif opcao == 1:
        if lista.vazia():
            print("Lista vazia")
        else:   
            lista.imprimir()
    elif opcao == 2:
        if lista.cheia():
            print("Lista cheia")
        else: 
            dado = input("Digite o dado a ser inserido: ")
            indice = int(input("Digite o índice do dado: "))
            lista.inserir(dado, indice)
    elif opcao == 3:
        if lista.cheia():
            print("Lista cheia")
        else: 
            dado = input("Digite o dado a ser inserido: ")
            lista.adicionar(dado)
    elif opcao == 4: #retirar
        if lista.vazia():
            print("Lista vazia")
        else: 
            indice = int(input("Digite o índice do dado: "))
            lista.retirar(indice)
    elif opcao == 5:
        if lista.vazia():
            print("Lista vazia")
        else: 
            dado = input("Digite o dado a ser removido: ")
            if dado not in lista:
                print("Não existe esse dado")
            else:
                lista.remover(dado)
    elif opcao == 6:
        if lista.vazia():
            print("Lista vazia")
        else:
            indice = int(input("Digite o índice do dado: "))
            lista.valor(indice)
    elif opcao == 7:
        if lista.cheia():
            print("Lista cheia")
        else: 
            dado = input("Digite o dado a ser inserido: ")
            lista.posicao(dado)