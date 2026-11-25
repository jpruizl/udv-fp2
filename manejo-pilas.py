class Pila:
    """Implementa una pila: el último en entrar es el primero en salir."""

    def __init__(self):
        self._elementos = []

    def esta_vacia(self):
        return len(self._elementos) == 0

    def apilar(self, elemento):
        self._elementos.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            raise IndexError("No se puede desapilar una pila vacía.")

        return self._elementos.pop()

    def obtener_elementos(self):
        """Devuelve una copia en orden de base a cima."""
        return self._elementos.copy()


def main():
    pila = Pila()

    print("MANEJO DE UNA PILA")
    print("Principio: último en entrar, primero en salir.")
    print("\nIngrese cinco elementos:")

    for numero in range(1, 6):
        while True:
            elemento = input(f"Elemento {numero}: ").strip()

            if elemento:
                pila.apilar(elemento)
                break

            print("Entrada inválida. Ingrese un valor no vacío.")

    print("\nPila inicial (base -> cima):")
    print(pila.obtener_elementos())

    print("\nDesapilando tres elementos:")

    for numero in range(1, 4):
        retirado = pila.desapilar()
        print(f"Elemento retirado {numero}: {retirado}")

    print("\nElementos restantes (base -> cima):")
    print(pila.obtener_elementos())


if __name__ == "__main__":
    main()