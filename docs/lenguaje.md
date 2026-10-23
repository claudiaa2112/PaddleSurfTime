# Lenguaje de programación

Se ha elegido Python 3.14, acordado con @manupa16 en el issue #6. Estas son las razones, según lo que necesita el modelado de la HU001:

- **Comprobación de tipos:** Python permite indicar el tipo de cada dato y mypy lo comprueba antes de ejecutar. Así, por ejemplo, mypy avisa si a una playa se le pasa algo que no es una `Ubicacion`. Python no comprueba los tipos por sí solo al ejecutar, por eso se usa mypy en modo estricto.
- **Objetos que no cambian:** los objetos valor se han hecho con `dataclass(frozen=True)`, que impide modificarlos una vez creados.
- **Datos privados:** la entidad `Playa` guarda sus datos en atributos que empiezan por guion bajo, que es como Python indica que son privados, y no tiene ningún método para cambiarlos desde fuera.
- **Composición:** un objeto puede contener otros sin heredar de ellos. Por ejemplo, `CondicionesMar` contiene un `Viento`.
- **Excepciones:** Python tiene una jerarquía de excepciones estándar. Las del dominio heredan de `ValueError`, que es la que indica que un valor no es correcto.
- **Conjuntos cerrados de valores:** `Enum` permite representar la bandera con solo sus tres colores.
- **Versión:** Python 3.14, que se instala en el espacio de usuario con un gestor de versiones (pyenv).
- **Estilo:** ruff comprueba que el código sigue PEP 8, la guía de estilo de Python.
- **Lo conocemos los dos:** tanto el propietario como quien ha desarrollado este milestone pueden trabajar con él.
