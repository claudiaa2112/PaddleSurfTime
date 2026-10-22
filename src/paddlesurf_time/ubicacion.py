from dataclasses import dataclass

LATITUD_MAXIMA = 90
LONGITUD_MAXIMA = 180


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


@dataclass(frozen=True, kw_only=True)
class Ubicacion:
    latitud: float
    longitud: float

    def __post_init__(self) -> None:
        if not (-LATITUD_MAXIMA <= self.latitud <= LATITUD_MAXIMA):
            raise LatitudFueraDeRangoError(self.latitud)
        if not (-LONGITUD_MAXIMA <= self.longitud <= LONGITUD_MAXIMA):
            raise LongitudFueraDeRangoError(self.longitud)
