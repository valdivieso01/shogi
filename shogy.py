import numpy as np


class Tablero:

    def __init__(self):
        self.t = np.array([
            [Lancero('v', 'n', 'r', 'L', (0, 1)), Caballo('v', 'n', 'r', 'N', (0, 4)),
             GeneralPlata('v', 'n', 'r', 'S', (0, 4)),
             GeneralOro('v', 'n', 'r', 'G', (0, 4)), Rey('v', 'n', 'r', 'K', (0, 5)),
             GeneralOro('v', 'n', 'r', 'G', (0, 6)),
             GeneralPlata('v', 'n', 'r', 'S', (0, 7)), Caballo('v', 'n', 'r', 'N', (0, 8)),
             Lancero('v', 'n', 'r', 'L', (0, 9))],

            [None, Torre('v', 'n', 'r', 'R', (1, 1)), None, None, None, None, None, Alfil('v', 'n', 'r', 'B', (1, 7)),
             None],

            [Peon('v', 'n', 'r', 'P', (2, 0)), Peon('v', 'n', 'r', 'P', (2, 1)), Peon('v', 'n', 'r', 'P', (2, 2)),
             Peon('v', 'n', 'r', 'P', (2, 3)), Peon('v', 'n', 'r', 'P', (2, 4)), Peon('v', 'n', 'r', 'P', (2, 5)),
             Peon('v', 'n', 'r', 'P', (2, 6)), Peon('v', 'n', 'r', 'P', (2, 7)), Peon('v', 'n', 'r', 'P', (2, 8))],

        ])

    def devolver_nombre(self):
        for i in self.t:
            print(i)

    def __str__(self):
        return self.t


class Jugador:

    def __init__(self, color, piezas):
        self.color = color


class Pieza:

    def __init__(self, estado, promocion, nombre):
        self.estado = estado
        self.promocion = promocion


class Rey(Pieza):

    def __init__(self, estado, promocion, color, nombre, posicion):
        super().__init__(estado, promocion, nombre)  # Pongo super() para usar herencia sin self

        self.nombre = nombre
        self.posicion = posicion
        self.color = color

    def __str__(self):
        return self.nombre


class Lancero(Pieza):

    def __init__(self, estado, promocion, color, nombre, posicion):
        super().__init__(estado, promocion, nombre)  # Pongo super() para usar herencia sin self

        self.nombre = nombre
        self.posicion = posicion
        self.color = color


class Caballo(Pieza):

    def __init__(self, estado, promocion, color, nombre, posicion):
        super().__init__(estado, promocion, nombre)  # Pongo super() para usar herencia sin self

        self.nombre = nombre
        self.posicion = posicion
        self.color = color


class GeneralOro(Pieza):

    def __init__(self, estado, promocion, color, nombre, posicion):
        super().__init__(estado, promocion, nombre)  # Pongo super() para usar herencia sin self

        self.nombre = nombre
        self.posicion = posicion
        self.color = color


class GeneralPlata(Pieza):

    def __init__(self, estado, promocion, color, nombre, posicion):
        super().__init__(estado, promocion, nombre)  # Pongo super() para usar herencia sin self

        self.nombre = nombre
        self.posicion = posicion
        self.color = color


class Alfil(Pieza):

    def __init__(self, estado, promocion, color, nombre, posicion):
        super().__init__(estado, promocion, nombre)  # Pongo super() para usar herencia sin self

        self.nombre = nombre
        self.posicion = posicion
        self.color = color


class Torre(Pieza):

    def __init__(self, estado, promocion, color, nombre, posicion):
        super().__init__(estado, promocion, nombre)  # Pongo super() para usar herencia sin self

        self.nombre = nombre
        self.posicion = posicion
        self.color = color


class Peon(Pieza):

    def __init__(self, estado, promocion, color, nombre, posicion):
        super().__init__(estado, promocion, nombre)  # Pongo super() para usar herencia sin self

        self.nombre = nombre
        self.posicion = posicion
        self.color = color


j1 = Jugador('rojo', 'negro')
j2 = Jugador('negro', 'negro')
tablero = Tablero()
tablero.devolver_nombre()
