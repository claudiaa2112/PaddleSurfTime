from dataclasses import dataclass

from paddlesurftime.angulo import Angulo


@dataclass(frozen=True)
class OrientacionPlaya:
    """Ángulo hacia el que mira la playa (#12)."""

    angulo: Angulo
