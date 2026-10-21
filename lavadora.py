"""Simulador de Lavadora Automática modularizado por clases."""

from estado import Estado
from programa_lavado import ProgramaLavado
from componentes import (
    Puerta,
    Motor,
    Tambor,
    TransmisionPoleas,
    SensorNivel,
    SensorCarga,
    ValvulaEntrada,
    BombaDrenaje,
    PanelControl,
)
from controlador_lavado import ControladorLavado


class Lavadora:
    PROGRAMAS = {
        "1": ProgramaLavado("Rápido", 15, 40, 1, 800),
        "2": ProgramaLavado("Normal", 40, 60, 2, 1000),
        "3": ProgramaLavado("Delicado", 25, 50, 2, 600),
    }

    def __init__(self):
        self.estado = Estado.LISTA
        self.programa = None
        self.puerta = Puerta()
        self.motor = Motor()
        self.tambor = Tambor()
        self.transmision = TransmisionPoleas(self.motor, self.tambor)
        self.sensor_nivel = SensorNivel()
        self.sensor_carga = SensorCarga(self.tambor)
        self.valvula = ValvulaEntrada()
        self.bomba = BombaDrenaje()
        self.panel = PanelControl()
        self.controlador = ControladorLavado(self)

    def comprobar_configuracion_permitida(self):
        if self.estado in (
            Estado.EJECUTANDO, Estado.PAUSADA, Estado.ERROR
        ):
            raise ValueError("Finaliza o cancela el ciclo antes de configurar.")

    def seleccionar_programa(self, opcion):
        self.comprobar_configuracion_permitida()
        if opcion not in self.PROGRAMAS:
            raise ValueError("Programa inexistente.")
        self.programa = self.PROGRAMAS[opcion]
        self.panel.mostrar(f"Programa seleccionado: {self.programa.nombre}.")

    def cargar_ropa(self, peso):
        self.comprobar_configuracion_permitida()
        if self.puerta.cerrada:
            raise ValueError("Abre la puerta para cargar ropa.")
        self.tambor.cargar(peso)
        self.sensor_carga.balanceada = True
        self.panel.mostrar(f"Carga registrada: {peso:.2f} kg.")

    def retirar_ropa(self):
        self.comprobar_configuracion_permitida()
        if self.puerta.cerrada:
            raise ValueError("Abre la puerta para retirar ropa.")
        self.tambor.descargar()
        self.panel.mostrar("Ropa retirada.")

    def mostrar_estado(self):
        programa = self.programa.nombre if self.programa else "Sin seleccionar"
        siguiente = "Ninguna"

        if self.estado in (Estado.EJECUTANDO, Estado.PAUSADA):
            siguiente = self.controlador.etapas[self.controlador.indice][0]

        print("\n" + "=" * 48)
        print(f"Estado:             {self.estado.value}")
        print(f"Programa:           {programa}")
        print(f"Última etapa:       {self.controlador.etapa_actual}")
        print(f"Siguiente etapa:    {siguiente}")
        print(f"Carga:              {self.tambor.peso_carga:.2f} kg")
        print(f"Nivel de agua:      {self.sensor_nivel.nivel}%")
        print(f"Velocidad tambor:   {self.tambor.velocidad} RPM")
        print(f"Puerta cerrada:     {self.puerta.cerrada}")
        print(f"Puerta bloqueada:   {self.puerta.bloqueada}")
        print(f"Carga balanceada:   {self.sensor_carga.balanceada}")
        print("=" * 48)


def mostrar_menu():
    print("""
========== SIMULADOR DE LAVADORA ==========
1. Seleccionar programa
2. Cargar ropa
3. Cerrar puerta
4. Abrir puerta
5. Iniciar ciclo
6. Avanzar una etapa
7. Ejecutar todas las etapas pendientes
8. Pausar
9. Reanudar
10. Cancelar
11. Consultar estado
12. Simular / corregir carga desbalanceada
13. Retirar ropa
0. Salir
""")


def main():
    lavadora = Lavadora()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        try:
            if opcion == "1":
                for clave, programa in Lavadora.PROGRAMAS.items():
                    print(
                        f"{clave}. {programa.nombre}: "
                        f"{programa.minutos_lavado} min de lavado, "
                        f"{programa.enjuagues} enjuague(s), "
                        f"{programa.velocidad_centrifugado} RPM"
                    )
                lavadora.seleccionar_programa(
                    input("Programa: ").strip()
                )

            elif opcion == "2":
                texto = input("Peso de la ropa en kg: ").replace(",", ".")
                lavadora.cargar_ropa(float(texto))

            elif opcion == "3":
                lavadora.puerta.cerrar()
                lavadora.panel.mostrar("Puerta cerrada.")

            elif opcion == "4":
                lavadora.puerta.abrir()
                lavadora.panel.mostrar("Puerta abierta.")

            elif opcion == "5":
                lavadora.controlador.iniciar()

            elif opcion == "6":
                lavadora.controlador.avanzar()

            elif opcion == "7":
                if lavadora.estado != Estado.EJECUTANDO:
                    raise ValueError("Inicia o reanuda el ciclo primero.")
                lavadora.controlador.ejecutar_completo()

            elif opcion == "8":
                lavadora.controlador.pausar()

            elif opcion == "9":
                lavadora.controlador.reanudar()

            elif opcion == "10":
                lavadora.controlador.cancelar()

            elif opcion == "11":
                lavadora.mostrar_estado()

            elif opcion == "12":
                sensor = lavadora.sensor_carga
                sensor.balanceada = not sensor.balanceada
                lavadora.panel.mostrar(
                    f"Carga balanceada: {sensor.balanceada}."
                )

            elif opcion == "13":
                lavadora.retirar_ropa()

            elif opcion == "0":
                if lavadora.estado in (
                    Estado.EJECUTANDO, Estado.PAUSADA, Estado.ERROR
                ):
                    lavadora.controlador.cancelar()
                print("Simulador cerrado.")
                break

            else:
                print("Opción no válida.")

        except ValueError as error:
            print(f"\n[AVISO] {error}")


if __name__ == "__main__":
    main()