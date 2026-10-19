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
        self._condiciones: dict[Momento, CondicionesMar] = {}
