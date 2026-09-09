# Clase padre
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo.")

    def dormir(self):
        print(f"{self.nombre} está durmiendo.")

    def desplazarse(self):
        print(f"{self.nombre} se está desplazando.")


# Subclases intermedias
class Vertebrado(Animal):
    def respirar(self):
        print(f"{self.nombre} respira por medio de su sistema respiratorio.")

    def tener_columna(self):
        print(f"{self.nombre} pertenece al grupo de los vertebrados.")


class Invertebrado(Animal):
    def moverse(self):
        print(f"{self.nombre} se mueve de acuerdo con su especie.")

    def no_tener_columna(self):
        print(f"{self.nombre} pertenece al grupo de los invertebrados.")


# Hijas de Vertebrado
class Mamifero(Vertebrado):
    def amamantar(self):
        print(f"{self.nombre} alimenta a sus crías con leche.")

class Ave(Vertebrado):
    def volar(self):
        print(f"{self.nombre} está volando.")

class Pez(Vertebrado):
    def nadar(self):
        print(f"{self.nombre} está nadando.")


# Hijas de Invertebrado
class Insecto(Invertebrado):
    def volar(self):
        print(f"{self.nombre} vuela usando sus alas.")

class Aracnido(Invertebrado):
    def caminar(self):
        print(f"{self.nombre} camina usando sus ocho patas.")

class Molusco(Invertebrado):
    def protegerse(self):
        print(f"{self.nombre} se protege con su cuerpo blando o concha.")


# Crear objetos
mamifero = Mamifero("Perro")
ave = Ave("Águila")
pez = Pez("Salmón")
insecto = Insecto("Mariposa")
aracnido = Aracnido("Araña")
molusco = Molusco("Caracol")


# Probar métodos heredados y propios
print("=== MAMÍFERO ===")
mamifero.comer()
mamifero.dormir()
mamifero.respirar()
mamifero.tener_columna()
mamifero.amamantar()

print("\n=== AVE ===")
ave.comer()
ave.desplazarse()
ave.respirar()
ave.volar()

print("\n=== PEZ ===")
pez.comer()
pez.dormir()
pez.tener_columna()
pez.nadar()

print("\n=== INSECTO ===")
insecto.comer()
insecto.moverse()
insecto.no_tener_columna()
insecto.volar()

print("\n=== ARÁCNIDO ===")
aracnido.comer()
aracnido.dormir()
aracnido.moverse()
aracnido.caminar()

print("\n=== MOLUSCO ===")
molusco.comer()
molusco.no_tener_columna()
molusco.moverse()
molusco.protegerse()