from dataclasses import dataclass

from paddlesurftime.excepciones import AnguloFueraDeRangoError

GRADOS_VUELTA_COMPLETA = 360


@dataclass(frozen=True)
class Angulo:
    grados: float

    def __post_init__(self) -> None:
        if not (0 <= self.grados <= GRADOS_VUELTA_COMPLETA):
            raise AnguloFueraDeRangoError(self.grados)
        if self.grados == GRADOS_VUELTA_COMPLETA:
            object.__setattr__(self, "grados", 0)
