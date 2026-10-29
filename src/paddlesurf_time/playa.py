from datetime import datetime

from paddlesurf_time.condiciones_mar import CondicionesMar
from paddlesurf_time.viento import GRADOS_VUELTA_COMPLETA

LATITUD_MAXIMA = 90
LONGITUD_MAXIMA = 180


class NombrePlayaVacioError(ValueError):
    def __init__(self) -> None:
        super().__init__("El nombre de la playa no puede estar vacío")


class MunicipioVacioError(ValueError):
    def __init__(self) -> None:
        super().__init__("El municipio de la playa no puede estar vacío")


class LatitudFueraDeRangoError(ValueError):
    def __init__(self, latitud: float) -> None:
        super().__init__(
            f"La latitud debe estar entre {-LATITUD_MAXIMA} y {LATITUD_MAXIMA} "
            f"grados, no {latitud}"
        )
        self.latitud = latitud


class LongitudFueraDeRangoError(ValueError):
    def __init__(self, longitud: float) -> None:
        super().__init__(
            f"La longitud debe estar entre {-LONGITUD_MAXIMA} y {LONGITUD_MAXIMA} "
            f"grados, no {longitud}"
        )
        self.longitud = longitud


class OrientacionFueraDeRangoError(ValueError):
    def __init__(self, orientacion_grados: int) -> None:
        super().__init__(
            "La orientación de la playa debe estar entre 0 y "
            f"{GRADOS_VUELTA_COMPLETA} grados, no {orientacion_grados}"
        )
        self.orientacion_grados = orientacion_grados


class Playa:
    def __init__(
        self,
        *,
        nombre: str,
        municipio: str,
        latitud: float,
        longitud: float,
        orientacion_grados: int,
    ) -> None:
        if nombre.strip() == "":
            raise NombrePlayaVacioError()
        if municipio.strip() == "":
            raise MunicipioVacioError()
        if not (-LATITUD_MAXIMA <= latitud <= LATITUD_MAXIMA):
            raise LatitudFueraDeRangoError(latitud)
        if not (-LONGITUD_MAXIMA <= longitud <= LONGITUD_MAXIMA):
            raise LongitudFueraDeRangoError(longitud)
        if not (0 <= orientacion_grados <= GRADOS_VUELTA_COMPLETA):
            raise OrientacionFueraDeRangoError(orientacion_grados)
        self._nombre = nombre
        self._municipio = municipio
        self._latitud = latitud
        self._longitud = longitud
        self._orientacion_grados = orientacion_grados
        self._condiciones: dict[datetime, CondicionesMar] = {}
