import numpy


class Tablero:

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
        print("| ▲▼ |", end='')
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
                            print('🞄▼ |', end='')
                        else:
                            print(' ' + j.nombre, end='')
                            print('🞄▲ |', end='')
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


class Jugador:

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


class Pieza:

    def __init__(self, estado, color, nombre):
        self.estado = estado
        self.color = color
        self.nombre = nombre

    def imprimir(self):
        return self.nombre

    def mover_pieza(self, jugador_activo, tablero, posicion_inicial, posicion_final):
        if tablero.tab[posicion_final[0]][posicion_final[1]] is None:
            tablero.tab[posicion_final[0]][posicion_final[1]] = tablero.tab[posicion_inicial[0]][posicion_inicial[1]]
            tablero.tab[posicion_inicial[0]][posicion_inicial[1]] = None
            print("Pieza movida")
            return True
        else:
            # Si el destino está ocupado por una pieza del otro jugador se debe poner la pieza en estado muerta y cambiar el color, sino se cancela la jugada
            if jugador_activo == 'negro':
                jugador_inactivo = 'blanco'
            else:
                jugador_inactivo = 'negro'
            if tablero.tab[posicion_final[0]][posicion_final[1]].color == jugador_inactivo:
                tablero.tab[posicion_final[0]][posicion_final[1]].estado = 'muerta'
                tablero.tab[posicion_final[0]][posicion_final[1]].color = jugador_activo
                tablero.piezas_muertas.append(tablero.tab[posicion_final[0]][posicion_final[1]])
                tablero.tab[posicion_final[0]][posicion_final[1]] = tablero.tab[posicion_inicial[0]][posicion_inicial[1]]
                tablero.tab[posicion_inicial[0]][posicion_inicial[1]] = None
                print("Pieza comida")
                return True
            else:
                # Cancelar jugada porque no puedo comer mi propia pieza
                print("Jugada no permitida")
                return False

    def mover_pieza_promocionada(self, color, tablero, posicion_inicial, posicion_final):
        # Valido que tipo de pieza es para llamar a la funcion que corresponda
        if tablero.tab[posicion_inicial[0]][posicion_inicial[1]].__class__ == Peon \
        or tablero.tab[posicion_inicial[0]][posicion_inicial[1]].__class__ == GeneralPlata \
        or tablero.tab[posicion_inicial[0]][posicion_inicial[1]].__class__ == Caballo \
        or tablero.tab[posicion_inicial[0]][posicion_inicial[1]].__class__ == Lancero:
            self.mover_como_general_oro(color, tablero, posicion_inicial, posicion_final)
        if tablero.tab[posicion_inicial[0]][posicion_inicial[X]].__class__ == Alfil:
            self.mover_como_alfil_coronado(color, tablero, posicion_inicial, posicion_final)
        if tablero.tab[posicion_inicial[0]][posicion_inicial[X]].__class__ == Torre:
            self.mover_como_torre_coronada(color, tablero, posicion_inicial, posicion_final)
            
    def mover_como_general_oro(self, color, tablero, posicion_inicial, posicion_final):
        if tablero.tab[posicion_inicial[0]][posicion_inicial[1]].color == 'negro':
            # Si es una pieza del jugador negro puede mover hacia abajo, los costados y solo derecho hacia arriba
            if posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[1] == posicion_inicial[1] \
            or posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1] \
            or posicion_final[0] == posicion_inicial[0] and posicion_final[1] == posicion_inicial[1] + 1 \
            or posicion_final[0] == posicion_inicial[0] and posicion_final[1] == posicion_inicial[1] - 1 \
            or posicion_final[0] == posicion_inicial[0] and posicion_final[1] == posicion_inicial[1] + 1 \
            or posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[1] == posicion_inicial[1] - 1:
                # Si el destino de la ficha esta libre, ponemos la pieza en ese lugar
                return self.mover_pieza(color, tablero, posicion_inicial, posicion_final)
            else:
                return False
        else:
            # Si es una pieza del jugador blanco puede mover hacia arriba, los costados y solo derecho hacia abajo
            if posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[1] == posicion_inicial[1] \
            or posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1] \
            or posicion_final[0] == posicion_inicial[0] and posicion_final[1] == posicion_inicial[1] + 1 \
            or posicion_final[0] == posicion_inicial[0] and posicion_final[1] == posicion_inicial[1] - 1 \
            or posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1] + 1 \
            or posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1] + 1:
                # Si el destino de la ficha esta libre, ponemos la pieza en ese lugar
                return self.mover_pieza(color, tablero, posicion_inicial, posicion_final)
            else:
                return False

    # def mover_como_alfil_coronado(self, color, tablero, inicial, final):
    #     i = 0
    #     if final[Y] == inicial[Y]+1 and final[X] == inicial[X] or final[Y] == inicial[Y]-1 and final[X] == inicial[X] \
    #     or final[Y] == inicial[Y] and final[X] == inicial[X]+1 or final[Y] == inicial[Y] and final[X] == inicial[X]-1:
    #         # Si el destino está libre, movemos el alfil
    #         return self.mover_pieza(color, tablero, inicial, final)
    #     elif final[Y] > inicial[Y] and final[X] > inicial[X]:
    #         while i < 10:
    #             i += 1
    #             if final[Y] == inicial[Y] + i and final[X] == inicial[X] + i:
    #                 # Si el destino de la ficha esta libre, ponemos el alfil en ese lugar
    #                 return self.mover_pieza(color, tablero, inicial, final)
    #             else:
    #                 if tablero.tab[inicial[Y] + i][inicial[X] + i] is None:
    #                     continue
    #                 else:
    #                     print("Hay una pieza en el camino")
    #                     return False
    #
    #     elif final[Y] < inicial[Y] and final[X] < inicial[X]:
    #         while i < 10:
    #             i += 1
    #             if final[Y] == inicial[Y] - i and final[X] == inicial[X] - i:
    #                 # Si el destino de la ficha esta libre, ponemos el alfil en ese lugar
    #                 return self.mover_pieza(color, tablero, inicial, final)
    #             else:
    #                 if tablero.tab[inicial[Y] - i][inicial[X] - i] is None:
    #                     continue
    #                 else:
    #                     print("Hay una pieza en el camino")
    #                     return False
    #
    #     elif final[Y] < inicial[Y] and final[X] > inicial[X]:
    #         while i < 10:
    #             i += 1
    #             if final[Y] == inicial[Y] - i and final[X] == inicial[X] + i:
    #                 # Si el destino de la ficha esta libre, ponemos el alfil en ese lugar
    #                 return self.mover_pieza(color, tablero, inicial, final)
    #             else:
    #                 if tablero.tab[inicial[Y] - i][inicial[X] + i] is None:
    #                     continue
    #                 else:
    #                     print("Hay una pieza en el camino")
    #                     return False
    #
    #     elif final[Y] > inicial[Y] and final[X] < inicial[X]:
    #         while i < 10:
    #             i += 1
    #             if final[Y] == inicial[Y] + i and final[X] == inicial[X] - i:
    #                 # Si el destino de la ficha esta libre, ponemos el alfil en ese lugar
    #                 return self.mover_pieza(color, tablero, inicial, final)
    #             else:
    #                 if tablero.tab[inicial[Y] + i][inicial[X] - i] is None:
    #                     continue
    #                 else:
    #                     print("Hay una pieza en el camino")
    #                     return False
    #     else:
    #         print("Jugada no permitida")
    #         return False
    #
    # def mover_como_torre_coronada(self, color, tablero, inicial, final):
    #     i = 0
    #     if final[Y] == inicial[Y] + 1 and final[X] == inicial[X] + 1 or final[Y] == inicial[Y] - 1 and final[X] == inicial[X] - 1\
    #     or final[Y] == inicial[Y] + 1 and final[X] == inicial[X] - 1 or final[Y] == inicial[Y] - 1 and final[X] == inicial[X] + 1:
    #         # Si el destino está libre, movemos la torre
    #         return self.mover_pieza(color, tablero, inicial, final)
    #     elif final[Y] > inicial[Y] and final[X] > inicial[X]:
    #         while i < 10:
    #             i += 1
    #             if final[Y] == inicial[Y] + i and final[X] == inicial[X] + i:
    #                 # Si el destino de la ficha esta libre, ponemos la torre en ese lugar
    #                 return self.mover_pieza(color, tablero, inicial, final)
    #             else:
    #                 if tablero.tab[inicial[Y] + i][inicial[X] + i] is None:
    #                     continue
    #                 else:
    #                     print("Hay una pieza en el camino")
    #                     return False
    #     elif final[Y] < inicial[Y] and final[X] == inicial[X]:
    #         while i < 10:
    #             i += 1
    #             if final[Y] == inicial[Y] - i and final[X] == inicial[X] - i:
    #                 # Si el destino de la ficha esta libre, ponemos el alfil en ese lugar
    #                 return self.mover_pieza(color, tablero, inicial, final)
    #             else:
    #                 if tablero.tab[inicial[Y] - i][inicial[X] - i] is None:
    #                     continue
    #                 else:
    #                     print("Hay una pieza en el camino")
    #                     return False
    #     elif final[Y] < inicial[Y] and final[X] == inicial[X]:
    #         while i < 10:
    #             i += 1
    #             if final[Y] == inicial[Y] - i and final[X] == inicial[X] + i:
    #                 # Si el destino de la ficha esta libre, ponemos el alfil en ese lugar
    #                 return self.mover_pieza(color, tablero, inicial, final)
    #             else:
    #                 if tablero.tab[inicial[Y] - i][inicial[X] + i] is None:
    #                     continue
    #                 else:
    #                     print("Hay una pieza en el camino")
    #                     return False
    #     elif final[Y] > inicial[Y] and final[X] == inicial[X]:
    #         while i < 10:
    #             i += 1
    #             if final[Y] == inicial[Y] + i and final[X] == inicial[X] - i:
    #                 # Si el destino de la ficha esta libre, ponemos el alfil en ese lugar
    #                 return self.mover_pieza(color, tablero, inicial, final)
    #             else:
    #                 if tablero.tab[inicial[Y] + i][inicial[X] - i] is None:
    #                     continue
    #                 else:
    #                     print("Hay una pieza en el camino")
    #                     return False
    #     else:
    #         print("Jugada no permitida")
    #         return False

    def jugar_pieza_en_jaque(self, tablero, color, inicial, final):
         # Cuando el jugador esta en jaque solo puede move rel rey
         if final[0] == inicial[0] + 1 and final[1] == inicial[1] or final[0] == inicial[0] + 1 and final[1] == inicial[1] + 1 \
         or final[0] == inicial[0] + 1 and final[1] == inicial[1] - 1 or final[0] == inicial[0] and final[1] == inicial[1] - 1 \
         or final[0] == inicial[0] and final[1] == inicial[1] + 1 or final[0] == inicial[0] - 1 and final[1] == inicial[1] \
         or final[0] == inicial[0] - 1 and final[1] == inicial[1] + 1 or final[0] == inicial[0] - 1 and final[1] == inicial[1] - 1:
             # Si el destino está libre, movemos el rey
             return self.mover_pieza(color, tablero, inicial, final)
         else:
             print("El rey está en jaque, solo puede mover el rey")
             return False

    # def ingresar_pieza(self, color, inicial, final):
    #     pass


