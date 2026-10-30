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


@dataclass(frozen=True)
class CondicionesMar:
    momento: datetime
    viento: Viento
    altura_olas_metros: float
    bandera: Bandera | None

    def __post_init__(self) -> None:
        if not (0 <= self.altura_olas_metros <= ALTURA_OLAS_MAXIMA_METROS):
            raise AlturaOlasFueraDeRangoError(self.altura_olas_metros)
