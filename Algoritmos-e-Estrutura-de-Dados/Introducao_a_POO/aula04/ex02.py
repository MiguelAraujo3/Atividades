class Cliente:
    def  __init__(self, cpf, nome):
        self.__cpf = cpf
        self.__nome = nome
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    def __str__(self):
        return f'Cliente {self.__nome} de CPF {self.__cpf}'
    
class Conta:
    def __init__(self, numero, cliente):
        self.__numero = numero
        self.__cliente = cliente
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
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cleinte(self, cliente):
        self.__cliente = cliente

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    def __str__(self):
        return f'Número: {self.__numero} Titular: {self.__cliente} Saldo: {self.__saldo}'  
cliente = Cliente(71885282480, "miguel")
conta = Conta(12312, cliente)
print(conta)
cliente.nome = 'Allan'
print(conta)
conta.depositar(float(input("Digite o valor do deposito: ")))
conta.sacar(float(input("Digite o valor do saque: ")))
print(conta)
