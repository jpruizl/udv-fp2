# Juan Pablo Ruiz Luna - 202103181
# 08 de septiembre del 2026
# Tarea - Abstracción y Herencia
# Objetivo: Practicar los conceptos de abstracción y herencia en Python.


# Parte 1 - Abstracción
from abc import ABC, abstractmethod

class DispositivoInteligente(ABC):
    @abstractmethod
    def conectar_red(self):
        pass

    @abstractmethod
    def mostrar_estado(self):
        pass


class RefrigeradorInteligente(DispositivoInteligente):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        self.conectado_wifi = False
        self.nombre_red = ""

    def encender(self):
        self.encendido = True
        print(f"El refrigerador {self.marca} {self.modelo} ha sido encendido.")

    def conectar_red(self):
        if not self.encendido:
            print("Primero debe encender el refrigerador.")
            return

        self.nombre_red = input("Ingrese el nombre de la red WiFi: ")
        clave = input("Ingrese la contraseña de la red: ")

        if self.nombre_red and clave:
            self.conectado_wifi = True
            print("Conexión a la red realizada correctamente.")
        else:
            print("No fue posible conectar a la red.")

    def mostrar_estado(self):
        print("\n--- Estado del Refrigerador Inteligente ---")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Encendido: {'Sí' if self.encendido else 'No'}")
        print(f"Conectado a WiFi: {'Sí' if self.conectado_wifi else 'No'}")
        if self.conectado_wifi:
            print(f"Red conectada: {self.nombre_red}")


# Programa principal
refrigerador = RefrigeradorInteligente("Samsung", "FamilyHub")
refrigerador.encender()
refrigerador.conectar_red()
refrigerador.mostrar_estado()



