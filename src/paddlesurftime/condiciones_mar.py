from dataclasses import dataclass

from paddlesurftime.altura_olas import AlturaOlas
from paddlesurftime.bandera import Bandera
from paddlesurftime.momento import Momento
from paddlesurftime.viento import Viento


@dataclass(frozen=True)
class CondicionesMar:
    """Viento, olas y bandera de una playa en un momento concreto (#16)."""

    momento: Momento
    viento: Viento
    altura_olas: AlturaOlas
    bandera: Bandera | None
