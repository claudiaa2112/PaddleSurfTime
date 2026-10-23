class AnguloFueraDeRangoError(ValueError):
    def __init__(self, grados: float) -> None:
        super().__init__(f"El ángulo debe estar entre 0 y 360 grados, no {grados}")
        self.grados = grados


class NombrePlayaVacioError(ValueError):
    def __init__(self) -> None:
        super().__init__("El nombre de la playa no puede estar vacío")


class MunicipioVacioError(ValueError):
    def __init__(self) -> None:
        super().__init__("El municipio de la playa no puede estar vacío")
