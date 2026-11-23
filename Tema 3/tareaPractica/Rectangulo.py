from Figura import Figura

class Rectangulo(Figura):
    def __init__(self, base = 1, altura = 1):
        if base <= 0 or altura <= 0:
            raise ValueError("La base y la altura deben ser mator a 0")
        self.base = base
        self.altura = altura

    def area (self):
        return self.base * self.altura

    def perimetro(self):
        return self.base * 2 + self.altura * 2

    def __str__(self):
        return f"Rectangulo [Bse = {self.base} | Altura = {self.altura}]"

r = Rectangulo()
print(r.perimetro())
        