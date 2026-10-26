from terrestre import Terrestre


class Vias(Terrestre):
    """Representa un vehículo terrestre que se desplaza sobre vías."""

    def avanzar(self):
        """Muestra cómo avanza un tren sobre las vías."""
        print(
            "Los vehículos terrestres de vías se desplazan "
            "hacia adelante o hacia atrás haciendo girar "
            "sus ruedas sobre los rieles."
        )


if __name__ == "__main__":
    tren = Vias()

    tren.avanzar()
    tren.identificar_tipo("vías")
    tren.verificar_temperatura(10)
    tren.encender_motor()