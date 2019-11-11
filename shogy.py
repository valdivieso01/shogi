class Tablero:

    def __init__(self):

        self.juego = 'iniciado'

        self.t = [
            [Lancero('v', 'n', 'r', 'L', (0, 1)), Caballo('v', 'n', 'r', 'N', (0, 4)),
             GeneralPlata('v', 'n', 'r', 'S', (0, 4)),
             GeneralOro('v', 'n', 'r', 'G', (0, 4)), Rey('v', 'n', 'r', 'K', (0, 5), False),
             GeneralOro('v', 'n', 'r', 'G', (0, 6)),
             GeneralPlata('v', 'n', 'r', 'S', (0, 7)), Caballo('v', 'n', 'r', 'N', (0, 8)),
             Lancero('v', 'n', 'r', 'L', (0, 9))],

            [None, Torre('v', 'n', 'r', 'R', (1, 1)), None, None, None, None, None, Alfil('v', 'n', 'r', 'B', (1, 7)), None,],

            [Peon('v', 'n', 'r', 'P', (2, 0)), Peon('v', 'n', 'r', 'P', (2, 1)), Peon('v', 'n', 'r', 'P', (2, 2)),
             Peon('v', 'n', 'r', 'P', (2, 3)), Peon('v', 'n', 'r', 'P', (2, 4)), Peon('v', 'n', 'r', 'P', (2, 5)),
             Peon('v', 'n', 'r', 'P', (2, 6)), Peon('v', 'n', 'r', 'P', (2, 7)), Peon('v', 'n', 'r', 'P', (2, 8))],

            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],

            [Peon('v', 'n', 'n', 'P', (2, 0)), Peon('v', 'n', 'n', 'P', (2, 1)), Peon('v', 'n', 'n', 'P', (2, 2)),
             Peon('v', 'n', 'n', 'P', (2, 3)), Peon('v', 'n', 'n', 'P', (2, 4)), Peon('v', 'n', 'n', 'P', (2, 5)),
             Peon('v', 'n', 'n', 'P', (2, 6)), Peon('v', 'n', 'n', 'P', (2, 7)), Peon('v', 'n', 'n', 'P', (2, 8))],

            [None, Alfil('v', 'n', 'n', 'B', (1, 7)), None, None, None, None, None, Torre('v', 'n', 'n', 'R', (1, 1)),
             None, ],

            [Lancero('v', 'n', 'n', 'L', (0, 1)), Caballo('v', 'n', 'n', 'N', (0, 4)),
             GeneralPlata('v', 'n', 'n', 'S', (0, 4)),
             GeneralOro('v', 'n', 'n', 'G', (0, 4)), Rey('v', 'n', 'n', 'K', (0, 5), False),
             GeneralOro('v', 'n', 'n', 'G', (0, 6)),
             GeneralPlata('v', 'n', 'n', 'S', (0, 7)), Caballo('v', 'n', 'n', 'N', (0, 8)),
             Lancero('v', 'n', 'n', 'L', (0, 9))],

        ]

    def __str__(self):
        return self.t


    def imprimir(self):
        columna = '| | |1| |2| |3| |4| |5| |6| |7| |8| |9|'
        fila = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        k = 0
        print(columna)
        for i in self.t:
            print('|'+fila[k]+'| ', end='')
            for j in i:
                if j:
                    print('|'+j.nombre+'| ', end='')
                else:
                    print('| | ', end='')
            k =+ 1
            print('', end='\n')


    def verificar_jaque_rojo(self):
        for i in self.t:
            for j in i:
                if j == Rey and j.color == 'r' and j.jaque == True:
                    return 'rey rojo en jaque'


    def verificar_jaque_negro(self):
        for i in self.t:
            for j in i:
                if j == Rey and j.color == 'n' and j.jaque == True:
                    return 'rey negro en jaque'


class Jugador:

    def __init__(self, color, piezas):
        self.color = color

    def hacer_jugada(self):
        pass


class Pieza:

    def __init__(self, estado, promocion, nombre):
        self.estado = estado
        self.promocion = promocion
        self.nombre = nombre

    def imprimir(self):
        return self.nombre


class Rey(Pieza):

    def __init__(self, estado, promocion, color, nombre, posicion, jaque):
        super().__init__(estado, promocion, nombre)  # Pongo super() para usar herencia sin self

        self.nombre = nombre
        self.posicion = posicion
        self.color = color
        self.color = jaque

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


def devolver_nombre(p):
    for i in p:
        print(i.nombre)


jugador_negro = Jugador('rojo', 'negro')
jugador_rojo = Jugador('negro', 'negro')
tablero = Tablero()

while tablero.juego != 'termiando':
    if tablero.verificar_jaque_negro():
        jugador_negro.hacer_jugada()
    tablero.imprimir()
    if tablero.verificar_jaque_rojo():
        jugador_rojo.hacer_jugada()
    tablero.imprimir()

