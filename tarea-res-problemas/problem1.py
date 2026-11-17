# Problema 1
# Juan Pablo Ruiz
# 202103181
# UDV
# Fundamentos de programación 2

class Pais:
    def __init__(self, nombre):
        self.nombre = nombre

    def que_pais_soy(self):
        print(f"Soy el país {self.nombre}.")


class Guatemala(Pais):
    def __init__(self):
        super().__init__("Guatemala")

    def que_pais_soy(self):
        print(
            f"Soy el país {self.nombre} y estoy modificando "
            "el método de mi clase padre."
        )


class Mexico(Pais):
    def __init__(self):
        super().__init__("México")

    def que_pais_soy(self):
        print(
            f"Soy el país {self.nombre} y estoy modificando "
            "el método de mi clase padre."
        )


if __name__ == "__main__":
    # Demostrar el método original de la clase padre.
    pais = Pais("El Salvador")
    pais.que_pais_soy()

    # Recorrer las instancias de las dos clases hijas.
    for pais in Guatemala(), Mexico():
        pais.que_pais_soy()