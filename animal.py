class Animal:
    def __init__(self,tipoAnimal):
        self.tipoAnimal = tipoAnimal

    def comer(self):
        print(f"El {self.tipoAnimal} esta comiendo")


class Gato(Animal):
    def maullar(self):
        print(f"El gato hace miau")


# Programa Principal
if __name__ == "__main__":
    MiGato = Gato("felino")
    MiGato.comer()
    MiGato.maullar()
