class PlantaCarnivora:
    def __init__(self, especie, energia=40, nivel_agua=50):
        self.especie = especie
        self.energia = energia
        self.nivel_agua = nivel_agua
        self.trampa_abierta = True
        self.presas_digeridas = 0

    def regar(self, cantidad):
        self.nivel_agua = min(100, self.nivel_agua + cantidad)
        print(f"La planta recibió agua. Nivel actual: {self.nivel_agua}%.")

    def recibir_luz(self, horas):
        energia_generada = horas * 4
        self.energia = min(100, self.energia + energia_generada)
        print(f"La planta recibió {horas} horas de luz.")
        print(f"Energía actual: {self.energia}%.")

    def atraer_insecto(self):
        if self.trampa_abierta:
            print("Un insecto se acercó a la planta.")
            self.cerrar_trampa()
        else:
            print("La trampa está cerrada; no puede atraer otro insecto.")

    def cerrar_trampa(self):
        self.trampa_abierta = False
        print("¡La trampa se cerró!")

    def digerir(self):
        if not self.trampa_abierta:
            self.presas_digeridas += 1
            self.energia = min(100, self.energia + 25)
            self.trampa_abierta = True
            print("La planta digirió al insecto y volvió a abrir su trampa.")
            print(f"Energía actual: {self.energia}%.")
        else:
            print("No hay una presa en la trampa para digerir.")

    def mostrar_estado(self):
        estado_trampa = "abierta" if self.trampa_abierta else "cerrada"
        print("\n--- Estado de la planta ---")
        print(f"Especie: {self.especie}")
        print(f"Energía: {self.energia}%")
        print(f"Agua: {self.nivel_agua}%")
        print(f"Trampa: {estado_trampa}")
        print(f"Presas digeridas: {self.presas_digeridas}")


# Creación y uso del objeto
venus = PlantaCarnivora("Dionaea muscipula")

venus.mostrar_estado()
venus.regar(20)
venus.recibir_luz(3)
venus.atraer_insecto()
venus.digerir()
venus.mostrar_estado()
