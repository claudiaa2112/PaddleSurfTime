from datetime import datetime

from paddlesurf_time.angulo import GRADOS_VUELTA_COMPLETA
from paddlesurf_time.condiciones_mar import CondicionesMar
from paddlesurf_time.ubicacion import Ubicacion


class NombrePlayaVacioError(ValueError):
    def __init__(self) -> None:
        super().__init__("El nombre de la playa no puede estar vacío")


class MunicipioVacioError(ValueError):
    def __init__(self) -> None:
        super().__init__("El municipio de la playa no puede estar vacío")


class OrientacionFueraDeRangoError(ValueError):
    def __init__(self, orientacion_grados: float) -> None:
        super().__init__(
            "La orientación de la playa debe estar entre 0 y "
            f"{GRADOS_VUELTA_COMPLETA} grados, no {orientacion_grados}"
        )
        self.orientacion_grados = orientacion_grados


class Playa:
    def __init__(
        self,
        nombre: str,
        municipio: str,
        ubicacion: Ubicacion,
        orientacion_grados: float,
    ) -> None:
        if nombre.strip() == "":
            raise NombrePlayaVacioError()
        if municipio.strip() == "":
            raise MunicipioVacioError()
        if not (0 <= orientacion_grados <= GRADOS_VUELTA_COMPLETA):
            raise OrientacionFueraDeRangoError(orientacion_grados)
        self._nombre = nombre
        self._municipio = municipio
        self._ubicacion = ubicacion
        self._orientacion_grados = orientacion_grados
        self._condiciones: dict[datetime, CondicionesMar] = {}
