class Conta:
    def __init__(self, numero, saldo, nome):
        self.numero = numero
        self.__saldo = saldo
        self.nome_titular = nome
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
        return self.__saldo
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return self.saldo
        else: 
            return "Valor Inválido"
    def sacar(self, valor):
        if valor < self.saldo or valor > 0:
            self.saldo -= valor
            return True
        else:
            print ("Valor Inválido")
            return False

c1 = Conta(None, None, None);
c2 = Conta(None, None, None);
c3 = Conta(None, None, None);
c4 = Conta(None, None, None);
c5 = Conta(None, None, None);
contas = [c1,c2,c3,c4,c5]

for conta in contas:
    conta.numero = int(input("Número da conta: "))
    conta.saldo = int(input("Saldo da conta: "))
    conta.nome_titular = input("Titular da conta: ")

while(True):
    choose = input(f'[1] DEPOSITAR \n[2] SACAR \n[3]SALDO \n[0]SAIR\n')
    if choose == '1':
        numero = int(input("Digite o número da conta: "))
        conta_encontrada = None
        for conta in contas:
            if conta.numero == numero:
                conta_encontrada = conta
        if conta_encontrada:
            valor = int(input("Digite o valor a ser depositado: "))
            conta_encontrada.depositar(valor)
        else: 
            print("Número de conta inválido")
        conta_encontrada = False
    elif choose == '2':
        numero = int(input("Digite o número da conta: "))
        conta_encontrada = None
        for conta in contas:
            if conta.numero == numero:
                conta_encontrada = conta
                break
        if conta_encontrada:
            valor = int(input("Digite o valor a ser sacado: "))
            conta_encontrada.sacar(valor)
        else: 
            print("Número de conta inválido") 
        conta_encontrada = False
    elif choose == '3':
        numero = int(input("Digite o número da conta: "))
        conta_encontrada = None
        for conta in contas:
            if conta.numero == numero:
                conta_encontrada = conta
                break
        if conta_encontrada:
            print(f'A conta de número {conta_encontrada.numero} tem o SALDO de {conta_encontrada.saldo}')
        else: 
                print("Número de conta inválido")
        conta_encontrada = False
    elif choose == '0':
        break;
    else: 
        print("Operação Inválida")