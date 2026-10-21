from programa import Programa


def main():
    programas_permitidos = {
        "word": "Word",
        "excel": "Excel",
        "powerpoint": "PowerPoint",
        "access": "Access"
    }

    programas_registrados = []
    nombres_registrados = set()

    print("REGISTRO DE PROGRAMAS QUE DOMINA")
    print("Programas disponibles: Word, Excel, PowerPoint y Access")
    print("-" * 55)

    while True:
        try:
            cantidad = int(
                input("¿Cuántos programas desea registrar? (1 a 4): ")
            )

            if 1 <= cantidad <= 4:
                break

            print("Debe ingresar un número entre 1 y 4.")

        except ValueError:
            print("Ingrese un número entero válido.")

    for numero in range(1, cantidad + 1):
        print(f"\nRegistro del programa {numero}")

        while True:
            nombre_ingresado = input(
                "Nombre del programa: "
            ).strip().lower()

            if nombre_ingresado not in programas_permitidos:
                print("Ingrese Word, Excel, PowerPoint o Access.")

            elif nombre_ingresado in nombres_registrados:
                print("Este programa ya fue registrado.")

            else:
                nombre = programas_permitidos[nombre_ingresado]
                break

        while True:
            dominio = input(
                "Nivel de dominio (básico, intermedio o avanzado): "
            ).strip()

            if dominio:
                break

            print("El nivel de dominio no puede quedar vacío.")

        while True:
            respuesta = input(
                "¿Posee certificación? (1 = Sí, 0 = No): "
            ).strip()

            if respuesta in ("0", "1"):
                certificacion = respuesta == "1"
                break

            print("Ingrese únicamente 1 o 0.")

        programa = Programa(nombre, dominio, certificacion)

        programas_registrados.append(programa)
        nombres_registrados.add(nombre_ingresado)

        print("Programa registrado correctamente.")

    print("\n" + "=" * 35)
    print("INFORMACIÓN REGISTRADA")
    print("=" * 35)

    for programa in programas_registrados:
        programa.mostrar_informacion()


if __name__ == "__main__":
    main()