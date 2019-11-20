import numpy

from piezas import *


class Tablero(object):

    def __init__(self):

        self.juego = 'iniciado'

        self.columna = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        self.fila = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

        # Defino una lista con las piezas y le paso los parametros: estadod e la pieza, si se encuentra promocionada,
        # color del jugador asignado, letra que lo identifica en el tablero y en el caso del rey un bolleano que indica si esta en jaque
        self.t = [
            [Lancero('viva', False, 'negro', 'L'), Caballo('viva', False, 'negro', 'N'), GeneralPlata('viva', False, 'negro', 'S'),
             GeneralOro('viva', 'negro', 'G'), Rey('viva', 'negro', 'K', False), GeneralOro('viva', 'negro', 'G'),
             GeneralPlata('viva', False, 'negro', 'S'), Caballo('viva', False, 'negro', 'N'), Lancero('viva', False, 'negro', 'L')],

            [None, Torre('viva', False, 'negro', 'R'), None, None, None, None, None, Alfil('viva', False, 'negro', 'B'), None],

            [Peon('viva', False, 'negro', 'P'), Peon('viva', False, 'negro', 'P'), Peon('viva', False, 'negro', 'P'),
             Peon('viva', False, 'negro', 'P'), Peon('viva', False, 'negro', 'P'), Peon('viva', False, 'negro', 'P'),
             Peon('viva', False, 'negro', 'P'), Peon('viva', False, 'negro', 'P'), Peon('viva', False, 'negro', 'P')],

            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],

            [Peon('viva', False, 'blanco', 'P'), Peon('viva', False, 'blanco', 'P'), Peon('viva', False, 'blanco', 'P'),
             Peon('viva', False, 'blanco', 'P'), Peon('viva', False, 'blanco', 'P'), Peon('viva', False, 'blanco', 'P'),
             Peon('viva', False, 'blanco', 'P'), Peon('viva', False, 'blanco', 'P'), Peon('viva', False, 'blanco', 'P')],

            [None, Alfil('viva', False, 'blanco', 'B'), None, None, None, None, None, Torre('viva', False, 'blanco', 'R'),
             None],

            [Lancero('viva', False, 'blanco', 'L'), Caballo('viva', False, 'blanco', 'N'),
             GeneralPlata('viva', False, 'blanco', 'S'),
             GeneralOro('viva', 'blanco', 'G'), Rey('viva', 'blanco', 'K', False), GeneralOro('viva', 'blanco', 'G'),
             GeneralPlata('viva', False, 'blanco', 'S'), Caballo('viva', False, 'blanco', 'N'),
             Lancero('viva', False, 'blanco', 'L')],
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
                    if j.estado == 'viva':
                        if j.color == 'negro':
                            print(' ' + j.nombre, end='')
                            print(' ▼ |', end='')
                        else:
                            print(' ' + j.nombre, end='')
                            print(' ▲ |', end='')
                    else:
                        print('  -  |', end='')
                else:
                    print('  -  |', end='')
            if k < 8:
                k += 1
            print('', end='\n')

    def verificar_promociones(self):
        for i in range(9):
            for j in range(9):
                if i > 3:
                    if self.tab[i][j].color == 'blanco':
                        if self.tab[i][j].promocion is False:
                            self.tab[i][j].promocion = True
                            print('pieza {} promocionada',self.tab[i][j].nombre)
                        else:
                            print('Ninguna pieza fue promocionada')
                elif i > 5:
                    if self.tab[i][j].color == 'negro':
                        if self.tab[i][j].promocion is False:
                            self.tab[i][j].promocion = True
                            print('pieza {} promocionada',self.tab[i][j].nombre)
                        else:
                            print('Ninguna pieza fue promocionada')

    def verificar_jaque(self, color):
        for i in range(9):
            for j in range(9):
                if self.tab[i][j].__class__ == Rey and self.tab[i][j].color == color:
                    if self.tab[i][j].jaque is True:
                        return True
                    else:
                        return False

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
                            self.tab[fila][columna] = i
                            self.piezas_muertas.remove(i)
                    else:
                        return False
            else:
                print("No existe la pieza elegida")
                return False