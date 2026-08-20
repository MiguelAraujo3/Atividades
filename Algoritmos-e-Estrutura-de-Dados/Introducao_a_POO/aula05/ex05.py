class Banco:
    def __init__(self, contas):
        self.contas = contas
    def depositar(self, valor):
        self.conta.depositar(valor)
        return self.conta.saldo()
    def sacar(self, valor):
        self.conta.sacar(valor)
        return self.conta.saldo()

    def transferir(self, valor, conta_recebe, conta_saida):
        self.conta_saida = conta_saida
        self.conta_saida.sacar(valor)
        self.conta_recebe = conta_recebe
        self.conta_recebe.depositar(valor)
    def somar_saldos(self):
        soma = sum(self.contas)
        return f'A soma do saldo de todas as contas é {soma}'
    def adicionar_conta(self, conta):
        self.nova_conta = conta
        self.contas.append(conta)
        return self.contas
    def remover_conta(self, conta):
        self.apagar_conta = conta
        self.contas.pop(conta)
        return self.contas
    
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
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return self.saldo
        else: 
            print("Valor Inválido")
    def sacar(self, valor):
        if valor <= self.saldo and valor > 0:
            self.saldo -= valor
            return True
        elif valor > self.saldo:
            print("Valor inválido")
        else:
            print ("Valor Inválido")
contas = []
for i in range(3):
    numero = int(input("Número da conta: "))
    saldo = int(input("Saldo da conta: "))
    nome_titular = input("Titular da conta: ")
    contas.append(Conta(numero, saldo, nome_titular))            
'''
c1 = Conta(None, None, None);
c2 = Conta(None, None, None);
c3 = Conta(None, None, None);
c4 = Conta(None, None, None);
c5 = Conta(None, None, None);
contas = [c1,c2,c3, c4, c5]
contas_banco = [c1, c2, c3, c4]
banco = Banco(contas_banco)
for conta in contas:
    conta.numero = int(input("Número da conta: "))
    conta.saldo = int(input("Saldo da conta: "))
    conta.nome_titular = input("Titular da conta: ")
'''
banco = Banco(contas)
while(True):
    choose = input(f'[1] DEPOSITAR \n[2] SACAR \n[3]SALDO \n[4]TRANSFERIR \n[5]ADICIONAR CONTA \n[6]REMOVER CONTA \n[7]CRIAR CONTA \n[0]SAIR\n')
    if choose == '0':
        break;
    elif choose == '1':
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
    elif choose == '4': #Transferir
        numero_recebe = int(input("Digite o número da conta que vai receber: "))
        conta_receber_encontrada = None 
        for conta in contas:
            if conta.numero == numero_recebe:
                conta_receber_encontrada = conta
                break
        numero_saida = int(input("Digite o número da conta que vai transferir o dinheiro: "))
        conta_saida_encontrada = None
        for conta in contas:
            if conta.numero == numero_saida:
                conta_saida_encontrada = conta
                break
        if conta_saida_encontrada != conta_receber_encontrada:
            valor = int(input("Digite o valor de transferência: "))
            banco.transferir(valor, conta_receber_encontrada, conta_saida_encontrada)
            print(f'O valor R${valor} foi transferido da conta {conta_saida_encontrada} para a conta {conta_receber_encontrada}')
        else:
            print("Operação Inválida")
    elif choose == '5':
        numero_conta = int(input("Escolha o número da conta que deseja adicionar ao banco"))
        conta_encontrada = None
        for conta in contas:
            if conta.numero == numero:
                conta_encontrada = conta
                break
        contas.append(conta_encontrada)
        
    elif choose == '6':
        numero_conta = int(input("Escolha o número da conta que deseja adicionar ao banco"))
        conta_encontrada = None
        for conta in contas:
            if conta.numero == numero:
                conta_encontrada = conta
                contas.pop(conta_encontrada)
                break
            else:
                print(f'A conta de número {conta_encontrada.numero} não está no banco')
    elif choose == '7':
        for i in range(1):
            numero = int(input("Número da conta: "))
            saldo = int(input("Saldo da conta: "))
            nome_titular = input("Titular da conta: ")
            contas.append(Conta(numero, saldo, nome_titular))