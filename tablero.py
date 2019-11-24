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
                print('No hay piezas para reincorporar')
                return False

    def incorporar_piezas(self, color, pieza_muerta):
        global i
        print("Piezas capturadas")
        # Listo las piezas que el jugador a comido al adversario
        for i in self.piezas_muertas:
            if i.nombre == pieza_muerta:
                for i in self.piezas_muertas:
                    if i.color == color:
                        if i.nombre == pieza_muerta:
                            posicion_donde_incorporar = input("Ingrese fila y columna de la posicion donde desea reincorporar (Separados por un espacio):")
                            fila, columna = (int(item) for item in posicion_donde_incorporar.split())
                            if self.tab[fila][columna] is None:
                                self.tab[fila][columna] = i
                                self.piezas_muertas.remove(i)
                                return True
                            else:
                                print("La posicion está ocupada")
                                return False
                    else:
                        return False
            else:
                print("No existe la pieza elegida")
                return False
