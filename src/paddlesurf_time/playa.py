from dataclasses import dataclass, field
from datetime import datetime

from paddlesurf_time.condiciones_mar import CondicionesMar
from paddlesurf_time.ubicacion import Ubicacion
from paddlesurf_time.viento import GRADOS_VUELTA_COMPLETA


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


@dataclass(kw_only=True, eq=False)
class Playa:
    nombre: str
    municipio: str
    ubicacion: Ubicacion
    orientacion_grados: float
    condiciones: dict[datetime, CondicionesMar] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.nombre.strip() == "":
            raise NombrePlayaVacioError()
        if self.municipio.strip() == "":
            raise MunicipioVacioError()
        if not (0 <= self.orientacion_grados <= GRADOS_VUELTA_COMPLETA):
            raise OrientacionFueraDeRangoError(self.orientacion_grados)
