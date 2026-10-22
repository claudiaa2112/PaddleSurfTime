from dataclasses import dataclass

from paddlesurf_time.excepciones import FuerzaVientoFueraDeRangoError

FUERZA_VIENTO_MAXIMA_KMH = 500


@dataclass(frozen=True)
class FuerzaViento:
    kilometros_por_hora: float

    def __post_init__(self) -> None:
        if not (0 <= self.kilometros_por_hora <= FUERZA_VIENTO_MAXIMA_KMH):
            raise FuerzaVientoFueraDeRangoError(self.kilometros_por_hora)
