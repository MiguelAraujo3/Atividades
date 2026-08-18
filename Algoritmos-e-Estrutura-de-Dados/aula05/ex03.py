class Pais:
    def __init__(self, nome, capital, dimensao):
        self.__nome = nome;
        self.__capital= capital;
        self.__dimensao = dimensao;
        self.paises = []
        
    @property 
    def nome (self):
        return self.__nome
    @property 
    def capital (self):
        return self.__capital
    @property 
    def dimensao (self):
        return self.__dimensao
    
    def paises_fronteira(self, paises):
        self.paises = paises
        return self.paises
    def add_pais(self, pais):
        if pais in self.paises:
            return "Esse País já está na lista"
        else:        
            self.paises.append(pais)
       
    def __str__(self):
        return f'Páis: {self.nome} \nCapital: {self.capital} \nDimensão: {self.dimensao}km² \nPaíses Vizinhos: {self.paises}'
    
p1 = Pais("Brasil", "Brasilia", 31213)
print(p1)
p1.add_pais("Argentina")
print(p1)