class Retangulo():
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
    def calcular_area(self):
        area = self.altura * self.largura
        return area
    def eh_quadrado(self):
        if self.altura == self.largura:
            return  "É quadrado"
        else: 
            return "Não é quadrado"
        
r1 = Retangulo(5, 4)
r2 = Retangulo(6, 6)

print(f'Retângulo 1: Largura: {r1.largura}; Altura: {r1.altura}; Área: {r1.calcular_area()}; {r1.eh_quadrado()}')
print(f'Retângulo 2: Largura: {r2.largura}; Altura: {r2.altura}; Área: {r2.calcular_area()}; {r2.eh_quadrado()}')