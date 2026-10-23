from dataclasses import dataclass
from datetime import datetime

from paddlesurf_time.bandera import Bandera
from paddlesurf_time.viento import Viento

ALTURA_OLAS_MAXIMA_METROS = 10


class AlturaOlasFueraDeRangoError(ValueError):
    def __init__(self, altura_olas_metros: float) -> None:
        super().__init__(
            "La altura de las olas debe estar entre 0 y "
            f"{ALTURA_OLAS_MAXIMA_METROS} metros, no {altura_olas_metros}"
        )
        self.altura_olas_metros = altura_olas_metros


class MomentoNoEnPuntoError(ValueError):
    def __init__(self, momento: datetime) -> None:
        super().__init__(f"El momento debe ser una hora en punto, no {momento}")
        self.momento = momento


@dataclass(frozen=True)
class CondicionesMar:
    momento: datetime
    viento: Viento
    altura_olas_metros: float
    bandera: Bandera | None

    def __post_init__(self) -> None:
        if (
            self.momento.minute != 0
            or self.momento.second != 0
            or self.momento.microsecond != 0
        ):
            raise MomentoNoEnPuntoError(self.momento)
        if not (0 <= self.altura_olas_metros <= ALTURA_OLAS_MAXIMA_METROS):
            raise AlturaOlasFueraDeRangoError(self.altura_olas_metros)
