from dataclasses import dataclass
from datetime import datetime

from paddlesurftime.excepciones import MomentoNoEnPuntoError


@dataclass(frozen=True)
class Momento:
    """Día y hora en punto a los que se refieren las condiciones del mar (#14)."""

    fecha_hora: datetime

    def __post_init__(self) -> None:
        if (
            self.fecha_hora.minute != 0
            or self.fecha_hora.second != 0
            or self.fecha_hora.microsecond != 0
        ):
            raise MomentoNoEnPuntoError(self.fecha_hora)
