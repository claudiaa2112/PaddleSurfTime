from dataclasses import dataclass

from paddlesurf_time.angulo import Angulo


@dataclass(frozen=True)
class DireccionViento:
    angulo: Angulo
