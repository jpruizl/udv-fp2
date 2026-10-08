import abc
import random


# ==========================================================
# CLASE ABSTRACTA: PERSONAJE
# ==========================================================

class Personaje(metaclass=abc.ABCMeta):
    """Contrato común para todos los personajes."""

    def __init__(self, nombre, vida):
        if not nombre.strip():
            raise ValueError("El personaje debe tener un nombre.")

        if vida <= 0:
            raise ValueError("La vida inicial debe ser mayor que cero.")

        self.nombre = nombre
        self.vida_maxima = vida
        self._vida = vida

    @property
    def vida(self):
        return self._vida

    @abc.abstractmethod
    def atacar(self, enemigo):
        """Cada personaje debe implementar su ataque básico."""
        pass

    @abc.abstractmethod
    def habilidad_especial(self, enemigo):
        """Cada personaje debe implementar su habilidad especial."""
        pass

    @abc.abstractmethod
    def describir(self):
        """Cada personaje debe describir sus características."""
        pass

    def recibir_danio(self, cantidad):
        """Método concreto compartido por los personajes."""
        if cantidad < 0:
            raise ValueError("El daño no puede ser negativo.")

        self._vida = max(0, self._vida - cantidad)

        print(
            f"{self.nombre} recibe {cantidad} puntos de daño. "
            f"Vida restante: {self.vida}/{self.vida_maxima}"
        )

    def esta_vivo(self):
        return self.vida > 0

    def mostrar_estado(self):
        print(
            f"{self.nombre} | {type(self).__name__} | "
            f"Vida: {self.vida}/{self.vida_maxima}"
        )


# ==========================================================
# CLASE CONCRETA: GUERRERO
# ==========================================================

class Guerrero(Personaje):
    """Implementa el contrato definido por Personaje."""

    def __init__(self, nombre):
        super().__init__(nombre, vida=100)
        self.fuerza = 8
        self.golpes_poderosos = 2

    def atacar(self, enemigo):
        dado = random.randint(1, 12)
        danio = dado + self.fuerza

        print(f"\n{self.nombre} ataca con su espada.")
        print(f"Daño: dado {dado} + fuerza {self.fuerza} = {danio}")

        enemigo.recibir_danio(danio)

    def habilidad_especial(self, enemigo):
        if self.golpes_poderosos == 0:
            print("\nSin golpes poderosos disponibles. Usa un ataque básico.")
            self.atacar(enemigo)
            return

        self.golpes_poderosos -= 1
        dado = random.randint(1, 12)
        danio = dado + self.fuerza + 12

        print(f"\n{self.nombre} utiliza GOLPE PODEROSO.")
        print(f"Usos restantes: {self.golpes_poderosos}")

        enemigo.recibir_danio(danio)

    def describir(self):
        return (
            f"Guerrero {self.nombre}: especialista en combate cuerpo a cuerpo. "
            f"Fuerza: {self.fuerza}. "
            f"Golpes poderosos: {self.golpes_poderosos}."
        )


# ==========================================================
# CLASE CONCRETA: MAGO
# ==========================================================

class Mago(Personaje):
    """Implementa ataques y habilidades basados en magia."""

    def __init__(self, nombre):
        super().__init__(nombre, vida=80)
        self.inteligencia = 10
        self.mana = 30

    def atacar(self, enemigo):
        dado = random.randint(1, 10)
        danio = dado + self.inteligencia

        print(f"\n{self.nombre} lanza un proyectil arcano.")
        print(
            f"Daño: dado {dado} + inteligencia "
            f"{self.inteligencia} = {danio}"
        )

        enemigo.recibir_danio(danio)

    def habilidad_especial(self, enemigo):
        costo = 10

        if self.mana < costo:
            print("\nManá insuficiente. Usa un ataque básico.")
            self.atacar(enemigo)
            return

        self.mana -= costo
        dado = random.randint(1, 20)
        danio = dado + self.inteligencia + 8

        print(f"\n{self.nombre} lanza BOLA DE FUEGO.")
        print(f"Maná restante: {self.mana}")

        enemigo.recibir_danio(danio)

    def describir(self):
        return (
            f"Mago {self.nombre}: especialista en ataques arcanos. "
            f"Inteligencia: {self.inteligencia}. Maná: {self.mana}."
        )


# ==========================================================
# CLASE ABSTRACTA: COMBATE
# ==========================================================

