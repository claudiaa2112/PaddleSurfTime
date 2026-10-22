from dataclasses import dataclass

from paddlesurf_time.direccion_viento import DireccionViento
from paddlesurf_time.fuerza_viento import FuerzaViento


@dataclass(frozen=True)
class Viento:
    fuerza: FuerzaViento
    direccion: DireccionViento
