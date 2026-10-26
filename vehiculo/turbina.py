from aereo import Aereo


class Turbina(Aereo):
    """Representa un vehículo aéreo que utiliza turbinas."""

    def avanzar(self):
        """Muestra cómo avanza un avión con turbinas."""
        print(
            "Los vehículos aéreos de turbinas avanzan mediante "
            "el empuje generado por sus turbinas."
        )


if __name__ == "__main__":
    avion = Turbina()

    avion.avanzar()
    avion.identificar_tipo("turbinas")
    avion.verificar_temperatura(10)
    avion.encender_motor()