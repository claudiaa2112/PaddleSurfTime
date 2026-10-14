from dataclasses import dataclass

from paddlesurftime.direccion_viento import DireccionViento
from paddlesurftime.fuerza_viento import FuerzaViento


@dataclass(frozen=True)
class Viento:
    fuerza: FuerzaViento
    direccion: DireccionViento
