class AnguloFueraDeRangoError(ValueError):
    """El ángulo no está entre 0 y 360 grados (#7)."""

    def __init__(self, grados: float) -> None:
        super().__init__(f"El ángulo debe estar entre 0 y 360 grados, no {grados}")
        self.grados = grados
