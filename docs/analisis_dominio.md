# Análisis del dominio

Este documento explica cómo se ha pasado de la [HU001](https://github.com/manupa16/PaddleSurfTime/issues/2) al código del Milestone 0, y al revés: de dónde sale cada parte del código.

Todas las decisiones que aparecen aquí se han consultado y consensuado con el propietario del repositorio, @manupa16, en los issues #6 a #18. En cada concepto se indica el issue donde se acordó.

## Cómo se ha hecho

- Se ha usado Domain Driven Design (DDD).
- Primero se han sacado de la HU001 las palabras que usa Pedro (el "lenguaje ubicuo"): playa, orientación, viento, olas, bandera, hora...
- Cada problema que plantean esas palabras se ha recogido en un issue, enlazado a la HU001 y revisado por el propietario antes de escribir código.
- Cada issue se ha resuelto en un commit que lo cierra.
- Al representar cada concepto se ha decidido si es:
  - un **objeto valor**: se define solo por su valor, no tiene identidad propia y no cambia una vez creado;
  - una **entidad**: tiene identidad propia y sigue siendo la misma aunque cambien sus datos;
  - un **agregado**: una entidad que agrupa otros objetos, a los que solo se accede a través de ella.

## De la HU001 al código

### Ángulo

- **En la HU:** "orientación en grados de 0 a 360 desde el norte en sentido horario" y "dirección desde la que sopla el viento (grados de 0 a 360, con el mismo criterio)".
- **Issue:** #7.
- **Es un objeto valor:** dos ángulos de 165° son el mismo y un ángulo no cambia.
- **Reglas:** entre 0 y 360; el 360 se guarda como 0 porque los dos son el norte.
- **Código:** `Angulo` en `src/paddlesurftime/angulo.py`. Si el valor no es válido lanza `AnguloFueraDeRangoError`.

### Ubicación

- **En la HU:** "ubicación, en latitud y longitud".
- **Issue:** #8.
- **Es un objeto valor:** dos ubicaciones con la misma latitud y longitud son la misma. Latitud y longitud van juntas porque por separado no sitúan nada.
- **Reglas:** latitud entre -90 y 90, longitud entre -180 y 180.
- **Código:** `Ubicacion` en `src/paddlesurftime/ubicacion.py`. Lanza `LatitudFueraDeRangoError` o `LongitudFueraDeRangoError`.

### Fuerza del viento

- **En la HU:** "fuerza del viento (km/h)".
- **Issue:** #9.
- **Es un objeto valor:** 12 km/h son siempre 12 km/h.
- **Reglas:** entre 0 y 500 km/h; 500 está por encima de la racha más fuerte registrada.
- **Código:** `FuerzaViento` en `src/paddlesurftime/fuerza_viento.py`. Lanza `FuerzaVientoFueraDeRangoError`.

### Altura de las olas

- **En la HU:** "altura de las olas (metros)".
- **Issue:** #10.
- **Es un objeto valor:** 0,4 metros son siempre 0,4 metros.
- **Reglas:** entre 0 (mar en calma) y 30 metros.
- **Código:** `AlturaOlas` en `src/paddlesurftime/altura_olas.py`. Lanza `AlturaOlasFueraDeRangoError`.

### Bandera

- **En la HU:** "bandera (verde, amarilla o roja)".
- **Issue:** #11.
- **Es un objeto valor:** solo existen esos tres colores y no cambian.
- **Reglas:** cualquier otro valor se rechaza.
- **Código:** `Bandera` en `src/paddlesurftime/bandera.py`. Con un color que no existe, Python lanza `ValueError`.

### Orientación de la playa y dirección del viento

- **En la HU:** "hacia donde mira la playa" y "dirección desde la que sopla el viento".
- **Issue:** #12.
- **Son dos objetos valor distintos:** se miden igual, con un ángulo, pero significan cosas distintas. Si fueran el mismo tipo se podría usar uno en lugar del otro sin que nada avisara, y más adelante se comparan entre sí.
- **Código:** `OrientacionPlaya` en `src/paddlesurftime/orientacion_playa.py` y `DireccionViento` en `src/paddlesurftime/direccion_viento.py`. Los dos contienen un `Angulo`, así que comparten su validación.

### Viento

- **En la HU:** "viento de 12km/h que viene desde 248°".
- **Issue:** #13.
- **Es un objeto valor:** la fuerza y la dirección siempre van juntas y por separado no describen el viento.
- **Reglas:** si la fuerza es 0 (calma), la dirección se guarda como 0°, porque no viene de ningún sitio.
- **Código:** `Viento` en `src/paddlesurftime/viento.py`, con la constante `DIRECCION_EN_CALMA`.

### Momento

- **En la HU:** "condiciones del mar a una hora concreta". Según el [user journey](user_journeys.md), Pedro consulta la noche anterior o al levantarse.
- **Issue:** #14.
- **Es un objeto valor:** el 8 de julio a las 9:00 es siempre el mismo momento.
- **Reglas:** un día y una hora en punto, porque solo con la hora no se distingue hoy de mañana.
- **Código:** `Momento` en `src/paddlesurftime/momento.py`. Lanza `MomentoNoEnPuntoError`.

### Condiciones del mar

- **En la HU:** "condiciones del mar a una hora concreta, fuerza del viento, dirección [...], altura de las olas y bandera".
- **Issue:** #16.
- **Es un objeto valor:** no se modifican; cuando llegan unas nuevas sustituyen enteras a las anteriores.
- **Reglas:** el viento, las olas y el momento son obligatorios; la bandera puede faltar porque no todas las zonas la publican.
- **Código:** `CondicionesMar` en `src/paddlesurftime/condiciones_mar.py`.

### Playa

- **En la HU:** "playa de Bolnuevo en Mazarrón" y "saber, antes de salir de casa, si la playa estará apta a la hora a la que llegue".
- **Issue:** #17.
- **Es una entidad:** se identifica por su nombre y su municipio, no por sus datos. Dos playas con el mismo nombre y municipio son la misma aunque cambie su ubicación. Además cambia con el tiempo, porque se le van guardando condiciones.
- **Es un agregado:** contiene sus condiciones del mar, que solo se guardan y consultan a través de la playa.
- **Reglas:** el nombre y el municipio no pueden estar vacíos; para cada momento solo hay unas condiciones y las nuevas sustituyen a las anteriores.
- **Interfaz:** sus datos son privados. Solo ofrece lo que necesita la HU001: guardar unas condiciones (`guardar_condiciones`) y consultar las de un momento (`condiciones_en`).
- **Código:** `Playa` en `src/paddlesurftime/playa.py`. Lanza `NombrePlayaVacioError` o `MunicipioVacioError`.

## Del código a la HU001

- `angulo.py` → #7 → "grados de 0 a 360 desde el norte".
- `ubicacion.py` → #8 → "ubicación, en latitud y longitud".
- `fuerza_viento.py` → #9 → "fuerza del viento (km/h)".
- `altura_olas.py` → #10 → "altura de las olas (metros)".
- `bandera.py` → #11 → "bandera (verde, amarilla o roja)".
- `orientacion_playa.py` y `direccion_viento.py` → #12 → "hacia donde mira la playa" y "desde la que sopla el viento".
- `viento.py` → #13 → "viento de 12km/h que viene desde 248°".
- `momento.py` → #14 → "a una hora concreta".
- `condiciones_mar.py` → #16 → "condiciones del mar".
- `playa.py` → #17 → "playa de Bolnuevo en Mazarrón".
- `excepciones.py` → cada excepción indica en su descripción el issue del que sale.

## El ejemplo de la HU001 en código

```python
bolnuevo = Playa(
    "Bolnuevo",
    "Mazarrón",
    Ubicacion(37.56, -1.30),
    OrientacionPlaya(Angulo(165)),
)
a_las_9 = Momento(datetime(2026, 7, 8, 9))
bolnuevo.guardar_condiciones(
    CondicionesMar(
        a_las_9,
        Viento(FuerzaViento(12), DireccionViento(Angulo(248))),
        AlturaOlas(0.4),
        Bandera.VERDE,
    )
)
```

La HU no da la latitud y longitud de Bolnuevo ni la fecha, así que en el ejemplo son aproximadas.
