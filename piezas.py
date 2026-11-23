class Pieza(object):

    def __init__(self, color, nombre):
        
        self.color = color
        self.nombre = nombre

    def imprimir(self):
        return self.nombre

    def mover_pieza(self, jugador_activo, tablero, posicion_inicial, posicion_final):
        if tablero.tab[posicion_final[0]][posicion_final[1]] is None:
            tablero.tab[posicion_final[0]][posicion_final[1]] = tablero.tab[posicion_inicial[0]][posicion_inicial[1]]
            tablero.tab[posicion_inicial[0]][posicion_inicial[1]] = None
            return True
        else:
            # Si el destino está ocupado por una pieza del otro jugador se debe poner la pieza en estado muerta y cambiar el color, sino se cancela la jugada
            if jugador_activo == 'negro':
                jugador_inactivo = 'blanco'
            else:
                jugador_inactivo = 'negro'
            if tablero.tab[posicion_final[0]][posicion_final[1]].color == jugador_inactivo:
                # Si el modo control es verdadero no se mueve la pieza en el tablero
                if not tablero.modo_control_tablero:
                    pieza_capturada = tablero.tab[posicion_final[0]][posicion_final[1]]
                    pieza_capturada.color = jugador_activo
                    # Al capturar una pieza pierde su promocion y vuelve a su estado base
                    if hasattr(pieza_capturada, 'promocion'):
                        pieza_capturada.promocion = False
                    tablero.piezas_muertas.append(pieza_capturada)
                    tablero.tab[posicion_final[0]][posicion_final[1]] = tablero.tab[posicion_inicial[0]][posicion_inicial[1]]
                    tablero.tab[posicion_inicial[0]][posicion_inicial[1]] = None
                return True
            else:
                # Cancelar jugada porque no puedo comer mi propia pieza
                return False

    def mover_pieza_promocionada(self, color, tablero, posicion_inicial, posicion_final):
        # Valido que tipo de pieza es para llamar a la funcion que corresponda
        if tablero.tab[posicion_inicial[0]][posicion_inicial[1]].__class__ == Peon \
        or tablero.tab[posicion_inicial[0]][posicion_inicial[1]].__class__ == GeneralPlata \
        or tablero.tab[posicion_inicial[0]][posicion_inicial[1]].__class__ == Caballo \
        or tablero.tab[posicion_inicial[0]][posicion_inicial[1]].__class__ == Lancero:
            return self.mover_como_general_oro(color, tablero, posicion_inicial, posicion_final)
        if tablero.tab[posicion_inicial[0]][posicion_inicial[1]].__class__ == Alfil:
            return self.mover_como_alfil_coronado(color, tablero, posicion_inicial, posicion_final)
        if tablero.tab[posicion_inicial[0]][posicion_inicial[1]].__class__ == Torre:
            return self.mover_como_torre_coronada(color, tablero, posicion_inicial, posicion_final)

    def mover_como_general_oro(self, color, tablero, posicion_inicial, posicion_final):
        if tablero.tab[posicion_inicial[0]][posicion_inicial[1]].color == 'negro':
            # Si es una pieza del jugador negro puede mover hacia abajo, los costados y solo derecho hacia arriba
            if posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[1] == posicion_inicial[1] \
            or posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[1] == posicion_inicial[1] + 1 \
            or posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[1] == posicion_inicial[1] - 1 \
            or posicion_final[0] == posicion_inicial[0] and posicion_final[1] == posicion_inicial[1] - 1 \
            or posicion_final[0] == posicion_inicial[0] and posicion_final[1] == posicion_inicial[1] + 1 \
            or posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1]:
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
            or posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1] - 1:
                # Si el destino de la ficha esta libre, ponemos la pieza en ese lugar
                return self.mover_pieza(color, tablero, posicion_inicial, posicion_final)
            else:
                return False

    def mover_como_alfil_coronado(self, color, tablero, posicion_inicial, posicion_final):
        if (abs(posicion_final[0] - posicion_inicial[0]) == 1 and posicion_final[1] == posicion_inicial[1]) or \
           (posicion_final[0] == posicion_inicial[0] and abs(posicion_final[1] - posicion_inicial[1]) == 1):
            return self.mover_pieza(color, tablero, posicion_inicial, posicion_final)

        dr = 1 if posicion_final[0] > posicion_inicial[0] else (-1 if posicion_final[0] < posicion_inicial[0] else 0)
        dc = 1 if posicion_final[1] > posicion_inicial[1] else (-1 if posicion_final[1] < posicion_inicial[1] else 0)
        if dr == 0 or dc == 0:
            return False

        i = 0
        while i < 10:
            i += 1
            nr = posicion_inicial[0] + dr * i
            nc = posicion_inicial[1] + dc * i
            if not (0 <= nr < 9 and 0 <= nc < 9):
                return False
            if nr == posicion_final[0] and nc == posicion_final[1]:
                return self.mover_pieza(color, tablero, posicion_inicial, posicion_final)
            if tablero.tab[nr][nc] is not None:
                return False
        return False

    def mover_como_torre_coronada(self, color, tablero, posicion_inicial, posicion_final):
        if abs(posicion_final[0] - posicion_inicial[0]) == 1 and abs(posicion_final[1] - posicion_inicial[1]) == 1:
            return self.mover_pieza(color, tablero, posicion_inicial, posicion_final)

        dr = 1 if posicion_final[0] > posicion_inicial[0] else (-1 if posicion_final[0] < posicion_inicial[0] else 0)
        dc = 1 if posicion_final[1] > posicion_inicial[1] else (-1 if posicion_final[1] < posicion_inicial[1] else 0)
        if (dr != 0 and dc != 0) or (dr == 0 and dc == 0):
            return False

        i = 0
        while i < 10:
            i += 1
            nr = posicion_inicial[0] + dr * i
            nc = posicion_inicial[1] + dc * i
            if not (0 <= nr < 9 and 0 <= nc < 9):
                return False
            if nr == posicion_final[0] and nc == posicion_final[1]:
                return self.mover_pieza(color, tablero, posicion_inicial, posicion_final)
            if tablero.tab[nr][nc] is not None:
                return False
        return False