class Combate(metaclass=abc.ABCMeta):
    """Contrato para implementar diferentes modalidades de combate."""

    def __init__(self, personaje_1, personaje_2):
        if not isinstance(personaje_1, Personaje):
            raise TypeError("El primer participante debe ser un Personaje.")

        if not isinstance(personaje_2, Personaje):
            raise TypeError("El segundo participante debe ser un Personaje.")

        if personaje_1 is personaje_2:
            raise ValueError("Se requieren dos personajes diferentes.")

        if not personaje_1.esta_vivo() or not personaje_2.esta_vivo():
            raise ValueError("Ambos personajes deben estar vivos.")

        self.personaje_1 = personaje_1
        self.personaje_2 = personaje_2

    @abc.abstractmethod
    def iniciar(self):
        """Define cómo comienza y se desarrolla el combate."""
        pass

    @abc.abstractmethod
    def ejecutar_turno(self, atacante, defensor):
        """Define las acciones disponibles durante un turno."""
        pass

    @abc.abstractmethod
    def obtener_ganador(self):
        """Define cómo se determina el ganador."""
        pass


# ==========================================================
# CLASE CONCRETA: COMBATE POR TURNOS
# ==========================================================

class CombatePorTurnos(Combate):
    """Modalidad interactiva para dos participantes en una consola."""

    def ejecutar_turno(self, atacante, defensor):
        while True:
            print(f"\n--- Turno de {atacante.nombre} ---")
            print("1. Ataque básico")
            print("2. Habilidad especial")
            print("3. Consultar estado de ambos personajes")

            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                atacante.atacar(defensor)
                return

            if opcion == "2":
                atacante.habilidad_especial(defensor)
                return

            if opcion == "3":
                print()
                self.personaje_1.mostrar_estado()
                print(self.personaje_1.describir())

                self.personaje_2.mostrar_estado()
                print(self.personaje_2.describir())
                continue

            print("Opción inválida. Escribe 1, 2 o 3.")

    def obtener_ganador(self):
        primero_vivo = self.personaje_1.esta_vivo()
        segundo_vivo = self.personaje_2.esta_vivo()

        if primero_vivo and not segundo_vivo:
            return self.personaje_1

        if segundo_vivo and not primero_vivo:
            return self.personaje_2

        return None

    def iniciar(self):
        print("\n" + "=" * 55)
        print("COMBATE FANTÁSTICO POR TURNOS")
        print("=" * 55)

        print(self.personaje_1.describir())
        print(self.personaje_2.describir())

        # El primer turno se decide aleatoriamente.
        atacante, defensor = random.sample(
            [self.personaje_1, self.personaje_2], 2
        )

        numero_turno = 1

        while atacante.esta_vivo() and defensor.esta_vivo():
            print(f"\nTURNO {numero_turno}")
            self.ejecutar_turno(atacante, defensor)

            if not defensor.esta_vivo():
                break

            atacante, defensor = defensor, atacante
            numero_turno += 1

        ganador = self.obtener_ganador()

        if ganador is not None:
            print("\n" + "=" * 55)
            print(f"¡{ganador.nombre} gana el combate!")
            ganador.mostrar_estado()
            print("=" * 55)


# ==========================================================
# DEMOSTRACIÓN DE LAS RESTRICCIONES DE ABSTRACCIÓN
# ==========================================================

def demostrar_abstraccion():
    print("\n--- PRUEBAS DE CLASES ABSTRACTAS ---")

    try:
        Personaje("Personaje abstracto", 100)
    except TypeError as error:
        print("\n1. No se puede crear un Personaje abstracto:")
        print(error)

    guerrero = Guerrero("Guerrero de prueba")
    mago = Mago("Mago de prueba")

    try:
        Combate(guerrero, mago)
    except TypeError as error:
        print("\n2. No se puede crear un Combate abstracto:")
        print(error)

    class PersonajeIncompleto(Personaje):
        """Implementa solo uno de los tres métodos obligatorios."""

        def atacar(self, enemigo):
            enemigo.recibir_danio(5)

    try:
        PersonajeIncompleto("Aprendiz", 50)
    except TypeError as error:
        print("\n3. Una subclase incompleta tampoco se puede instanciar:")
        print(error)

    print("\n4. Las clases concretas sí permiten crear objetos:")
    print(guerrero.describir())
    print(mago.describir())


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

def main():
    print("DEMOSTRACIÓN DE abc.ABCMeta Y @abc.abstractmethod")

    demostrar_abstraccion()

    print("\n--- CREACIÓN DE LOS PERSONAJES ---")

    nombre_guerrero = input(
        "Nombre del guerrero [Arthas]: "
    ).strip() or "Arthas"

    nombre_mago = input(
        "Nombre del mago [Merlín]: "
    ).strip() or "Merlín"

    guerrero = Guerrero(nombre_guerrero)
    mago = Mago(nombre_mago)

    combate = CombatePorTurnos(guerrero, mago)
    combate.iniciar()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma finalizado por el usuario.")