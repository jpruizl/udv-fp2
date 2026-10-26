from vehiculo import Vehiculo


class Aereo(Vehiculo):
    """Representa la categoría de vehículos aéreos."""

    def identificar_tipo(self, tipo):
        """Identifica el vehículo aéreo que extiende esta clase."""
        print(
            "Esta clase está siendo extendida desde la clase "
            f"vehículo aéreo de {tipo}."
        )