class Rey(Pieza):

    def __init__(self, color, nombre, jaque):
        super().__init__(color, nombre)  # Pongo super() para usar herencia sin self
        
        self.nombre = nombre
        self.color = color
        self.jaque = jaque

    def mover_rey(self, tablero, posicion_inicial, posicion_final, color_de_jugador):
        # El rey no tiene promocion por lo que solo tiene un tipo de movimeinto y es indiferente del color
        # El rey puede mover un lugar hacia cualquier lado
        if posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[1] == posicion_inicial[1] \
        or posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[1] == posicion_inicial[1] + 1 \
        or posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[1] == posicion_inicial[1] - 1 \
        or posicion_final[0] == posicion_inicial[0] and posicion_final[1] == posicion_inicial[1] - 1 \
        or posicion_final[0] == posicion_inicial[0] and posicion_final[1] == posicion_inicial[1] + 1 \
        or posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1] \
        or posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1] + 1 \
        or posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1] - 1:
            # Si el destino está libre, movemos el rey
            return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
        else:
            return False


class Lancero(Pieza):

    def __init__(self, promocion, color, nombre):
        super().__init__(color, nombre)  # Pongo super() para usar herencia sin self

        self.nombre = nombre
        self.color = color
        self.promocion = promocion

    def mover_lancero(self, tablero, posicion_inicial, posicion_final, color_de_jugador):
        i = 0
        if not tablero.tab[posicion_inicial[0]][posicion_inicial[1]].promocion:
            if tablero.tab[posicion_inicial[0]][posicion_inicial[1]].color == 'negro':
                if posicion_final[1] == posicion_inicial[1] and posicion_final[0] > posicion_inicial[0]:
                    # Si es una pieza del jugador negro solo puede mover hacia abajo hasta encontrar el final o otra pieza
                    while i < 10:
                        i += 1
                        nr = posicion_inicial[0] + i
                        if not (0 <= nr < 9):
                            return False
                        if posicion_final[0] == nr and posicion_final[1] == posicion_inicial[1]:
                            # Si el destino de la ficha esta libre, ponemos el lancero en ese lugar
                            return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
                        else:
                            if tablero.tab[nr][posicion_inicial[1]] is None:
                                continue
                            else:
                                return False
                else:
                    return False
            else:
                if posicion_final[1] == posicion_inicial[1] and posicion_final[0] < posicion_inicial[0]:
                    # Si es una pieza del jugador blanco solo puede mover hacia arriba ahsta encontrar el final o otra pieza
                    while i < 10:
                        i += 1
                        nr = posicion_inicial[0] - i
                        if not (0 <= nr < 9):
                            return False
                        if posicion_final[0] == nr and posicion_final[1] == posicion_inicial[1]:
                            # Si el destino de la ficha esta libre, ponemos el lancero en ese lugar
                            return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
                        else:
                            if tablero.tab[nr][posicion_inicial[1]] is None:
                                continue
                            else:
                                return False
                else:
                    return False
        else:
            return self.mover_pieza_promocionada(color_de_jugador, tablero, posicion_inicial, posicion_final)


class Caballo(Pieza):

    def __init__(self, promocion, color, nombre):
        super().__init__(color, nombre)  # Pongo super() para usar herencia sin self
        
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
                or posicion_final[0] == posicion_inicial[0] + 2 and posicion_final[1] == posicion_inicial[1] - 1:
                    # Si el destino de la ficha esta libre, ponemos el caballo en ese lugar
                    return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
                else:
                    return False
            else:
                # Si es una pieza del jugador blanco solo puede mover 2 lugares hacia arriba y uno a la derecha o izquierda
                if posicion_final[0] == posicion_inicial[0] - 2 and posicion_final[1] == posicion_inicial[1] + 1 \
                or posicion_final[0] == posicion_inicial[0] - 2 and posicion_final[1] == posicion_inicial[1] - 1:
                    # Si el destino de la ficha esta libre, ponemos el caballo en ese lugar
                    return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
                else:
                    return False
        else:
            return self.mover_pieza_promocionada(color_de_jugador, tablero, posicion_inicial, posicion_final)


