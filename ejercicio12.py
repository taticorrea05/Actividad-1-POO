class Empleado:
    def __init__(self, horas_trabajadas, valor_hora, porcentaje_retencion):
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.porcentaje_retencion = porcentaje_retencion
        self.salario_bruto = 0
        self.retencion = 0
        self.salario_neto = 0

    def calcular_salario_bruto(self):
        self.salario_bruto = self.horas_trabajadas * self.valor_hora

    def calcular_retencion(self):
        self.retencion = (
            self.salario_bruto * self.porcentaje_retencion / 100
        )

    def calcular_salario_neto(self):
        self.salario_neto = self.salario_bruto - self.retencion

    def mostrar_resultados(self):
        print("SALARIO BRUTO:", self.salario_bruto)
        print("RETENCIÓN EN LA FUENTE:", self.retencion)
        print("SALARIO NETO:", self.salario_neto)


# Programa principal
empleado = Empleado(48, 5000, 12.5)

empleado.calcular_salario_bruto()
empleado.calcular_retencion()
empleado.calcular_salario_neto()
empleado.mostrar_resultados()
