class Burbuja:
    def ordenamiento(self, lista):
        for limite in range(len(lista) - 1, 0, -1):
            for j in range(limite):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

        return lista