class Rey(Pieza):

    def __init__(self, estado, color, nombre, jaque):
        super().__init__(estado, color, nombre)  # Pongo super() para usar herencia sin self

        self.estado = estado
        self.nombre = nombre
        self.color = color
        self.jaque = jaque

    def __str__(self):
        return self.nombre

    def mover_rey(self, tablero, posicion_inicial, posicion_final, color_de_jugador):
        # El rey no tiene promocion por lo que solo tiene un tipo de movimeinto y es indiferente del color
        # El rey puede mover un lugar hacia cualquier lado
        if posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[1] == posicion_inicial[1] or posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[1] == posicion_inicial[1] + 1 \
        or posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[1] == posicion_inicial[1] - 1 or posicion_final[0] == posicion_inicial[0] and posicion_final[1] == posicion_inicial[1] - 1 \
        or posicion_final[0] == posicion_inicial[0] and posicion_final[1] == posicion_inicial[1] + 1 or posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1] \
        or posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1] + 1 or posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1] - 1:
            # Si el destino está libre, movemos el rey
            return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
        else:
            print("Jugada no permitida")
            return False


class Lancero(Pieza):

    def __init__(self, estado, promocion, color, nombre):
        super().__init__(estado, color, nombre)  # Pongo super() para usar herencia sin self

        self.estado = estado
        self.nombre = nombre
        self.color = color
        self.promocion = promocion

    def mover_lancero(self, tablero, posicion_inicial, posicion_final, color_de_jugador):
        i = 0
        if not tablero.tab[posicion_inicial[0]][posicion_inicial[1]].promocion:
            if tablero.tab[posicion_inicial[0]][posicion_inicial[1]].color == 'negro':
                if posicion_final[1] == posicion_inicial[1]:
                    # Si es una pieza del jugador negro solo puede mover hacia abajo ahsta encontrar el final o otra pieza
                    while i < 10:
                        i += 1
                        if posicion_final[0] == posicion_inicial[0] + i and posicion_final[1] == posicion_inicial[1]:
                            # Si el destino de la ficha esta libre, ponemos el lancero en ese lugar
                            return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
                        else:
                            if tablero.tab[posicion_inicial[0] + i][posicion_inicial[1]] is None:
                                continue
                            else:
                                print("Hay una pieza en el camino")
                                return False
                else:
                    print("Jugada no permitida")
                    return False
            else:
                if posicion_final[1] == posicion_inicial[1]:
                    # Si es una pieza del jugador blanco solo puede mover hacia arriba ahsta encontrar el final o otra pieza
                    while i < 10:
                        i += 1
                        if posicion_final[0] == posicion_inicial[0] - i and posicion_final[1] == posicion_inicial[1]:
                            # Si el destino de la ficha esta libre, ponemos el lancero en ese lugar
                            return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
                        else:
                            if tablero.tab[posicion_inicial[0] - i][posicion_inicial[1]] is None:
                                continue
                            else:
                                print("Hay una pieza en el camino")
                                return False
                else:
                    print("Jugada no permitida")
                    return False


