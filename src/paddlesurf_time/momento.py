from dataclasses import dataclass
from datetime import datetime

from paddlesurf_time.excepciones import MomentoNoEnPuntoError


@dataclass(frozen=True)
class Momento:
    fecha_hora: datetime

    def __post_init__(self) -> None:
        if (
            self.fecha_hora.minute != 0
            or self.fecha_hora.second != 0
            or self.fecha_hora.microsecond != 0
        ):
            raise MomentoNoEnPuntoError(self.fecha_hora)
