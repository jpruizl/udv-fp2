from vehiculo import Vehiculo


class Terrestre(Vehiculo):
    """Representa la categoría de vehículos terrestres."""

    def identificar_tipo(self, tipo):
        """Identifica el vehículo terrestre que extiende esta clase."""
        print(
            "Esta clase está siendo extendida desde la clase "
            f"vehículo terrestre de {tipo}."
        )