from piezas import *


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
                    return tablero.tab[posicion_inicial[0]][posicion_inicial[1]].mover_peon(tablero, posicion_inicial, posicion_final, color_de_jugador)

                elif tablero.tab[posicion_inicial[0]][posicion_inicial[1]].__class__ is GeneralOro:
                    return tablero.tab[posicion_inicial[0]][posicion_inicial[1]].mover_general_oro(tablero, posicion_inicial, posicion_final, color_de_jugador)

                elif tablero.tab[posicion_inicial[0]][posicion_inicial[1]].__class__ is Rey:
                    return tablero.tab[posicion_inicial[0]][posicion_inicial[1]].mover_rey(tablero, posicion_inicial, posicion_final, color_de_jugador)

                elif tablero.tab[posicion_inicial[0]][posicion_inicial[1]].__class__ is GeneralPlata:
                    return tablero.tab[posicion_inicial[0]][posicion_inicial[1]].mover_general_plata(tablero, posicion_inicial, posicion_final, color_de_jugador)

                elif tablero.tab[posicion_inicial[0]][posicion_inicial[1]].__class__ is Caballo:
                    return tablero.tab[posicion_inicial[0]][posicion_inicial[1]].mover_caballo(tablero, posicion_inicial, posicion_final, color_de_jugador)

                elif tablero.tab[posicion_inicial[0]][posicion_inicial[1]].__class__ is Alfil:
                    return tablero.tab[posicion_inicial[0]][posicion_inicial[1]].mover_alfil(tablero, posicion_inicial, posicion_final, color_de_jugador)

                elif tablero.tab[posicion_inicial[0]][posicion_inicial[1]].__class__ is Torre:
                    return tablero.tab[posicion_inicial[0]][posicion_inicial[1]].mover_torre(tablero, posicion_inicial, posicion_final, color_de_jugador)

                elif tablero.tab[posicion_inicial[0]][posicion_inicial[1]].__class__ is Lancero:
                    return tablero.tab[posicion_inicial[0]][posicion_inicial[1]].mover_lancero(tablero, posicion_inicial, posicion_final, color_de_jugador)
            else:
                #print("Pieza de adversario")
                return False
        else:
            #print("No hay pieza para esa ubicacion")
            return False

    def verificar_jaque(self, ultimo_jugador, tablero):
        jaque = False
        pieza_rey = (0, 0)
        if ultimo_jugador.color == 'negro':
            color_ultimo_jugador = 'negro'
            color_siguiente_jugador = 'blanco'
        else:
            color_ultimo_jugador = 'blanco'
            color_siguiente_jugador = 'negro'
        for i in range(9):
            for j in range(9):
                if tablero.tab[i][j].__class__ == Rey:
                    if tablero.tab[i][j].color == color_siguiente_jugador:
                        pieza_rey = (i, j)
        for i in tablero.tab:
            for j in i:
                if j and j.color == color_ultimo_jugador:
                    for k in range(9):
                        for l in range(9):
                            pieza_cualquiera = (k, l)
                            if tablero.tab[k][l]:
                                if tablero.tab[k][l].__class__ is not Rey:
                                    if self.jugar_pieza(tablero, j.color, pieza_cualquiera, pieza_rey) is True:
                                        jaque = True
                                        return jaque
                                    else:
                                        continue
        return jaque