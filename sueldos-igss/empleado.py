from descuentos import Descuentos


class Empleado:

    def __init__(
        self,
        nombre,
        apellido,
        edad,
        telefono,
        correo,
        salario
    ):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.correo = correo

        self.descuentos = Descuentos(salario)

    def mostrar_informacion(self):
        print("\nINFORMACIÓN PERSONAL")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad} años")
        print(f"Teléfono: {self.telefono}")
        print(f"Correo: {self.correo}")

    def mostrar_reporte(self):
        self.mostrar_informacion()
        self.descuentos.mostrar_sueldo()