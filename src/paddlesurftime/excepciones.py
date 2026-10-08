class AnguloFueraDeRangoError(ValueError):
    """El ángulo no está entre 0 y 360 grados (#7)."""

    def __init__(self, grados: float) -> None:
        super().__init__(f"El ángulo debe estar entre 0 y 360 grados, no {grados}")
        self.grados = grados


class LatitudFueraDeRangoError(ValueError):
    """La latitud no está entre -90 y 90 grados (#8)."""

    def __init__(self, latitud: float) -> None:
        super().__init__(f"La latitud debe estar entre -90 y 90 grados, no {latitud}")
        self.latitud = latitud


class LongitudFueraDeRangoError(ValueError):
    """La longitud no está entre -180 y 180 grados (#8)."""

    def __init__(self, longitud: float) -> None:
        super().__init__(
            f"La longitud debe estar entre -180 y 180 grados, no {longitud}"
        )
        self.longitud = longitud


class FuerzaVientoFueraDeRangoError(ValueError):
    """La fuerza del viento no está entre 0 y 500 km/h (#9)."""

    def __init__(self, kilometros_por_hora: float) -> None:
        super().__init__(
            "La fuerza del viento debe estar entre 0 y 500 km/h, "
            f"no {kilometros_por_hora}"
        )
        self.kilometros_por_hora = kilometros_por_hora
