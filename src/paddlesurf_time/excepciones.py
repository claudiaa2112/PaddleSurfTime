from datetime import datetime


class AnguloFueraDeRangoError(ValueError):
    def __init__(self, grados: float) -> None:
        super().__init__(f"El ángulo debe estar entre 0 y 360 grados, no {grados}")
        self.grados = grados


class FuerzaVientoFueraDeRangoError(ValueError):
    def __init__(self, kilometros_por_hora: float) -> None:
        super().__init__(
            "La fuerza del viento debe estar entre 0 y 500 km/h, "
            f"no {kilometros_por_hora}"
        )
        self.kilometros_por_hora = kilometros_por_hora


class AlturaOlasFueraDeRangoError(ValueError):
    def __init__(self, metros: float) -> None:
        super().__init__(
            f"La altura de las olas debe estar entre 0 y 30 metros, no {metros}"
        )
        self.metros = metros


class MomentoNoEnPuntoError(ValueError):
    def __init__(self, fecha_hora: datetime) -> None:
        super().__init__(f"El momento debe ser una hora en punto, no {fecha_hora}")
        self.fecha_hora = fecha_hora


class NombrePlayaVacioError(ValueError):
    def __init__(self) -> None:
        super().__init__("El nombre de la playa no puede estar vacío")


class MunicipioVacioError(ValueError):
    def __init__(self) -> None:
        super().__init__("El municipio de la playa no puede estar vacío")
