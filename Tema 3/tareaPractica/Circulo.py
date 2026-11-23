import math

from Figura import Figura

class Circulo(Figura):
    def __init__(self, radio = 1):
        if radio <= 0:
            raise ValueError("La radio debe ser mator a 0")
        self.radio = radio
        

    def area(self):
        return (math.pi  * self.radio**2)

    def perimetro(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return f"Circulo [Radio = {self.radio}]"

c = Circulo(5)
print(c.area())
print(c.perimetro())