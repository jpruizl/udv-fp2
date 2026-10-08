from dataclasses import dataclass
from enum import Enum


class Estado(Enum):
    LISTA = "Lista"
    EJECUTANDO = "En ejecución"
    PAUSADA = "Pausada"
    CANCELADA = "Cancelada"
    FINALIZADA = "Finalizada"
    ERROR = "En error"


@dataclass(frozen=True)
class ProgramaLavado:
    nombre: str
    minutos_lavado: int
    nivel_agua: int
    enjuagues: int
    velocidad_centrifugado: int


class Puerta:
    def __init__(self):
        self.cerrada = False
        self.bloqueada = False

    def cerrar(self):
        self.cerrada = True

    def abrir(self):
        if self.bloqueada:
            raise ValueError("La puerta está bloqueada.")
        self.cerrada = False

    def bloquear(self):
        if not self.cerrada:
            raise ValueError("No se puede bloquear una puerta abierta.")
        self.bloqueada = True

    def desbloquear(self):
        self.bloqueada = False


class Motor:
    def __init__(self):
        self.velocidad = 0
        self.sentido = "Detenido"

    def arrancar(self, velocidad, sentido="Horario"):
        if velocidad <= 0:
            raise ValueError("La velocidad debe ser mayor que cero.")
        self.velocidad = velocidad
        self.sentido = sentido

    def detener(self):
        self.velocidad = 0
        self.sentido = "Detenido"


class Tambor:
    def __init__(self, capacidad=8.0):
        self.capacidad = capacidad
        self.peso_carga = 0.0
        self.velocidad = 0

    def cargar(self, peso):
        if not 0 < peso <= self.capacidad:
            raise ValueError(
                f"La carga debe ser mayor que 0 y hasta {self.capacidad} kg."
            )
        self.peso_carga = peso

    def descargar(self):
        self.peso_carga = 0.0


class TransmisionPoleas:
    def __init__(self, motor, tambor):
        self.motor = motor
        self.tambor = tambor

    def transmitir(self):
        # Relación 1:1 simplificada para esta simulación.
        self.tambor.velocidad = self.motor.velocidad


class SensorNivel:
    def __init__(self):
        self.nivel = 0


class SensorCarga:
    def __init__(self, tambor):
        self.tambor = tambor
        self.balanceada = True

    def carga_valida(self):
        return 0 < self.tambor.peso_carga <= self.tambor.capacidad


class ValvulaEntrada:
    def __init__(self):
        self.abierta = False

    def llenar(self, sensor, objetivo):
        self.abierta = True
        sensor.nivel = objetivo
        self.abierta = False


class BombaDrenaje:
    def __init__(self):
        self.activa = False

    def drenar(self, sensor):
        self.activa = True
        sensor.nivel = 0
        self.activa = False


class PanelControl:
    @staticmethod
    def mostrar(mensaje):
        print(f"\n[LAVADORA] {mensaje}")


