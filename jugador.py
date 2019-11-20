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
                print("Pieza de adversario")
                return False
        else:
            print("No hay pieza para esa ubicacion")
            return False

    def jugar_pieza_en_jaque(self, tablero, color, posicion_inicial, posicion_final):
         # Cuando el jugador esta en jaque solo puede move rel rey
         if posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[1] == posicion_inicial[1] or posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[1] == posicion_inicial[1] + 1 \
         or posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[1] == posicion_inicial[1] - 1 or posicion_final[0] == posicion_inicial[0] and posicion_final[1] == posicion_inicial[1] - 1 \
         or posicion_final[0] == posicion_inicial[0] and posicion_final[1] == posicion_inicial[1] + 1 or posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1] \
         or posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1] + 1 or posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1] - 1:
             # Si el destino está libre, movemos el rey
             return self.mover_pieza(color, tablero, posicion_inicial, posicion_final)
         else:
             print("El rey está en jaque, solo puede mover el rey")
             return False