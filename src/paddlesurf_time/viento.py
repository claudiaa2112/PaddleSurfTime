from dataclasses import dataclass

from paddlesurf_time.angulo import GRADOS_VUELTA_COMPLETA

FUERZA_VIENTO_MAXIMA_KMH = 500


class FuerzaVientoFueraDeRangoError(ValueError):
    def __init__(self, fuerza_kmh: float) -> None:
        super().__init__(
            f"La fuerza del viento debe estar entre 0 y {FUERZA_VIENTO_MAXIMA_KMH} "
            f"km/h, no {fuerza_kmh}"
        )
        self.fuerza_kmh = fuerza_kmh


class DireccionVientoFueraDeRangoError(ValueError):
    def __init__(self, direccion_grados: float) -> None:
        super().__init__(
            f"La dirección del viento debe estar entre 0 y {GRADOS_VUELTA_COMPLETA} "
            f"grados, no {direccion_grados}"
        )
        self.direccion_grados = direccion_grados


@dataclass(frozen=True, kw_only=True)
class Viento:
    fuerza_kmh: float
    direccion_grados: float

    def __post_init__(self) -> None:
        if not (0 <= self.fuerza_kmh <= FUERZA_VIENTO_MAXIMA_KMH):
            raise FuerzaVientoFueraDeRangoError(self.fuerza_kmh)
        if not (0 <= self.direccion_grados <= GRADOS_VUELTA_COMPLETA):
            raise DireccionVientoFueraDeRangoError(self.direccion_grados)
