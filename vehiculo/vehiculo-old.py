class Vehiculo:
    """Define los comportamientos generales de los vehículos."""

    def verificar_temperatura(self, temperatura):
        """Recibe la temperatura y la muestra en pantalla."""
        print(f"La temperatura del vehículo es de {temperatura} grados.")

    def encender_motor(self):
        """Muestra el mensaje de encendido del motor."""
        print("Encendiendo motor.")