from paddlesurf_time.condiciones_mar import CondicionesMar
from paddlesurf_time.excepciones import MunicipioVacioError, NombrePlayaVacioError
from paddlesurf_time.momento import Momento
from paddlesurf_time.orientacion_playa import OrientacionPlaya
from paddlesurf_time.ubicacion import Ubicacion


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