class ControladorLavado:
    def __init__(self, lavadora):
        self.lavadora = lavadora
        self.etapas = []
        self.indice = 0
        self.etapa_actual = "Sin iniciar"

    def iniciar(self):
        l = self.lavadora

        if l.estado in (Estado.EJECUTANDO, Estado.PAUSADA):
            raise ValueError("Ya existe un ciclo activo.")
        if l.programa is None:
            raise ValueError("Selecciona un programa primero.")
        if not l.puerta.cerrada:
            raise ValueError("Cierra la puerta antes de iniciar.")
        if not l.sensor_carga.carga_valida():
            raise ValueError("Carga ropa dentro de la capacidad permitida.")
        if l.sensor_nivel.nivel != 0:
            raise ValueError("El tambor debe estar vacío de agua al iniciar.")

        self.etapas = [
            ("Llenado inicial", self.llenar),
            ("Lavado", self.lavar),
            ("Drenaje del lavado", self.drenar),
        ]

        for numero in range(1, l.programa.enjuagues + 1):
            self.etapas.extend([
                (f"Llenado del enjuague {numero}", self.llenar),
                (f"Enjuague {numero}", self.enjuagar),
                (f"Drenaje del enjuague {numero}", self.drenar),
            ])

        self.etapas.extend([
            ("Centrifugado", self.centrifugar),
            ("Finalización", self.finalizar),
        ])

        self.indice = 0
        self.etapa_actual = "Inicio validado"
        l.puerta.bloquear()
        l.estado = Estado.EJECUTANDO
        l.panel.mostrar(f"Ciclo iniciado: {l.programa.nombre}.")

    def avanzar(self):
        l = self.lavadora

        if l.estado != Estado.EJECUTANDO:
            raise ValueError("El ciclo debe estar en ejecución para avanzar.")

        nombre, accion = self.etapas[self.indice]
        self.etapa_actual = nombre
        l.panel.mostrar(f"Etapa: {nombre}")

        try:
            accion()
        except ValueError as error:
            self.detener_componentes()
            l.estado = Estado.ERROR
            l.panel.mostrar(f"Error: {error}")
            l.panel.mostrar("Cancela el ciclo para drenar y liberar la puerta.")
            return

        self.indice += 1

    def ejecutar_completo(self):
        while self.lavadora.estado == Estado.EJECUTANDO:
            self.avanzar()

    def llenar(self):
        l = self.lavadora
        l.valvula.llenar(l.sensor_nivel, l.programa.nivel_agua)
        l.panel.mostrar(f"Nivel de agua: {l.sensor_nivel.nivel}%.")

    def mover_tambor(self, velocidad, sentido):
        l = self.lavadora

        if not l.puerta.bloqueada:
            raise ValueError("La puerta debe estar bloqueada.")

        l.motor.arrancar(velocidad, sentido)
        l.transmision.transmitir()
        l.panel.mostrar(
            f"Tambor girando a {l.tambor.velocidad} RPM. "
            f"Movimiento: {sentido}."
        )

        # Cada operación se completa instantáneamente en la simulación.
        l.motor.detener()
        l.transmision.transmitir()

    def lavar(self):
        l = self.lavadora
        if l.sensor_nivel.nivel < l.programa.nivel_agua:
            raise ValueError("Agua insuficiente para lavar.")

        self.mover_tambor(50, "Alternado")
        l.panel.mostrar(
            f"Lavado simulado: {l.programa.minutos_lavado} minutos."
        )

    def drenar(self):
        l = self.lavadora
        l.bomba.drenar(l.sensor_nivel)
        l.panel.mostrar("Drenaje completado. Nivel de agua: 0%.")

    def enjuagar(self):
        l = self.lavadora
        if l.sensor_nivel.nivel < l.programa.nivel_agua:
            raise ValueError("Agua insuficiente para enjuagar.")
        self.mover_tambor(40, "Alternado")

    def centrifugar(self):
        l = self.lavadora

        if l.sensor_nivel.nivel != 0:
            raise ValueError("Debe drenarse el agua antes de centrifugar.")
        if not l.sensor_carga.balanceada:
            raise ValueError("Carga desbalanceada: centrifugado suspendido.")

        self.mover_tambor(l.programa.velocidad_centrifugado, "Horario")

    def detener_componentes(self):
        l = self.lavadora
        l.motor.detener()
        l.transmision.transmitir()
        l.valvula.abierta = False
        l.bomba.activa = False

    def liberar_puerta(self):
        l = self.lavadora
        if l.tambor.velocidad != 0 or l.sensor_nivel.nivel != 0:
            raise ValueError("No se cumplen las condiciones de apertura.")
        l.puerta.desbloquear()

    def finalizar(self):
        self.detener_componentes()
        self.liberar_puerta()
        self.lavadora.estado = Estado.FINALIZADA
        self.lavadora.panel.mostrar(
            "¡Ciclo terminado! Puedes abrir la puerta y retirar la ropa."
        )

    def pausar(self):
        l = self.lavadora
        if l.estado != Estado.EJECUTANDO:
            raise ValueError("No existe un ciclo en ejecución.")
        self.detener_componentes()
        l.estado = Estado.PAUSADA
        l.panel.mostrar("Ciclo pausado. La puerta permanece bloqueada.")

    def reanudar(self):
        l = self.lavadora
        if l.estado != Estado.PAUSADA:
            raise ValueError("El ciclo no está pausado.")
        l.estado = Estado.EJECUTANDO
        l.panel.mostrar("Ciclo reanudado desde la siguiente etapa pendiente.")

    def cancelar(self):
        l = self.lavadora
        if l.estado not in (
            Estado.EJECUTANDO, Estado.PAUSADA, Estado.ERROR
        ):
            raise ValueError("No existe un ciclo activo para cancelar.")

        self.detener_componentes()
        self.drenar()
        self.liberar_puerta()
        l.estado = Estado.CANCELADA
        self.etapa_actual = "Cancelación"
        l.panel.mostrar("Ciclo cancelado. Puerta desbloqueada.")


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