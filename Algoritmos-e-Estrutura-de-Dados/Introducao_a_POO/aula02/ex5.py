class Ponto():
    def __init__(self):
        self.__x = None
        self.__y = None
     
    @property   
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    @x.setter
    def x(self, x):
        self.__x = x
        
    @y.setter
    def y(self, y):
        self.__y = y
        
p1 = Ponto()

p1.x(2)
p1.y(3)

print(f'Ponto 1: {p1.x()}, {p1.y()}')
