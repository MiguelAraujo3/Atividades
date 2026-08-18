class Conta:
    def __init__(self,numero, saldo, nome_titular):
        self.numero = numero
        self.saldo = saldo
        self.nome_titular = nome_titular
    
    def depositar(self, valor):
        if valor < 0:
            self.saldo =+ valor
        else: 
            return "Valor Inválido"
    def sacar(self, valor):
        if valor > self.saldo or valor < 0:
            self.saldo =- valor
            return True
        else:
            print ("Valor Inválido")
            return False
        