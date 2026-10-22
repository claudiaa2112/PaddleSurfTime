from dataclasses import dataclass

from paddlesurf_time.altura_olas import AlturaOlas
from paddlesurf_time.bandera import Bandera
from paddlesurf_time.momento import Momento
from paddlesurf_time.viento import Viento


@dataclass(frozen=True)
class CondicionesMar:
    momento: Momento
    viento: Viento
    altura_olas: AlturaOlas
    bandera: Bandera | None
