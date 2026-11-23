class CuentaBancaria:
    def __init__(self, nombre: str, saldo: float = 0):
        if saldo < 0:
            raise ValueError("El saldo no puede ser negativo")
        
        self.nombre = nombre
        self.saldo = saldo

    def ingresar(self, cantidad: float):
        if cantidad < 0:
            raise ValueError("La cantidD NO PUEDE SER NEGATIVA")
        self.saldo += cantidad

    def retirar(self, cantidad: float):
        if cantidad > self.saldo or cantidad < 0:
            raise ValueError("La cntidad no puede ser negativa o superior al saldo")
        self.saldo -= cantidad


    def __str__(self):
        return f"Cuenta bancaria[Nombre = {self.nombre} | Saldo = {self.saldo}]"

cuenta1 = CuentaBancaria("Pepito")
cuenta2 = CuentaBancaria("Juanito", 100)
cuenta1.ingresar(100)
cuenta2.retirar(50)
print(cuenta1)
print(cuenta2)