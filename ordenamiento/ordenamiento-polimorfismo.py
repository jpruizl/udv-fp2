from inserccion import Insercion
from burbuja import Burbuja
from seleccion import Seleccion


class Ordenamiento:
    def __init__(self, lista):
        self.lista = lista

    def ordenamiento(self, metodo):
        datos = self.lista.copy()
        resultado = metodo.ordenamiento(datos)
        print(f"{type(metodo).__name__}: {resultado}")


if __name__ == "__main__":
    datos = [5, 42, 36, 42, 40, 7, 11, 17, 23, 52]
    ordenador = Ordenamiento(datos)

    for metodo in (Insercion(), Burbuja(), Seleccion()):
        ordenador.ordenamiento(metodo)