class Caballo(Pieza):

    def __init__(self, estado, promocion, color, nombre):
        super().__init__(estado, color, nombre)  # Pongo super() para usar herencia sin self

        self.estado = estado
        self.nombre = nombre
        self.color = color
        self.promocion = promocion

    def mover_caballo(self, tablero, posicion_inicial, posicion_final, color_de_jugador):
        # Verifico si la pieza tiene promocion
        if not tablero.tab[posicion_inicial[0]][posicion_inicial[1]].promocion:
            # El caballo puede mover 2 hacia adelante y 1 a los costados
            if tablero.tab[posicion_inicial[0]][posicion_inicial[1]].color == 'negro':
                # Si es una pieza del jugador negro solo puede mover 2 lugares hacia abajo y 1 para la izquierda o derecha
                if posicion_final[0] == posicion_inicial[0] + 2 and posicion_final[1] == posicion_inicial[1] + 1 \
                or posicion_final[0] == posicion_inicial[0] + 2 and posicion_final[0] == posicion_inicial[0] - 1:
                    # Si el destino de la ficha esta libre, ponemos el caballo en ese lugar
                    return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
                else:
                    print("Jugada no permitida")
                    return False
            else:
                # Si es una pieza del jugador blanco solo puede mover 2 lugares hacia arriba y uno a la derecha o izquierda
                if posicion_final[0] == posicion_inicial[0] - 2 and posicion_final[1] == posicion_inicial[1] + 1 \
                or posicion_final[0] == posicion_inicial[0] - 2 and posicion_final[0] == posicion_inicial[0] - 1:
                    # Si el destino de la ficha esta libre, ponemos el caballo en ese lugar
                    return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
                else:
                    print("Jugada no permitida")
                    return False
        else:
            self.promocion(color_de_jugador, posicion_inicial, posicion_final)


