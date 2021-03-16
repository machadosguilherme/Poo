class Carro:
    def __init__(self):
        self.quantidade_combustivel = 0

    def adicionar_combustivel(self, litros):
        self.quantidade_combustivel += litros
        return self.quantidade_combustivel

    def obter_combustivel(self):
        self.quantidade_combustivel
        return self.quantidade_combustivel

    def andar(self, distancia):
        consumo = 0.2 * distancia
        qnt = self.quantidade_combustivel - consumo
        self.quantidade_combustivel = qnt
        return qnt


meu_carro = Carro()				
meu_carro.adicionar_combustivel(20)				# Adiciona 20 litros
meu_carro.andar(80)						# Andar 80 quilômetros 
print(f'Litros de combustível no tanque: {meu_carro.obter_combustivel()}')
