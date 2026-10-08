from dataclasses import dataclass

from paddlesurftime.excepciones import (
    LatitudFueraDeRangoError,
    LongitudFueraDeRangoError,
)

LATITUD_MAXIMA = 90
LONGITUD_MAXIMA = 180


@dataclass(frozen=True)
class Ubicacion:
    """Posición de una playa dada por su latitud y su longitud en grados (#8)."""

    latitud: float
    longitud: float

    def __post_init__(self) -> None:
        if not (-LATITUD_MAXIMA <= self.latitud <= LATITUD_MAXIMA):
            raise LatitudFueraDeRangoError(self.latitud)
        if not (-LONGITUD_MAXIMA <= self.longitud <= LONGITUD_MAXIMA):
            raise LongitudFueraDeRangoError(self.longitud)