class GeneralOro(Pieza):

    def __init__(self, estado, color, nombre):
        super().__init__(estado, color, nombre)  # Pongo super() para usar herencia sin self

        self.estado = estado
        self.nombre = nombre
        self.color = color

    # El general no tiene promocion por lo que solo tiene un tipo de movimeinto que depende del color del jugador
    def mover_general_oro(self, tablero, posicion_inicial, posicion_final, color_de_jugador):
        # El general no tiene promocion por lo que solo tiene un tipo de movimeinto que depende del color del jugador
        if tablero.tab[posicion_inicial[0]][posicion_inicial[1]].color == 'negro':
            # Si es una pieza del jugador negro puede mover hacia abajo, los costados y solo derecho hacia arriba
            if posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[1] == posicion_inicial[1] \
            or posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[1] == posicion_inicial[1] + 1 \
            or posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[1] == posicion_inicial[1] - 1 \
            or posicion_final[0] == posicion_inicial[0] and posicion_final[1] == posicion_inicial[1] - 1 \
            or posicion_final[0] == posicion_inicial[0] and posicion_final[1] == posicion_inicial[1] + 1 \
            or posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1]:
                # Si el destino de la ficha esta libre, ponemos el general de oro en ese lugar
                return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
            else:
                print("Jugada no permitida")
                return False
        else:
            # Si es una pieza del jugador blanco puede mover hacia arriba, los costados y solo derecho hacia abajo
            if posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1] \
            or posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1] + 1 \
            or posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1] - 1 \
            or posicion_final[0] == posicion_inicial[0] and posicion_final[1] == posicion_inicial[1] - 1 \
            or posicion_final[0] == posicion_inicial[0] and posicion_final[1] == posicion_inicial[1] + 1 \
            or posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[1] == posicion_inicial[1]:
                # Si el destino de la ficha esta libre, ponemos el general de oro en ese lugar
                return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
            else:
                print("Jugada no permitida")
                return False


