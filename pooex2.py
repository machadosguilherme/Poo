class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def calcular_perimeitro(self):
        perimetro = self.lado_a + self.lado_b + self.lado_c
        return perimetro
