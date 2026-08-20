class Data:
    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
        
    @property 
    def dia (self):
        return self.__dia
    @dia.setter
    def dia (self, dia):
        self.__dia = dia
        return self.__dia
    @property 
    def mes (self):
        return self.__mes
    @mes.setter
    def mes (self, mes):
        self.__mes = mes
        return self.__mes
    @property 
    def ano (self):
        return self.__ano
    @ano.setter
    def ano (self, ano):
        self.__ano = ano
        return self.__ano

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano:02d}"
    
aniversario = Data(16, 5, 2008)
inicio_curso = Data(25, 2, 2008)
primeiro_dia = Data(1,1,2026)

print(aniversario)
print(inicio_curso)
print(primeiro_dia)