class GeneralOro(Pieza):

    def __init__(self, color, nombre):
        super().__init__(color, nombre)  # Pongo super() para usar herencia sin self

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
                return False


class GeneralPlata(Pieza):

    def __init__(self, promocion, color, nombre):
        super().__init__(color, nombre)  # Pongo super() para usar herencia sin self

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
                or posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[1] == posicion_inicial[1] + 1 \
                or posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[1] == posicion_inicial[1] - 1 \
                or posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1] + 1 \
                or posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1] - 1:
                    # Si el destino de la ficha esta libre, ponemos el general en ese lugar
                    return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
                else:
                    return False
            else:
                # Si es una pieza del jugador blanco solo puede mover hacia arriba
                if posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1] \
                or posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1] + 1 \
                or posicion_final[0] == posicion_inicial[0] - 1 and posicion_final[1] == posicion_inicial[1] - 1 \
                or posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[1] == posicion_inicial[1] + 1 \
                or posicion_final[0] == posicion_inicial[0] + 1 and posicion_final[1] == posicion_inicial[1] - 1:
                    # Si el destino de la ficha esta libre, ponemos el gereral de plata en ese lugar
                    return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
                else:
                    return False
        else:
            return self.mover_pieza_promocionada(color_de_jugador, tablero, posicion_inicial, posicion_final)


class Alfil(Pieza):

    def __init__(self, promocion, color, nombre):
        super().__init__(color, nombre)  # Pongo super() para usar herencia sin self

        self.nombre = nombre
        self.color = color
        self.promocion = promocion

    def mover_alfil(self, tablero, posicion_inicial, posicion_final, color_de_jugador):
        # Verifico si la pieza tiene promocion
        if not tablero.tab[posicion_inicial[0]][posicion_inicial[1]].promocion:
            dr = 1 if posicion_final[0] > posicion_inicial[0] else (-1 if posicion_final[0] < posicion_inicial[0] else 0)
            dc = 1 if posicion_final[1] > posicion_inicial[1] else (-1 if posicion_final[1] < posicion_inicial[1] else 0)
            if dr == 0 or dc == 0:
                return False
            i = 0
            while i < 10:
                i += 1
                nr = posicion_inicial[0] + dr * i
                nc = posicion_inicial[1] + dc * i
                if not (0 <= nr < 9 and 0 <= nc < 9):
                    return False
                if nr == posicion_final[0] and nc == posicion_final[1]:
                    return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
                if tablero.tab[nr][nc] is not None:
                    return False
            return False
        else:
            return self.mover_pieza_promocionada(color_de_jugador, tablero, posicion_inicial, posicion_final)


class Torre(Pieza):

    def __init__(self, promocion, color, nombre):
        super().__init__(color, nombre)  # Pongo super() para usar herencia sin self

        self.nombre = nombre
        self.color = color
        self.promocion = promocion

    def mover_torre(self, tablero, posicion_inicial, posicion_final, color_de_jugador):
        # Verifico si la pieza tiene promocion
        if not tablero.tab[posicion_inicial[0]][posicion_inicial[1]].promocion:
            dr = 1 if posicion_final[0] > posicion_inicial[0] else (-1 if posicion_final[0] < posicion_inicial[0] else 0)
            dc = 1 if posicion_final[1] > posicion_inicial[1] else (-1 if posicion_final[1] < posicion_inicial[1] else 0)
            if (dr != 0 and dc != 0) or (dr == 0 and dc == 0):
                return False
            i = 0
            while i < 10:
                i += 1
                nr = posicion_inicial[0] + dr * i
                nc = posicion_inicial[1] + dc * i
                if not (0 <= nr < 9 and 0 <= nc < 9):
                    return False
                if nr == posicion_final[0] and nc == posicion_final[1]:
                    return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
                if tablero.tab[nr][nc] is not None:
                    return False
            return False
        else:
            return self.mover_pieza_promocionada(color_de_jugador, tablero, posicion_inicial, posicion_final)


class Peon(Pieza):

    def __init__(self, promocion, color, nombre):
        super().__init__(color, nombre)  # Pongo super() para usar herencia sin self

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
                    return False
            else:
                # Si es una pieza del jugador blanco solo puede mover hacia arriba
                if posicion_final[1] == posicion_inicial[1] and posicion_final[0] == posicion_inicial[0] - 1:
                    # Si el destino de la ficha esta libre, ponemos el peon en ese lugar
                    return self.mover_pieza(color_de_jugador, tablero, posicion_inicial, posicion_final)
                else:
                    return False
        else:
            return self.mover_pieza_promocionada(color_de_jugador, tablero, posicion_inicial, posicion_final)


