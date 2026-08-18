class Conta:
    def __init__(self, numero, titular):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else: 
            return "Valor inválido para depósito"
    
    def sacar(self, valor): 
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
        elif valor < 0:
            return "Valor Inválido"
        else:
            return "Solicite o saldo para saber quanto pode sacar"
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    def imprimir(self):
        print(f'Número: {self.__numero} Titular: {self.__titular} Saldo: {self.__saldo}')  

conta = Conta(12312,'Miguel')
conta.imprimir()
conta.numero = 31231
conta.titular = 'Allan'
conta.imprimir()
conta.depositar(float(input("Digite o valor do deposito: ")))
conta.sacar(float(input("Digite o valor do saque: ")))
conta.imprimir()
