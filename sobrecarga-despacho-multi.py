from multipledispatch import dispatch


@dispatch(int, int)
def combinar(a, b):
    return f"Dos enteros: {a + b}"


@dispatch(float, float)
def combinar(a, b):
    return f"Dos decimales: {a + b}"


@dispatch(int, float)
def combinar(a, b):
    return f"Entero y decimal: {a + b}"


@dispatch(float, int)
def combinar(a, b):
    return f"Decimal y entero: {a + b}"


@dispatch(str, str)
def combinar(a, b):
    return f"Dos cadenas: {a + b}"


if __name__ == "__main__":
    print(combinar(10, 20))
    print(combinar(2.5, 3.5))
    print(combinar(10, 2.5))
    print(combinar(2.5, 10))
    print(combinar("Hola, ", "Python"))