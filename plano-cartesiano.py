from math import sqrt


class Punto:

    array_de_puntos = []

    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            print("El punto está en el origen")

        elif self.x == 0:
            print("El punto está sobre el eje Y")

        elif self.y == 0:
            print("El punto está sobre el eje X")

        elif self.x < 0 and self.y > 0:
            print("Cuadrante 2")

        elif self.x < 0 and self.y < 0:
            print("Cuadrante 3")

        elif self.x > 0 and self.y < 0:
            print("Cuadrante 4")

        else:
            print("Cuadrante 1")

        punto = [self.x, self.y]
        self.array_de_puntos.append(punto)

    def vector(self):
        resultado_x = (
            self.array_de_puntos[1][0]
            - self.array_de_puntos[0][0]
        )

        resultado_y = (
            self.array_de_puntos[1][1]
            - self.array_de_puntos[0][1]
        )

        print("Resultado X:", resultado_x)
        print("Resultado Y:", resultado_y)
        print("Vector del punto 1 al punto 2:",
              (resultado_x, resultado_y))

    def distancia(self):
        x1 = self.array_de_puntos[0][0]
        y1 = self.array_de_puntos[0][1]

        x2 = self.array_de_puntos[1][0]
        y2 = self.array_de_puntos[1][1]

        resultado = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        print(f"Distancia entre los puntos: {resultado:.2f} unidades")


if __name__ == "__main__":

    print("PLANO CARTESIANO")
    print("-" * 40)

    Punto.array_de_puntos.clear()

    for numero in range(1, 3):
        print(f"\nIngrese el punto {numero}")

        while True:
            try:
                x = float(input("Coordenada X: "))
                y = float(input("Coordenada Y: "))
                break

            except ValueError:
                print("Ingrese números válidos.")
                print("Para decimales utilice punto, por ejemplo: 2.5")

        plano = Punto(x, y)

        print("Punto ingresado:", plano)
        plano.cuadrante()

    print("\nRESULTADOS")
    print("-" * 40)

    plano.vector()
    plano.distancia()