from typing import TYPE_CHECKING
from estado import Estado

if TYPE_CHECKING:
    from lavadora import Lavadora


class ControladorLavado:
    def __init__(self, lavadora: "Lavadora"):
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
