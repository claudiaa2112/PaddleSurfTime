from dataclasses import dataclass

from paddlesurftime.excepciones import AlturaOlasFueraDeRangoError

ALTURA_OLAS_MAXIMA_METROS = 30


@dataclass(frozen=True)
class AlturaOlas:
    metros: float

    def __post_init__(self) -> None:
        if not (0 <= self.metros <= ALTURA_OLAS_MAXIMA_METROS):
            raise AlturaOlasFueraDeRangoError(self.metros)
