# PaddleSurfTime

## Descripción del Problema

Soy un apasionado del deporte y este verano he empezado a practicar paddle surf. Durante estos meses me he ido moviendo por diversas playas de Málaga, Murcia y Granada, y mi problema es que en varias de ellas, pese a que hubiera bandera verde y el baño estuviera permitido, no podía practicarlo, ya que el mar no estaba en condiciones para hacerlo de forma óptima.

Esto se debía a que hacía viento, que daba lugar a pequeñas corrientes o incluso, muchas veces, a olas que, por muy pequeñas que fueran, imposibilitaban la práctica. Y todo esto no era previsible, ya que, pese a que podía consultar las banderas o el viento, eso no me confirmaba si era posible practicar paddle surf. Por eso, unas 10-15 veces no pude sacar la tabla y tuve que coger el coche hacia otro lugar a ver si encontraba una playa donde sí se pudiera, lo que me supuso una gran pérdida de tiempo y gasolina, además de un hartazgo increíble.

## Estado del Proyecto

El proyecto está en fase de planificación, están definidos los usuarios, historias de usuario y dos milestones.

## Planificación

- [User Journeys](docs/user_journeys.md): se incluyen los user journeys y su relación con las historias de usuario.
- [Personas](docs/personas.md): se incluyen los perfiles de usuario de los que salen las historias de usuario.
- [Historias de Usuario](docs/historias_de_usuario.md): se incluyen las historias de usuario del proyecto.
- [Milestones](docs/milestones.md): se incluyen los milestones.

## Documentación adicional

- [Lenguaje de programación](docs/lenguaje.md)
- [Fuentes de datos y heurística](docs/datos.md)
- [Juego de rol](docs/juego_de_rol.md)
- [Configuración del entorno](docs/entorno.md)

## Comprobación del código

- Python 3.14, la versión fijada en `.python-version`.
- Herramientas: ruff 0.16.10 (estilo, PEP 8) y mypy 2.4.0 (tipos).
- Desde la carpeta del proyecto:

```bash
python -m venv .venv
source .venv/bin/activate
pip install ruff==0.16.10 mypy==2.4.0
ruff check --select E,F,I,N,UP,B src
ruff format --check src
mypy --strict src/paddlesurftime
```



