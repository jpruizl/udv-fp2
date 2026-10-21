from enum import Enum


class Estado(Enum):
    LISTA = "Lista"
    EJECUTANDO = "En ejecución"
    PAUSADA = "Pausada"
    CANCELADA = "Cancelada"
    FINALIZADA = "Finalizada"
    ERROR = "En error"
