class TV():
    def __init__(self):
        self.ligada = False

    def liga_desliga(self):
        if  not self.ligada:
            self.ligada = not self.ligada
        self.canal = 7
        self.volume = 42
    def mudar_canal(self, canal):
        if self.ligada:
            self.canal = canal
    def aumentar_volume(self):
        if self.ligada:
            self.volume += 1
    def diminuir_volume(self):
        if self.ligada:
            self.volume -= 1       
    def imprimir(self):
        if self.ligada :
            print(f'Canal {self.canal}, Volume {self.volume}')
        else: 
            print('Tv desligada')
            
tv = TV()
tv.imprimir()
tv.liga_desliga()
tv.imprimir()
tv.mudar_canal(6)
tv.imprimir()
tv.aumentar_volume()
tv.imprimir()
tv.diminuir_volume()
tv.diminuir_volume()
tv.imprimir()