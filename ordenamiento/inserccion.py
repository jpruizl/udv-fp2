class Insercion:
    def ordenamiento(self, lista):
        for i in range(1, len(lista)):
            actual = lista[i]
            j = i - 1

            while j >= 0 and lista[j] > actual:
                lista[j + 1] = lista[j]
                j -= 1

            lista[j + 1] = actual

        return lista