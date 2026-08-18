class Aluno:
    def __init__(self, matricula, nome, notas):
        self.__matricula = matricula
        self.__nome = nome
        self.__notas = notas
    
    @property 
    def matricula (self):
        self.__matricula = str(self.__matricula)
        return f'{self.__matricula[:4]}.{self.__matricula[4]}.{self.__matricula[5:12]}'
    @property 
    def nome (self):
        return self.__nome
    @nome.setter
    def nome (self, nome):
        self.__nome = nome
        return self.__nome
    @property 
    def notas (self):
        return self.__notas
    def media (self):
        media =  sum(self.notas)/len(self.notas)
        return media
    def adiciona_nota(self, nota):
        self.notas.append(nota)
    
    def __str__ (self):
        return f'Aluno: {self.nome} \nMatrícula: {self.matricula} \nNotas {self.notas}'
        
    
a1 = Aluno (202614320024, "Miguel", [10, 10, 10])
a2 = Aluno (202614320014, "Allan", [7, 7, 7])
print(a1)
print(a2)
a1.adiciona_nota(20)
print(a1)
print("Média:", a1.media())