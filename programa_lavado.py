from dataclasses import dataclass


@dataclass(frozen=True)
class ProgramaLavado:
    nombre: str
    minutos_lavado: int
    nivel_agua: int
    enjuagues: int
    velocidad_centrifugado: int
