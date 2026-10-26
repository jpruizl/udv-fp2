from aereo import Aereo


class Helice(Aereo):
    """Representa un vehículo aéreo que utiliza hélices."""

    def avanzar(self):
        """Muestra cómo avanza un helicóptero."""
        print(
            "Los vehículos aéreos de hélices se desplazan mediante "
            "el giro y la inclinación de su rotor principal."
        )


if __name__ == "__main__":
    helicoptero = Helice()

    helicoptero.avanzar()
    helicoptero.identificar_tipo("hélices")
    helicoptero.verificar_temperatura(10)
    helicoptero.encender_motor()