class GeneralPlata(Pieza):

    def __init__(self, estado, promocion, color, nombre):
        super().__init__(estado, color, nombre)  # Pongo super() para usar herencia sin self

        self.estado = estado
        self.nombre = nombre
        self.color = color
        self.promocion = promocion

    def mover_general_plata(self, tablero, posicion_inicial, posicion_final, color_de_jugador):
        # Verifico si la pieza tiene promocion
        if not tablero.tab[posicion_inicial[0]][posicion_inicial[1]].promocion:
            # El general de plata puede mover adelante derecho y cruzado y atras cruzado
            if tablero.tab[posicion_inicial[0]][posicion_inicial[1]].color == 'negro':
                # Si es una pieza del jugador negro solo puede mover hacia abajo y cruzado para atras
                if posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[1] == posicion_inicial[1] \
                or posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[0] == posicion_inicial[0] + 1 \
                or posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[1] == posicion_inicial[1] - 1 \
                or posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1] + 1 \
                or posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1] - 1:
                    # Si el destino de la ficha esta libre, ponemos el general en ese lugar
                    return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
                else:
                    print("Jugada no permitida")
                    return False
            else:
                # Si es una pieza del jugador blanco solo puede mover hacia arriba
                if posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1] \
                or posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[0] == posicion_inicial[0] + 1 \
                or posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1] - 1 \
                or posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[1] == posicion_inicial[1] + 1 \
                or posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[1] == posicion_inicial[1] - 1:
                    # Si el destino de la ficha esta libre, ponemos el gereral de plata en ese lugar
                    return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_inicial)
                else:
                    print("Jugada no permitida")
                    return False
        else:
            return self.promocion(color_de_jugador, posicion_inicial, posicion_final)


