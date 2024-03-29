import numpy

from piezas import *


class Tablero(object):

    def __init__(self):

        self.modo_control_tablero = False
        self.juego = 'iniciado'

        self.columna = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        self.fila = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

        # Defino una lista con las piezas y le paso los parametros: estadod e la pieza, si se encuentra promocionada,
        # Color del jugador asignado, letra que lo identifica en el tablero y en el caso del rey un bolleano que indica si esta en jaque
        self.t = [
            [Lancero(False, 'negro', 'L'), Caballo(False, 'negro', 'N'), GeneralPlata(False, 'negro', 'S'),
             GeneralOro('negro', 'G'), Rey('negro', 'K', False), GeneralOro('negro', 'G'),
             GeneralPlata(False, 'negro', 'S'), Caballo(False, 'negro', 'N'), Lancero(False, 'negro', 'L')],

            [None, Torre(False, 'negro', 'R'), None, None, None, None, None, Alfil(False, 'negro', 'B'), None],

            [Peon(False, 'negro', 'P'), Peon(False, 'negro', 'P'), Peon(False, 'negro', 'P'),
             Peon(False, 'negro', 'P'), Peon(False, 'negro', 'P'), Peon(False, 'negro', 'P'),
             Peon(False, 'negro', 'P'), Peon(False, 'negro', 'P'), Peon(False, 'negro', 'P')],

            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],

            [Peon(False, 'blanco', 'P'), Peon(False, 'blanco', 'P'), Peon(False, 'blanco', 'P'),
             Peon(False, 'blanco', 'P'), Peon(False, 'blanco', 'P'), Peon(False, 'blanco', 'P'),
             Peon(False, 'blanco', 'P'), Peon(False, 'blanco', 'P'), Peon(False, 'blanco', 'P')],

            [None, Alfil(False, 'blanco', 'B'), None, None, None, None, None, Torre(False, 'blanco', 'R'),
             None],

            [Lancero(False, 'blanco', 'L'), Caballo(False, 'blanco', 'N'),
             GeneralPlata(False, 'blanco', 'S'),
             GeneralOro('blanco', 'G'), Rey('blanco', 'K', False), GeneralOro('blanco', 'G'),
             GeneralPlata(False, 'blanco', 'S'), Caballo(False, 'blanco', 'N'),
             Lancero(False, 'blanco', 'L')],
        ]
        # Agrego las piezas al arreglo que va a representar mi tablero
        self.tab = numpy.array(self.t)
        # Defino la lsita donde se van a agregar las piezas muertas
        self.piezas_muertas = []

    def imprimir(self):
        k = 0
        print("|  ▼  |", end='')
        for k in range(len(self.columna)):
            print('  ' + self.columna[k] + '  |', end='')
        print("")
        k = 0
        for i in self.tab:
            print('|  ' + self.fila[k] + '  |', end='')
            for j in i:
                if j:
                    if j.color == 'negro':
                        if j.__class__ == GeneralOro or j.__class__ == Rey:
                            print(' ' + j.nombre, end='')
                            print(' ▼ |', end='')
                        else:
                            if j.promocion is True:
                                print(' ' + j.nombre, end='')
                                print('c▼ |', end='')
                            else:
                                print(' ' + j.nombre, end='')
                                print(' ▼ |', end='')
                    else:
                        if j.__class__ == GeneralOro or j.__class__ == Rey:
                            print(' ' + j.nombre, end='')
                            print(' ▲ |', end='')
                        else:
                            if j.promocion is True:
                                print(' ' + j.nombre, end='')
                                print('c▲ |', end='')
                            else:
                                print(' ' + j.nombre, end='')
                                print(' ▲ |', end='')

                else:
                    print('  -  |', end='')
            if k < 8:
                k += 1
            print('', end='\n')

    def verificar_promociones(self):
        for i in range(9):
            for j in range(9):
                if i < 3:
                    if self.tab[i][j]:
                        if self.tab[i][j].color == 'blanco':
                            if self.tab[i][j] == GeneralOro or self.tab[i][j] == Rey:
                                pass
                            else:
                                if self.tab[i][j].promocion is False:
                                    self.tab[i][j].promocion = True
                                    # print('pieza {} promocionada', self.tab[i][j].nombre)

                elif i > 5:
                    if self.tab[i][j]:
                        if self.tab[i][j].color and self.tab[i][j].color == 'negro':
                            if self.tab[i][j] == GeneralOro or self.tab[i][j] == Rey:
                                pass
                            else:
                                if self.tab[i][j].promocion is False:
                                    self.tab[i][j].promocion = True
                                    # print('pieza {} promocionada', self.tab[i][j].nombre)

    def mostrar_piezas_muertas(self, color):
        if self.piezas_muertas:
            p = 0
            for i in self.piezas_muertas:
                if i.color == color:
                    print(i.nombre)
                    p += 1
            if p > 0:
                return True
            else:
                return False

    def reintroducir_pieza(self, jugador, pieza_muerta, posicion_donde_incorporar, tablero):
        # Listo las piezas que el jugador a comido al adversario
        fila, columna = (int(item) for item in posicion_donde_incorporar.split())
        for i in self.piezas_muertas:
            # Verifico qie exista la pieza del color indicado
            if i.nombre == pieza_muerta and i.color == jugador.color:
                # verifico si es un peon
                if i.nombre == 'P':
                    if jugador.color == 'negro':
                        # El peon no se puede ingresar en la ultima fila
                        if fila != 8:
                            # El peon no se puede ingresar si en la misma fila hay otro peon del mismo color
                            for j in range(8):
                                if self.tab[fila + j][columna].__class__ == Peon and self.tab[fila + j][columna].color == 'negro':
                                    return False
                            # Ingreso la pieza para verificar en el paso siguiente si hay jaque
                            self.reintroducir(i, fila, columna)
                            # El peon no puede ingresar delante del rey si lo pone en jaque mate o si hay otro peon de ese color
                            if self.tab[fila - 1][columna].__class__ == Rey and jugador.verificar_jaque_mate(jugador, tablero) is False:
                                # La pieza ya se encuentra colocada, solo devuelvo true
                                return True
                            else:
                                # Si el peon deja en jaque mate al rey lo retiro y lo vuelvo a poner en la lista de piezas muertas
                                tablero.piezas_muertas.append(self.tab[fila][columna])
                                self.tab[fila][columna] = None
                                return False
                        else:
                            return False
                    elif jugador.color == 'blanco':
                        # El peon no se puede ingresar en la ultima fila
                        if fila != 0:
                            for j in range(8):
                                # El peon no se puede ingresar si en la misma fila hay otro peon del mismo color
                                if self.tab[fila + j][columna].__class__ == Peon and self.tab[fila + j][columna].color == 'blanco':
                                    return False
                            # Ingreso la pieza para verificar en el paso siguiente si hay jaque
                            self.reintroducir(i, fila, columna)
                            # El peon no se puede ingresar delante del rey si lo pone en jaque mate o si hay otro peon de ese color
                            if self.tab[fila + 1][columna].__class__ != Rey and jugador.verificar_jaque_mate(jugador, tablero) is False:
                                # La pieza ya se encuentra colocada, solo devuelvo true
                                return True
                            else:
                                # Si el peon deja en jaque mate al rey lo retiro y lo vuelvo a poner en la lista de piezas muertas
                                tablero.piezas_muertas.append(self.tab[fila][columna])
                                self.tab[fila][columna] = None
                                return False
                        else:
                            return False
                if i.nombre == 'L' or i.nombre == 'N':
                    if jugador.color == 'negro':
                        # El lancero o caballo no se puede ingresar en la ultima fila
                        if fila != 8:
                            return self.reintroducir(i, fila, columna)
                        else:
                            return False
                    elif jugador.color == 'blanco':
                        # El lancero o caballo no se puede ingresar en la ultima fila
                        if fila != 0:
                            return self.reintroducir(i, fila, columna)
                        else:
                            return False
                # Si es cualquier otra pieza, no tiene restricciones
                else:
                    return self.reintroducir(i, fila, columna)
        return False

    def reintroducir(self, pieza, fila, columna):
        if self.tab[fila][columna] is None:
            self.tab[fila][columna] = pieza
            self.piezas_muertas.remove(pieza)
            return True
        else:
            return False
