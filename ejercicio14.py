class Numero:
    def __init__(self, valor):
        self.valor = valor
        self.cuadrado = 0
        self.cubo = 0

    def calcular_cuadrado(self):
        self.cuadrado = self.valor ** 2

    def calcular_cubo(self):
        self.cubo = self.valor ** 3

    def mostrar_resultados(self):
        print("EL CUADRADO DEL NÚMERO ES:", self.cuadrado)
        print("EL CUBO DEL NÚMERO ES:", self.cubo)


# Programa principal
valor = float(input("Ingrese un número: "))

numero = Numero(valor)

numero.calcular_cuadrado()
numero.calcular_cubo()
numero.mostrar_resultados()
