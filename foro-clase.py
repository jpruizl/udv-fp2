class Estudiante:
    # Atributos
    def __init__(self, nombre, carnet, carrera):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera

    def recibir_clase(self, asignatura):
        print(f"{self.nombre} está recibiendo la clase de {asignatura}.")

    def entregar_tarea(self, tarea):
        print(f"{self.nombre} entregó la tarea: {tarea}.")


# Crear el objeto estudiante
estudiante1 = Estudiante(
    "Juan Pablo Ruiz",
    "202103181",
    "Ingeniería en Sistemas"
)

# Utilizar los métodos
estudiante1.recibir_clase("Fundamentos de Programación II")
estudiante1.entregar_tarea("Práctica de clase y constructor")
