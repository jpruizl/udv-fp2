# Juan Pablo Ruiz Luna - 202103181
# 08 de septiembre del 2026
# Tarea - Herencia
# Objetivo: Practicar los conceptos de herencia en Python.

# Parte 2 - Herencia
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo.")

    def correr(self):
        print(f"{self.nombre} está corriendo.")


class Leon(Animal):
    def rugir(self):
        print(f"{self.nombre} está rugiendo fuertemente.")


class Elefante(Animal):
    def trompetear(self):
        print(f"{self.nombre} está emitiendo un sonido con la trompa.")


# Programa principal
leon = Leon("Simba")
elefante = Elefante("Dumbo")

print("--- Acciones del León ---")
leon.comer()
leon.correr()
leon.rugir()

print("\n--- Acciones del Elefante ---")
elefante.comer()
elefante.correr()
elefante.trompetear()