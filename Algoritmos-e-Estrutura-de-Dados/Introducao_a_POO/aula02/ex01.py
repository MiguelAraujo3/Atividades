class Ponto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def quadrante(self):
        if self.x > 0 and self.y > 0:
            return "Primeiro quadrante"
        elif self.x > 0 and self.y < 0:
            return "Quarto quadrante"
        if self.x < 0 and self.y > 0:
            return "Segundo quadrante"
        if self.x < 0 and self.y < 0:
            return "Terceiro quadrante"
        else: 
            return None

p1 = Ponto(4, 5)
p2 = Ponto(-4, 5)
p3 = Ponto(-4, -5)
p4 = Ponto(4, -5)
p5 = Ponto(0,0)

print(f'Ponto 1 : {p1.x}, {p1.y}; Quadrante: {p1.quadrante()}')
print(f'Ponto 1 : {p2.x}, {p2.y}; Quadrante: {p2.quadrante()}')
print(f'Ponto 1 : {p3.x}, {p3.y}; Quadrante: {p3.quadrante()}')
print(f'Ponto 1 : {p4.x}, {p4.y}; Quadrante: {p4.quadrante()}')
print(f'Ponto 1 : {p5.x}, {p5.y}; Quadrante: {p5.quadrante()}')
