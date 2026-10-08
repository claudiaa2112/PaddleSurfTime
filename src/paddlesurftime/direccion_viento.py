from dataclasses import dataclass

from paddlesurftime.angulo import Angulo


@dataclass(frozen=True)
class DireccionViento:
    """Ángulo desde el que sopla el viento (#12)."""

    angulo: Angulo
