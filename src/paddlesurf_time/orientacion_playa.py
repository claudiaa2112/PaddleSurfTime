from dataclasses import dataclass

from paddlesurf_time.angulo import Angulo


@dataclass(frozen=True)
class OrientacionPlaya:
    angulo: Angulo
