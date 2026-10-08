from dataclasses import dataclass

from paddlesurftime.excepciones import AnguloFueraDeRangoError

GRADOS_VUELTA_COMPLETA = 360


@dataclass(frozen=True)
class Angulo:
    """Ángulo en grados, medido desde el norte en sentido horario (#7)."""

    grados: float

    def __post_init__(self) -> None:
        if not (0 <= self.grados <= GRADOS_VUELTA_COMPLETA):
            raise AnguloFueraDeRangoError(self.grados)
        if self.grados == GRADOS_VUELTA_COMPLETA:
            # La dataclass es inmutable, así que hay que usar object.__setattr__
            # para cambiar el valor mientras se está creando el objeto.
            object.__setattr__(self, "grados", 0)