class Alfil(Pieza):

    def __init__(self, estado, promocion, color, nombre):
        super().__init__(estado, color, nombre)  # Pongo super() para usar herencia sin self

        self.estado = estado
        self.nombre = nombre
        self.color = color
        self.promocion = promocion

    def mover_alfil(self, tablero, posicion_inicial, posicion_final, color_de_jugador):
        # Verifico si la pieza tiene promocion
        if not tablero.tab[posicion_inicial[0]][posicion_inicial[1]].promocion:
            # Es indiferente el color para mover
            # El alfil puede mover en diagonal ahsta topar con el final del tablero o otra pieza
            i = 0
            var = 0
            if posicion_final[0] > posicion_inicial[0] and posicion_final[1] > posicion_inicial[1]:
                var = 1
            elif posicion_final[0] < posicion_inicial[0] and posicion_final[1] < posicion_inicial[1]:
                var = 2
            elif posicion_final[0] < posicion_inicial[0] and posicion_final[1] > posicion_inicial[1]:
                var = 3
            elif posicion_final[0] > posicion_inicial[0] and posicion_final[1] < posicion_inicial[1]:
                var = 4
            if var == 1:
                while i < 10:
                    i += 1
                    if posicion_final[0] == posicion_inicial[0] + i and posicion_final[1] == posicion_inicial[1] + i:
                        # Si el destino de la ficha esta libre, ponemos el alfil en ese lugar
                        return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
                    else:
                        if tablero.tab[posicion_inicial[0] + i][posicion_inicial[1] + i] is None:
                            continue
                        else:
                            print("Hay una pieza en el camino")
                            return False
            if var == 2:
                while i < 10:
                    i += 1
                    if posicion_final[0] == posicion_inicial[0] - i and posicion_final[1] == posicion_inicial[1] - i:
                        # Si el destino de la ficha esta libre, ponemos el alfil en ese lugar
                        return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
                    else:
                        if tablero.tab[posicion_inicial[0][0] - i][posicion_inicial[0][1] - i] is None:
                            continue
                        else:
                            print("Hay una pieza en el camino")
                            return False
            if var == 3:
                while i < 10:
                    i += 1
                    if posicion_final[0] == posicion_inicial[0] - i and posicion_final[1] == posicion_inicial[1] + i:
                        # Si el destino de la ficha esta libre, ponemos el alfil en ese lugar
                        return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
                    else:
                        if tablero.tab[posicion_inicial[0][0] - i][posicion_inicial[0][1] + i] is None:
                            continue
                        else:
                            print("Hay una pieza en el camino")
                            return False
            if var == 4:
                while i < 10:
                    i += 1
                    if posicion_final[0] == posicion_inicial[0] + i and posicion_final[1] == posicion_inicial[1] - i:
                        # Si el destino de la ficha esta libre, ponemos el alfil en ese lugar
                        return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
                    else:
                        if tablero.tab[posicion_inicial[0] + i][posicion_inicial[1] - i] is None:
                            continue
                        else:
                            print("Hay una pieza en el camino")
                            return False

        else:
            return self.promocion(color_de_jugador, posicion_inicial, posicion_final)


