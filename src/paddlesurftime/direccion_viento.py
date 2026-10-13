from dataclasses import dataclass

from paddlesurftime.angulo import Angulo


@dataclass(frozen=True)
class DireccionViento:
    angulo: Angulo
