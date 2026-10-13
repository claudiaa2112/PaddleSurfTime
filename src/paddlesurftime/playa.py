from paddlesurftime.condiciones_mar import CondicionesMar
from paddlesurftime.excepciones import MunicipioVacioError, NombrePlayaVacioError
from paddlesurftime.momento import Momento
from paddlesurftime.orientacion_playa import OrientacionPlaya
from paddlesurftime.ubicacion import Ubicacion


class Playa:
    def __init__(
        self,
        nombre: str,
        municipio: str,
        ubicacion: Ubicacion,
        orientacion: OrientacionPlaya,
    ) -> None:
        if nombre.strip() == "":
            raise NombrePlayaVacioError()
        if municipio.strip() == "":
            raise MunicipioVacioError()
        self._nombre = nombre
        self._municipio = municipio
        self._ubicacion = ubicacion
        self._orientacion = orientacion
        self._condiciones: list[CondicionesMar] = []

    def __eq__(self, otra: object) -> bool:
        if not isinstance(otra, Playa):
            return False
        return self._nombre == otra._nombre and self._municipio == otra._municipio

    def guardar_condiciones(self, condiciones: CondicionesMar) -> None:
        for i, guardadas in enumerate(self._condiciones):
            if guardadas.momento == condiciones.momento:
                self._condiciones[i] = condiciones
                return
        self._condiciones.append(condiciones)

    def condiciones_en(self, momento: Momento) -> CondicionesMar | None:
        for condiciones in self._condiciones:
            if condiciones.momento == momento:
                return condiciones
        return None
