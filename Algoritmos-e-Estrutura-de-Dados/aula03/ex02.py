class Conta:
    def __init__(self, numero, titular):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = 0

    def depositar(self, valor):
        self.__saldo += valor

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

conta = Conta(12312,'Miguel')
print(f'Número: {conta.numero} Titular: {conta.titular} Saldo: {conta.saldo}')

conta.numero = 31231
conta.titular = 'Allan'
print(f'Número: {conta.numero} Titular: {conta.titular} Saldo: {conta.saldo}')
conta.depositar(float(input("Digite o valor do deposito: ")))
print(f'Número: {conta.numero} Titular: {conta.titular} Saldo: {conta.saldo}')

