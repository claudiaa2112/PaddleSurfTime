from dataclasses import dataclass

from paddlesurftime.angulo import Angulo
from paddlesurftime.direccion_viento import DireccionViento
from paddlesurftime.fuerza_viento import FuerzaViento

DIRECCION_EN_CALMA = DireccionViento(Angulo(0))


@dataclass(frozen=True)
class Viento:
    fuerza: FuerzaViento
    direccion: DireccionViento

    def __post_init__(self) -> None:
        if self.fuerza.kilometros_por_hora == 0:
            object.__setattr__(self, "direccion", DIRECCION_EN_CALMA)
