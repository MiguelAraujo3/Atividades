class Motor():
    def __init__(self, cilindrada, combustivel):
        self.__cilindrada = cilindrada;
        self.__combustivel = combustivel;
    @property
    def cilindrada(self):
        return self.__cilindrada;
    @cilindrada.setter
    def cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada

    @property
    def combustivel(self):
        return self.__combustivel;
    @combustivel.setter
    def combustivel(self, combustivel):
        self.__combustivel = combustivel
    
    def __str__(self):
        return f'Cilindrada: {self.__cilindrada}; Combustível: {self.__combustivel}'
class Carro():
    def __init__(self, cor, placa, motor):
        self.__cor = cor;
        self.__placa = placa;
        self.__motor = motor;
    
    @property
    def cor(self):
        return self.__cor;
    @cor.setter
    def cor(self, cor):
        self.__cor = cor;
    
    @property
    def placa(self):
        return self.__placa;
    @placa.setter
    def placa(self, placa):
        self.__placa = placa
    @property 
    def motor(self):
        return self.__motor;
    @motor.setter
    def motor(self, motor):
        self.__motor = motor
    
    def __str__(self):
        return f'Carro: Cor: {self.__cor}; Placa: {self.__placa}; {self.__motor}'
    
motor = Motor(1.5, 'Alcool')
carro = Carro('verde', '3123NDA', motor)

print(carro)