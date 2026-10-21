class Programa:
    def __init__(self, nombre, dominio, certificacion):
        self.nombre = nombre
        self.dominio = dominio
        self.certificacion = certificacion

    def mostrar_informacion(self):
        print(f"Programa: {self.nombre}")
        print(f"Dominio: {self.dominio}")
        print(
            "Certificación:",
            "Sí" if self.certificacion else "No"
        )
        print("-" * 35)
