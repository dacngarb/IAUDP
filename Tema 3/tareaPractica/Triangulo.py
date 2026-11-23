from Figura import Figura

class Triangulo(Figura):
    def __init__(self, base = 1, altura = 1):
        if base <= 0 or altura <= 0:
            raise ValueError("La base y la altura deben ser mator a 0")
        self.base = base
        self.altura = altura

    def area (self):
        return (self.base * self.altura) /2

    def perimetro(self):
        return self.base * 3

    def __str__(self):
        return f"Triangulo [Base = {self.base} | Altura = {self.altura}]"
t = Triangulo(3, 3)
print(t.area())
print(t.perimetro())