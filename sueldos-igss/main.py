from decimal import Decimal, InvalidOperation
from empleado import Empleado


def solicitar_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto:
            return texto

        print("Este dato no puede quedar vacío.")


def solicitar_entero(mensaje, minimo):
    while True:
        try:
            numero = int(input(mensaje))

            if numero >= minimo:
                return numero

            print(f"Debe ingresar un número mayor o igual a {minimo}.")

        except ValueError:
            print("Ingrese un número entero válido.")


def solicitar_salario():
    while True:
        try:
            entrada = input(
                "Salario mensual en quetzales: "
            ).strip()

            salario = Decimal(entrada)

            if not salario.is_finite():
                print("Ingrese un salario válido.")
                continue

            if salario <= 0:
                print("El salario debe ser mayor que cero.")
                continue

            if salario != salario.quantize(Decimal("0.01")):
                print("Ingrese el salario con un máximo de dos decimales.")
                continue

            return salario

        except (InvalidOperation, ValueError):
            print(
                "Ingrese un monto válido, sin Q ni comas. "
                "Ejemplo: 4500.00"
            )


def main():
    empleados = []
    sueldos_empleados = []

    print("=" * 55)
    print("DIGITALIZACIONES CREATIVAS")
    print("CÁLCULO DE SUELDO DE EMPLEADOS")
    print("=" * 55)

    cantidad = solicitar_entero(
        "\n¿Cuántos empleados desea registrar? (mínimo 5): ",
        5
    )

    for numero in range(1, cantidad + 1):
        print("\n" + "-" * 55)
        print(f"REGISTRO DEL EMPLEADO {numero}")
        print("-" * 55)

        nombre = solicitar_texto("Nombre: ")
        apellido = solicitar_texto("Apellido: ")
        edad = solicitar_entero("Edad: ", 1)
        telefono = solicitar_texto("Teléfono: ")
        correo = solicitar_texto("Correo: ")
        salario = solicitar_salario()

        empleado = Empleado(
            nombre,
            apellido,
            edad,
            telefono,
            correo,
            salario
        )

        empleados.append(empleado)

        # Cada posición guarda los cuatro valores de un empleado.
        sueldos_empleados.append(
            empleado.descuentos.datos_sueldo.copy()
        )

        print("\nEmpleado registrado correctamente.")

    print("\n" + "=" * 55)
    print("REPORTE DE EMPLEADOS")
    print("=" * 55)

    for numero, empleado in enumerate(empleados, start=1):
        print(f"\nEMPLEADO {numero}")
        empleado.mostrar_reporte()
        print("-" * 55)

    print("\nRESUMEN DE VALORES ALMACENADOS")
    print("=" * 55)

    for empleado, datos in zip(empleados, sueldos_empleados):
        print(
            f"{empleado.nombre} {empleado.apellido}: "
            f"[salario: {datos[0]:.2f}, "
            f"salario_con_descuento: {datos[1]:.2f}, "
            f"IGSS: {datos[2]:.2f}, "
            f"ISR: {datos[3]:.2f}]"
        )

    print(f"\nTotal de empleados registrados: {len(empleados)}")


if __name__ == "__main__":
    main()