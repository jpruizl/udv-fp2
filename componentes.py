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
