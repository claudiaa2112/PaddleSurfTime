from dataclasses import dataclass

from paddlesurftime.angulo import Angulo
from paddlesurftime.direccion_viento import DireccionViento
from paddlesurftime.fuerza_viento import FuerzaViento

DIRECCION_EN_CALMA = DireccionViento(Angulo(0))


@dataclass(frozen=True)
class Viento:
    """Fuerza del viento junto con la dirección desde la que sopla (#13)."""

    fuerza: FuerzaViento
    direccion: DireccionViento

    def __post_init__(self) -> None:
        if self.fuerza.kilometros_por_hora == 0:
            # La dataclass es inmutable, así que hay que usar object.__setattr__
            # para cambiar el valor mientras se está creando el objeto.
            object.__setattr__(self, "direccion", DIRECCION_EN_CALMA)
