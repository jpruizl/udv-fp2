class Habitacion:
    def __init__(self, numero, torre, tipo, precio):
        self.numero = numero
        self.torre = torre
        self.tipo = tipo
        self.precio = precio
        self.reservada = False

    def reservar(self):
        if not self.reservada:
            self.reservada = True
            print(f"Habitación {self.numero} en {self.torre} reservada correctamente.")
        else:
            print(f"La habitación {self.numero} ya está reservada.")

    def mostrar_info(self):
        estado = "Reservada" if self.reservada else "Disponible"
        print(f"Habitación: {self.numero}")
        print(f"Torre: {self.torre}")
        print(f"Tipo: {self.tipo}")
        print(f"Precio por noche: Q{self.precio}")
        print(f"Estado: {estado}")


class HabitacionFrenteMar(Habitacion):
    def __init__(self, numero, torre, tipo, precio, vista_mar, recargo):
        super().__init__(numero, torre, tipo, precio)
        self.vista_mar = vista_mar
        self.recargo = recargo

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Vista al mar: {self.vista_mar}")
        print(f"Recargo adicional: Q{self.recargo}")
        print(f"Precio total por noche: Q{self.precio + self.recargo}")


# Habitaciones en las dos torres del complejo
habitacion1 = Habitacion(101, "Torre 1", "Sencilla", 350)
habitacion2 = Habitacion(205, "Torre 2", "Doble", 500)

# Habitación en la torre frente al mar
habitacion3 = HabitacionFrenteMar(301, "Torre Frente al Mar", "Suite", 800, "Sí", 250)

# Mostrar información inicial
print("=== HABITACIONES DISPONIBLES ===")
habitacion1.mostrar_info()
print()
habitacion2.mostrar_info()
print()
habitacion3.mostrar_info()

# Reservar habitaciones
print("\n=== PROCESO DE RESERVA ===")
habitacion1.reservar()
habitacion3.reservar()

# Mostrar información final
print("\n=== ESTADO FINAL ===")
habitacion1.mostrar_info()
print()
habitacion3.mostrar_info()
