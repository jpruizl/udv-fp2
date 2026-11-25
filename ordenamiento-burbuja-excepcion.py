def ordenamiento_burbuja(lista):
    """Ordena una lista de enteros; devuelve None si la entrada es inválida."""
    try:
        if not isinstance(lista, list):
            raise TypeError(
                "Se esperaba una lista de números enteros."
            )

        # Validar todos los elementos antes de ordenar.
        for posicion, elemento in enumerate(lista, start=1):
            if type(elemento) is not int:
                raise TypeError(
                    f"El elemento en la posición {posicion}, "
                    f"con valor {elemento!r}, es de tipo "
                    f"{type(elemento).__name__}. "
                    "Solo se permiten números enteros."
                )

        ordenada = lista.copy()
        n = len(ordenada)

        # Ordenamiento de burbuja ascendente.
        for i in range(n - 1):
            hubo_intercambio = False

            for j in range(n - 1 - i):
                if ordenada[j] > ordenada[j + 1]:
                    ordenada[j], ordenada[j + 1] = (
                        ordenada[j + 1],
                        ordenada[j],
                    )
                    hubo_intercambio = True

            if not hubo_intercambio:
                break

        return ordenada

    except TypeError as error:
        print(f"Error de tipo: {error}")
        return None


def main():
    casos = [
        ("Lista de enteros", [8, 3, 5, 1, 9, 2]),
        ("Lista de strings", ["pera", "manzana", "uva"]),
        ("Lista mixta", [8, 3, "cinco", 1, 9]),
    ]

    for nombre, datos in casos:
        print(f"\n{nombre}")
        print(f"Entrada: {datos}")

        resultado = ordenamiento_burbuja(datos)

        if resultado is not None:
            print(f"Lista ordenada: {resultado}")
        else:
            print("No se realizó el ordenamiento.")


if __name__ == "__main__":
    main()