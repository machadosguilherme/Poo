class Televisao:
    def __init__(self):
        self.canal = None
        self.volume = 0

    def aumentar_volume(self):
        self.volume += 1
        return self.volume

    def diminuir_volume(self):
        self.volume -= 1
        return self.volume

    def alterar_canal(self, canal):
        self.canal = canal 
        return canal


tv = Televisao()
tv.alterar_canal(5)
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
print(f'A tv está no canal {tv.canal}')
print(f'A tv está no volume {tv.volume}')
