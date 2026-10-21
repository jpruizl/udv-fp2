from decimal import Decimal, ROUND_HALF_UP


class Descuentos:

    def __init__(self, salario):
        self.salario = Decimal(str(salario)).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP
        )

        self.datos_sueldo = []
        self.calcular_descuentos()

    def calcular_descuentos(self):
        igss = (self.salario * Decimal("0.0483")).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP
        )

        if self.salario >= Decimal("4167.00"):
            isr = (self.salario * Decimal("0.05")).quantize(
                Decimal("0.01"),
                rounding=ROUND_HALF_UP
            )
        else:
            isr = Decimal("0.00")

        salario_con_descuento = self.salario - igss - isr

        # La lista almacena únicamente valores.
        self.datos_sueldo = [
            self.salario,
            salario_con_descuento,
            igss,
            isr
        ]

        return self.datos_sueldo

    def mostrar_sueldo(self):
        print("\nINFORMACIÓN DEL SUELDO")

        print(
            f"Sueldo sin deducciones: "
            f"Q{self.datos_sueldo[0]:,.2f}"
        )

        print(
            f"Sueldo con deducciones: "
            f"Q{self.datos_sueldo[1]:,.2f}"
        )

        print(
            f"Descuento de IGSS: "
            f"Q{self.datos_sueldo[2]:,.2f}"
        )

        print(
            f"Descuento de ISR: "
            f"Q{self.datos_sueldo[3]:,.2f}"
        )