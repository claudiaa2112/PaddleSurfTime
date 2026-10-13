from dataclasses import dataclass

from paddlesurftime.angulo import Angulo


@dataclass(frozen=True)
class OrientacionPlaya:
    angulo: Angulo
