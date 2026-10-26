from terrestre import Terrestre


class Llantas(Terrestre):
    """Representa un vehículo terrestre que utiliza llantas."""

    def avanzar(self):
        """Muestra cómo avanza un vehículo con llantas."""
        print(
            "Los vehículos terrestres de llantas se desplazan "
            "hacia adelante o hacia atrás girando las llantas."
        )


if __name__ == "__main__":
    automovil = Llantas()

    automovil.avanzar()
    automovil.identificar_tipo("llantas")
    automovil.verificar_temperatura(10)
    automovil.encender_motor()