class Seleccion:
    def ordenamiento(self, lista):
        for i in range(len(lista) - 1):
            indice_menor = i

            for j in range(i + 1, len(lista)):
                if lista[j] < lista[indice_menor]:
                    indice_menor = j

            if indice_menor != i:
                lista[i], lista[indice_menor] = lista[indice_menor], lista[i]

        return lista