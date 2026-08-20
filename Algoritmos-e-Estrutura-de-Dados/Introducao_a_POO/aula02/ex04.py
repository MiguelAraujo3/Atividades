class Ponto():
    def __init__(self):
        self.__x = None
        self.__y = None
        
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def set_x(self, x):
        self.__x = x
    def set_y(self, y):
        self.__y = y
        
p1 = Ponto()
p1.set_x(2)
p1.set_y(3)

print(f'Ponto 1: {p1.get_x()}, {p1.get_y()}')