class Torre(Pieza):

    def __init__(self, estado, promocion, color, nombre):
        super().__init__(estado, color, nombre)  # Pongo super() para usar herencia sin self

        self.estado = estado
        self.nombre = nombre
        self.color = color
        self.promocion = promocion

    def mover_torre(self, tablero, posicion_inicial, posicion_final, color_de_jugador):
        # Verifico si la pieza tiene promocion
        if not tablero.tab[posicion_inicial[0]][posicion_inicial[1]].promocion:
            # Es indiferente el color para mover
            # El alfil puede mover en diagonal ahsta topar con el final del tablero o otra pieza
            i = 0
            var = 0
            if posicion_final[0] > posicion_inicial[0] and posicion_final[1] == posicion_inicial[1]:
                var = 1
            elif posicion_final[0] < posicion_inicial[0] and posicion_final[1] == posicion_inicial[1]:
                var = 2
            elif posicion_final[0] == posicion_inicial[0] and posicion_final[1] > posicion_inicial[1]:
                var = 3
            elif posicion_final[0] == posicion_inicial[0] and posicion_final[1] < posicion_inicial[1]:
                var = 4
            if var == 1:
                while i < 10:
                    i += 1
                    if posicion_final[0] == posicion_inicial[0] + i and posicion_final[1] == posicion_inicial[1]:
                        # Si el destino de la ficha esta libre, ponemos el alfil en ese lugar
                        return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
                    else:
                        if tablero.tab[posicion_inicial[0] + i][posicion_inicial[1]] is None:
                            continue
                        else:
                            print("Hay una pieza en el camino")
                            return False
            if var == 2:
                while i < 10:
                    i += 1
                    if posicion_final[0] == posicion_inicial[0] - i and posicion_final[1] == posicion_inicial[0][1]:
                        # Si el destino de la ficha esta libre, ponemos el alfil en ese lugar
                        return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
                    else:
                        if tablero.tab[posicion_inicial[0] - i][posicion_inicial[0][1] ] is None:
                            continue
                        else:
                            print("Hay una pieza en el camino")
                            return False
            if var == 3:
                while i < 10:
                    i += 1
                    if posicion_final[0] == posicion_inicial[0] and posicion_final[1] == posicion_inicial[1] + i:
                        # Si el destino de la ficha esta libre, ponemos el alfil en ese lugar
                        return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
                    else:
                        if tablero.tab[posicion_inicial[0]][posicion_inicial[1] + i] is None:
                            continue
                        else:
                            print("Hay una pieza en el camino")
                            return False
            if var == 4:
                while i < 10:
                    i += 1
                    if posicion_final[0] == posicion_inicial[0] and posicion_final[1] == posicion_inicial[1] - i:
                        # Si el destino de la ficha esta libre, ponemos el alfil en ese lugar
                        return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
                    else:
                        if tablero.tab[posicion_inicial[0]][posicion_inicial[1] - i] is None:
                            continue
                        else:
                            print("Hay una pieza en el camino")
                            return False
        else:
            return self.promocion(color_de_jugador, posicion_inicial, posicion_final)


class Peon(Pieza):

    def __init__(self, estado, promocion, color, nombre):
        super().__init__(estado, color, nombre)  # Pongo super() para usar herencia sin self

        self.estado = estado
        self.nombre = nombre
        self.color = color
        self.promocion = promocion

    def mover_peon(self, tablero, posicion_inicial, posicion_final, color_de_jugador):
        # Verifico si la pieza tiene promocion
        if not tablero.tab[posicion_inicial[0]][posicion_inicial[1]].promocion:
            # El peon no está en estado de promocion por lo que solo puede mover un lugar adelante
            if color_de_jugador == 'negro':
                # Si es una pieza del jugador negro solo puede mover hacia abajo
                if posicion_final[1] == posicion_inicial[1] and posicion_final[0] == posicion_inicial[0] + 1:
                    # Si el destino de la ficha esta libre, ponemos el peon en ese lugar
                    return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
                else:
                    print("Jugada no permitida")
                    return False
            else:
                # Si es una pieza del jugador blanco solo puede mover hacia arriba
                if posicion_final[1] == posicion_inicial[1] and posicion_final[0] == posicion_inicial[0] - 1:
                    # Si el destino de la ficha esta libre, ponemos el peon en ese lugar
                    return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
                else:
                    print("Jugada no permitida")
                    return False
        else:
            return self.promocion(color_de_jugador, posicion_inicial, posicion_final)


