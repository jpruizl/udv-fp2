from vehiculo import Vehiculo
from aereo import Aereo
from terrestre import Terrestre
from turbina import Turbina
from helice import Helice
from llantas import Llantas
from vias import Vias


def probar_acceso_privado(nombre_clase, objeto):
    """Intenta acceder directamente al método privado."""
    print(f"\nPRUEBA: objeto de la clase {nombre_clase}")
    print("Intento: objeto.__verificar_estado_general()")

    try:
        objeto.__verificar_estado_general()
    except AttributeError as error:
        print(f"Acceso directo no permitido: {error}")
    else:
        print("Resultado inesperado: se permitió el acceso directo.")


if __name__ == "__main__":
    print("=" * 65)
    print("PRUEBAS DE ACCESO DIRECTO AL MÉTODO PRIVADO")
    print("=" * 65)

    objetos = [
        ("Vehiculo", Vehiculo()),
        ("Aereo", Aereo()),
        ("Terrestre", Terrestre()),
        ("Turbina", Turbina()),
        ("Helice", Helice()),
        ("Llantas", Llantas()),
        ("Vias", Vias()),
    ]

    for nombre_clase, objeto in objetos:
        probar_acceso_privado(nombre_clase, objeto)

    print("\n" + "=" * 65)
    print("COMPROBACIÓN DE LOS MÉTODOS PÚBLICOS HEREDADOS")
    print("=" * 65)

    automovil = Llantas()
    automovil.avanzar()
    automovil.identificar_tipo("llantas")
    automovil.verificar_temperatura(10)
    automovil.encender_motor()