from piezas import *
from tablero import *


class Jugador(object):

    def __init__(self, color):
        self.color = color

    def imprimir(self):
        return self.color

    def validar_posiciones(self, x, y):
        if 9 > x >= 0 and 9 > y >= 0:
            return True
        else:
            return False

    def jugar_pieza(self, tablero, color_de_jugador, posicion_inicial, posicion_final):
        # Verifico si se selecciono una pieza
        if tablero.tab[posicion_inicial[0]][posicion_inicial[1]]:
            # Verifico si se selecciono una pieza del jugador correcto
            if tablero.tab[posicion_inicial[0]][posicion_inicial[1]].color == color_de_jugador:
                # Verifico que tipo de pieza es
                if tablero.tab[posicion_inicial[0]][posicion_inicial[1]].__class__ is Peon:
                    return tablero.tab[posicion_inicial[0]][posicion_inicial[1]].mover_peon(tablero, posicion_inicial,
                                                                                            posicion_final,
                                                                                            color_de_jugador)

                elif tablero.tab[posicion_inicial[0]][posicion_inicial[1]].__class__ is GeneralOro:
                    return tablero.tab[posicion_inicial[0]][posicion_inicial[1]].mover_general_oro(tablero,
                                                                                                   posicion_inicial,
                                                                                                   posicion_final,
                                                                                                   color_de_jugador)

                elif tablero.tab[posicion_inicial[0]][posicion_inicial[1]].__class__ is Rey:
                    return tablero.tab[posicion_inicial[0]][posicion_inicial[1]].mover_rey(tablero, posicion_inicial,
                                                                                           posicion_final,
                                                                                           color_de_jugador)

                elif tablero.tab[posicion_inicial[0]][posicion_inicial[1]].__class__ is GeneralPlata:
                    return tablero.tab[posicion_inicial[0]][posicion_inicial[1]].mover_general_plata(tablero,
                                                                                                     posicion_inicial,
                                                                                                     posicion_final,
                                                                                                     color_de_jugador)

                elif tablero.tab[posicion_inicial[0]][posicion_inicial[1]].__class__ is Caballo:
                    return tablero.tab[posicion_inicial[0]][posicion_inicial[1]].mover_caballo(tablero,
                                                                                               posicion_inicial,
                                                                                               posicion_final,
                                                                                               color_de_jugador)

                elif tablero.tab[posicion_inicial[0]][posicion_inicial[1]].__class__ is Alfil:
                    return tablero.tab[posicion_inicial[0]][posicion_inicial[1]].mover_alfil(tablero, posicion_inicial,
                                                                                             posicion_final,
                                                                                             color_de_jugador)

                elif tablero.tab[posicion_inicial[0]][posicion_inicial[1]].__class__ is Torre:
                    return tablero.tab[posicion_inicial[0]][posicion_inicial[1]].mover_torre(tablero, posicion_inicial,
                                                                                             posicion_final,
                                                                                             color_de_jugador)

                elif tablero.tab[posicion_inicial[0]][posicion_inicial[1]].__class__ is Lancero:
                    return tablero.tab[posicion_inicial[0]][posicion_inicial[1]].mover_lancero(tablero,
                                                                                               posicion_inicial,
                                                                                               posicion_final,
                                                                                               color_de_jugador)
            else:
                # print("Pieza de adversario")
                return False
        else:
            # print("No hay pieza para esa ubicacion")
            return False

    def verificar_jaque(self, ultimo_jugador, tablero):
        tablero.modo_control_tablero = True
        pieza_rey = (0, 0)
        # verifico color de jugadores
        if ultimo_jugador.color == 'negro':
            color_ultimo_jugador = 'negro'
            color_siguiente_jugador = 'blanco'
        else:
            color_ultimo_jugador = 'blanco'
            color_siguiente_jugador = 'negro'
        # encuentro la ubicacion del rey del jugador contrario
        for i in range(9):
            for j in range(9):
                if tablero.tab[i][j].__class__ == Rey:
                    if tablero.tab[i][j].color == color_siguiente_jugador:
                        pieza_rey = (i, j)
        # verifico que en cada posible jugada el rey pueda ser comido
        k = 0
        l = 0
        for i in range(9):
            for j in range(9):
                if tablero.tab[i][j] is not None:
                    if tablero.tab[i][j].color == color_ultimo_jugador:
                        # for k in range(9):
                        # for l in range(9):
                        pieza_cualquiera = (i, j)
                        # if tablero.tab[i][j].__class__ != Rey:
                        if self.jugar_pieza(tablero, color_ultimo_jugador, pieza_cualquiera, pieza_rey) is True:
                            tablero.modo_control_tablero = False
                            return True
                        else:
                            continue
        tablero.modo_control_tablero = False
        return False

    def verificar_jaque_mate(self, ultimo_jugador, tablero):
        pieza_rey = (0, 0)
        # verifico color de jugadores
        if ultimo_jugador.color == 'negro':
            color_ultimo_jugador = 'negro'
            color_siguiente_jugador = 'blanco'
        else:
            color_ultimo_jugador = 'blanco'
            color_siguiente_jugador = 'negro'
        # encuentro la ubicacion del rey del jugador contrario
        for i in range(9):
            for j in range(9):
                if tablero.tab[i][j].__class__ == Rey:
                    if tablero.tab[i][j].color == color_siguiente_jugador:
                        pieza_rey = (i, j)
                        continue
        # verifico si moviendo el rey es posible no ser comido
        for i in range(-1, 2):
            for j in range(-1, 2):
                tablero.tab[1][4]
                movimiento_rey = (pieza_rey[0] + i, pieza_rey[1] + j)
                if self.validar_posiciones(movimiento_rey[0], movimiento_rey[1]):
                    # verifico que la casilla donde va a mover el rey tenga una pieza que no sea de su mismo color o none
                    if tablero.tab[movimiento_rey[0]][movimiento_rey[1]] is None:
                        if self.jugar_pieza(tablero, color_siguiente_jugador, pieza_rey, movimiento_rey) is True:
                            if self.verificar_jaque(ultimo_jugador, tablero) is False:
                                self.jugar_pieza(tablero, color_siguiente_jugador, movimiento_rey, pieza_rey)
                                return False
                            else:
                                self.jugar_pieza(tablero, color_siguiente_jugador, movimiento_rey, pieza_rey)
                    # verifico si el movimiento del rey cae sobre una pieza del jugador contrario
                    elif tablero.tab[movimiento_rey[0]][movimiento_rey[1]].color == color_ultimo_jugador:
                        pieza_aux = tablero.tab[movimiento_rey[0]][movimiento_rey[1]]
                        tablero.tab[movimiento_rey[0]][movimiento_rey[1]] = None
                        # verifico si al mover el rey, luego queda en jaque, despues vuelvo a poner el rey en su lugar y si alguna pieza fue comida la vuelvo a colocar
                        if self.jugar_pieza(tablero, color_siguiente_jugador, pieza_rey, movimiento_rey) is True:
                            if self.verificar_jaque(ultimo_jugador, tablero) is False:
                                self.jugar_pieza(tablero, color_siguiente_jugador, movimiento_rey, pieza_rey)
                                tablero.tab[movimiento_rey[0]][movimiento_rey[1]] = pieza_aux
                                return False
                        self.jugar_pieza(tablero, color_siguiente_jugador, movimiento_rey, pieza_rey)
                        tablero.tab[movimiento_rey[0]][movimiento_rey[1]] = pieza_aux
        return True
