import numpy


class Tablero:

    def __init__(self):

        self.juego = 'iniciado'

        self.columna = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        self.fila = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

        self.t = [
            [Lancero('v', 'no', 'negro', 'L'), Caballo('v', 'no', 'negro', 'N'), GeneralPlata('v', 'no', 'negro', 'S'),
             GeneralOro('v', 'negro', 'G'), Rey('v', 'negro', 'K', False), GeneralOro('v', 'negro', 'G'),
             GeneralPlata('v', 'no', 'negro', 'S'), Caballo('v', 'no', 'negro', 'N'), Lancero('v', 'no', 'negro', 'L')],

            [None, Torre('v', 'no', 'negro', 'R'), None, None, None, None, None, Alfil('v', 'no', 'negro', 'B'), None],

            [Peon('v', 'no', 'negro', 'P'), Peon('v', 'no', 'negro', 'P'), Peon('v', 'no', 'negro', 'P'),
             Peon('v', 'no', 'negro', 'P'), Peon('v', 'no', 'negro', 'P'), Peon('v', 'no', 'negro', 'P'),
             Peon('v', 'no', 'negro', 'P'), Peon('v', 'no', 'negro', 'P'), Peon('v', 'no', 'negro', 'P')],

            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],

            [Peon('v', 'no', 'blanco', 'P'), Peon('v', 'no', 'blanco', 'P'), Peon('v', 'no', 'blanco', 'P'),
             Peon('v', 'no', 'blanco', 'P'), Peon('v', 'no', 'blanco', 'P'), Peon('v', 'no', 'blanco', 'P'),
             Peon('v', 'no', 'blanco', 'P'), Peon('v', 'no', 'blanco', 'P'), Peon('v', 'no', 'blanco', 'P')],

            [None, Alfil('v', 'no', 'blanco', 'B'), None, None, None, None, None, Torre('v', 'no', 'blanco', 'R'),
             None],

            [Lancero('v', 'no', 'blanco', 'L'), Caballo('v', 'no', 'blanco', 'N'),
             GeneralPlata('v', 'no', 'blanco', 'S'),
             GeneralOro('v', 'blanco', 'G'), Rey('v', 'blanco', 'K', False), GeneralOro('v', 'blanco', 'G'),
             GeneralPlata('v', 'no', 'blanco', 'S'), Caballo('v', 'no', 'blanco', 'N'),
             Lancero('v', 'no', 'blanco', 'L')],
        ]

        self.tab = numpy.array(self.t)

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
                    if j.estado == 'v':
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

    def verificar_jaque_negro(self):
        for i in self.tab:
            for j in i:
                if j == Rey and j.color == 'negro' and j.jaque == True:
                    return True

    def verificar_jaque_blanco(self):
        for i in self.tab:
            for j in i:
                if j == Rey and j.color == 'blanco' and j.jaque == True:
                    return True


class Jugador:

    def __init__(self, color):
        self.color = color

    def validar_posiciones(self, x, y):
        if 9 > x >= 0 and 9 > y >= 0:
            return x, y
        else:
            return False

    def promocion(self, tablero, inicial, final):
        # El peon está en estado de promocion y puede mover como general de oro
        if tablero.tab[inicial[0]][inicial[1]].color == 'negro':
            # Si es una pieza del jugador negro puede mover hacia abajo, los costados y solo derecho hacia arriba
            if final[0] == inicial[0] + 1 and final[1] == inicial[1] or final[0] == inicial[0] - 1 \
                    and final[1] == inicial[1] or final[0] == inicial[0] and final[1] == inicial[1] + 1 or final[0] == \
                    inicial[0] \
                    and final[1] == inicial[1] - 1 or final[0] == inicial[0] and final[1] == inicial[1] + 1 or final[
                0] == inicial[0] + 1 \
                    and final[1] == inicial[1] - 1:
                # Si el destino de la ficha esta libre, ponemos el peon en ese lugar
                if tablero.tab[final[0]][final[1]] is None:
                    tablero.tab[final[0]][final[1]] = tablero.tab[inicial[0]][inicial[1]]
                    tablero.tab[inicial[0]][inicial[1]] = None
                    print("Pieza movida")
                    return True
                else:
                    # Si el destino está ocupado por una pieza del otro jugador se debe poner la pieza en estado muerta y cambiar el color, sino se cancela la jugada
                    if tablero.tab[final[0]][final[1]].color == 'blanco':
                        tablero.tab[final[0]][final[1]].estado = 'm'
                        tablero.tab[final[0]][final[1]].estado = 'negro'
                        tablero.tab[final[0]][final[1]] = tablero.tab[inicial[0]][inicial[1]]
                        print("Pieza comida")
                        return True
                    else:
                        # Cancelar jugada porque no puedo comer mi propia pieza
                        print("Jugada no permitida")
                        return False
            else:
                return False
        else:
            # Si es una pieza del jugador blanco puede mover hacia arriba, los costados y solo derecho hacia abajo
            if final[0] == inicial[0] + 1 and final[1] == inicial[1] or final[0] == inicial[0] - 1 and \
                    final[1] == inicial[1] or final[0] == inicial[0] \
                    and final[1] == inicial[1] + 1 or final[0] == inicial[0] and final[1] == inicial[
                1] - 1 or final[0] == inicial[0] - 1 \
                    and final[1] == inicial[1] + 1 or final[0] == inicial[0] - 1 and final[1] == \
                    inicial[1] + 1:
                # Si el destino de la ficha esta libre, ponemos el peon en ese lugar
                if tablero.tab[final[0]][final[1]] is None:
                    tablero.tab[final[0]][final[1]] = tablero.tab[inicial[0]][inicial[1]]
                    tablero.tab[inicial[0]][inicial[1]] = None
                    print("Pieza movida")
                    return True
                else:
                    # Si el destino está ocupado por una pieza del otro jugador se debe poner la pieza en estado muerta y cambiar el color, sino se cancela la jugada
                    if tablero.tab[final[0]][final[1]].color == 'negro':
                        tablero.tab[final[0]][final[1]].estado = 'm'
                        tablero.tab[final[0]][final[1]].estado = 'blanco'
                        tablero.tab[final[0]][final[1]] = tablero.tab[inicial[0]][inicial[1]]
                        print("Pieza comida")
                        return True
                    else:
                        # Cancelar jugada porque no puedo comer mi propia pieza
                        print("Jugada no permitida")
                        return False

    def jugar_pieza(self, tablero, color, inicial, final):
        # Si es una pieza entro
        if tablero.tab[inicial[0]][inicial[1]]:
            # Verifico que tipo de pieza es para despues analizar el movimiento
            if tablero.tab[inicial[0]][inicial[1]].color == color:
                #Verifico si se selecciono una pieza del jugador en el tablero
                if tablero.tab[inicial[0]][inicial[1]].__class__ is Peon:
                    # Verifico si la pieza tiene promocion
                    if tablero.tab[inicial[0]][inicial[1]].promocion == 'no':
                        # El peon no está en estado de promocion por lo que solo puede mover un lugar adelante
                        if tablero.tab[inicial[0]][inicial[1]].color == 'negro':
                            # Si es una pieza del jugador negro solo puede mover hacia abajo
                            if final[1] == inicial[1] and final[0] == inicial[0] + 1:
                                # Si el destino de la ficha esta libre, ponemos el peon en ese lugar
                                if tablero.tab[final[0]][final[1]] is None:
                                    tablero.tab[final[0]][final[1]] = tablero.tab[inicial[0]][inicial[1]]
                                    tablero.tab[inicial[0]][inicial[1]] = None
                                    print("Pieza movida")
                                    return True
                                else:
                                    # Si el destino está ocupado por una pieza del otro jugador se debe poner la pieza en estado muerta y cambiar el color, sino se cancela la jugada
                                    if tablero.tab[final[0]][final[1]].color == 'blanco':
                                        tablero.tab[final[0]][final[1]].estado = 'm'
                                        tablero.tab[final[0]][final[1]].estado = 'negro'
                                        tablero.tab[final[0]][final[1]] = tablero.tab[inicial[0]][inicial[1]]
                                        print("Pieza comida")
                                        return True
                                    else:
                                        # Cancelar jugada porque no puedo comer mi propia pieza
                                        print("Jugada no permitida")
                                        return False
                            else:
                                print("Jugada no permitida")
                                return False
                        else:
                            # Si es una pieza del jugador blanco solo puede mover hacia arriba
                            if final[1] == inicial[1] and final[0] == inicial[0] - 1:
                                # Si el destino de la ficha esta libre, ponemos el peon en ese lugar
                                if tablero.tab[final[0]][final[1]] is None:
                                    tablero.tab[final[0]][final[1]] = tablero.tab[inicial[0]][inicial[1]]
                                    tablero.tab[inicial[0]][inicial[1]] = None
                                    print("Pieza movida")
                                    return True
                                else:
                                    # Si el destino está ocupado por una pieza del otro jugador se debe poner la pieza en estado muerta y cambiar el color, sino se cancela la jugada
                                    if tablero.tab[final[0]][final[1]].color == 'negro':
                                        tablero.tab[final[0]][final[1]].estado = 'm'
                                        tablero.tab[final[0]][final[1]].estado = 'blanco'
                                        tablero.tab[final[0]][final[1]] = tablero.tab[inicial[0]][inicial[1]]
                                        print("Pieza comida")
                                        return True
                                    else:
                                        # Cancelar jugada porque no puedo comer mi propia pieza
                                        print("Jugada no permitida")
                                        return False
                            else:
                                print("Jugada no permitida")
                                return False
                    else:
                        self.promocion(color, inicial, final)

                elif tablero.tab[inicial[0]][inicial[1]].__class__ is GeneralOro:
                    # El general no tiene promocion por lo que solo tiene un tipo de movimeinto que depende del color del jugador
                    if tablero.tab[inicial[0]][inicial[1]].color == 'negro':
                        # Si es una pieza del jugador negro puede mover hacia abajo, los costados y solo derecho hacia arriba
                        if final[0] == inicial[0]+1 and final[1] == inicial[1] or final[0] == inicial[0]+1 and final[1] == inicial[1]+1 \
                        or final[0] == inicial[0]+1 and final[1] == inicial[1]-1 or final[0] == inicial[0] and final[1] == inicial[1]-1 \
                        or final[0] == inicial[0] and final[1] == inicial[1]+1 or final[0] == inicial[0]-1 and final[1] == inicial[1]:
                            # Si el destino de la ficha esta libre, ponemos el peon en ese lugar
                            if tablero.tab[final[0]][final[1]] is None:
                                tablero.tab[final[0]][final[1]] = tablero.tab[inicial[0]][inicial[1]]
                                tablero.tab[inicial[0]][inicial[1]] = None
                                print("Pieza movida")
                                return True
                            else:
                                # Si el destino está ocupado por una pieza del otro jugador se debe poner la pieza en estado muerta y cambiar el color, sino se cancela la jugada
                                if tablero.tab[final[0]][final[1]].color == 'blanco':
                                    tablero.tab[final[0]][final[1]].estado = 'm'
                                    tablero.tab[final[0]][final[1]].estado = 'negro'
                                    tablero.tab[final[0]][final[1]] = tablero.tab[inicial[0]][inicial[1]]
                                    print("Pieza comida")
                                    return True
                                else:
                                    # Cancelar jugada porque no puedo comer mi propia pieza
                                    print("Jugada no permitida")
                                    return False
                        else:
                            print("Jugada no permitida")
                            return False
                    else:
                        # Si es una pieza del jugador blanco puede mover hacia arriba, los costados y solo derecho hacia abajo
                        if final[0] == inicial[0]-1 and final[1] == inicial[1] or final[0] == inicial[0]-1 and final[1] == inicial[1]+1 \
                        or final[0] == inicial[0]-1 and final[1] == inicial[1]-1 or final[0] == inicial[0] and final[1] == inicial[1]-1 \
                        or final[0] == inicial[0] and final[1] == inicial[1]+1 or final[0] == inicial[0]+1 and final[1] == inicial[1]:
                            # Si el destino de la ficha esta libre, ponemos el peon en ese lugar
                            if tablero.tab[final[0]][final[1]] is None:
                                tablero.tab[final[0]][final[1]] = tablero.tab[inicial[0]][inicial[1]]
                                tablero.tab[inicial[0]][inicial[1]] = None
                                print("Pieza movida")
                                return True
                            else:
                                # Si el destino está ocupado por una pieza del otro jugador se debe poner la pieza en estado muerta y cambiar el color, sino se cancela la jugada
                                if tablero.tab[final[0]][final[1]].color == 'negro':
                                    tablero.tab[final[0]][final[1]].estado = 'm'
                                    tablero.tab[final[0]][final[1]].estado = 'blanco'
                                    tablero.tab[final[0]][final[1]] = tablero.tab[inicial[0]][inicial[1]]
                                    print("Pieza comida")
                                    return True
                                else:
                                    # Cancelar jugada porque no puedo comer mi propia pieza
                                    print("Jugada no permitida")
                                    return False
                        else:
                            print("Jugada no permitida")
                            return False

                elif tablero.tab[inicial[0]][inicial[1]].__class__ is Rey:
                    # El rey no tiene promocion por lo que solo tiene un tipo de movimeinto y es indiferente del color
                        # El rey puede mover un lugar hacia cualquier lado
                        if final[0] == inicial[0]+1 and final[1] == inicial[1] or final[0] == inicial[0]+1 and final[1] == inicial[1]+1 \
                        or final[0] == inicial[0]+1 and final[1] == inicial[1]-1 or final[0] == inicial[0] and final[1] == inicial[1]-1 \
                        or final[0] == inicial[0] and final[1] == inicial[1]+1 or final[0] == inicial[0]-1 and final[1] == inicial[1] \
                        or final[0] == inicial[0]-1 and final[1] == inicial[1]+1 or final[0] == inicial[0]-1 and final[1] == inicial[1]-1:
                            # Si el destino está libre, movemos el rey
                            if tablero.tab[final[0]][final[1]] is None:
                                tablero.tab[final[0]][final[1]] = tablero.tab[inicial[0]][inicial[1]]
                                tablero.tab[inicial[0]][inicial[1]] = None
                                print("Pieza movida")
                                return True
                            else:
                                # Si el destino está ocupado por una pieza del otro jugador se debe poner la pieza en estado muerta y cambiar el color, sino se cancela la jugada
                                if tablero.tab[final[0]][final[1]].color == 'blanco':
                                    tablero.tab[final[0]][final[1]].estado = 'm'
                                    tablero.tab[final[0]][final[1]].estado = 'negro'
                                    tablero.tab[final[0]][final[1]] = tablero.tab[inicial[0]][inicial[1]]
                                    print("Pieza comida")
                                    return True
                                else:
                                    # Cancelar jugada porque no puedo comer mi propia pieza
                                    print("Jugada no permitida")
                                    return False
                        else:
                            print("Jugada no permitida")
                            return False

                elif tablero.tab[inicial[0]][inicial[1]].__class__ is GeneralPlata:
                    # Verifico si la pieza tiene promocion
                    if tablero.tab[inicial[0]][inicial[1]].promocion == 'no':
                        # El general de plata puede mover adelante derecho y cruzado y atras cruzado
                        if tablero.tab[inicial[0]][inicial[1]].color == 'negro':
                            # Si es una pieza del jugador negro solo puede mover hacia abajo y cruzado para atras
                                if final[0] == inicial[0]+1 and final[1] == inicial[1] or final[0] == inicial[0]+1 and final[0] == inicial[0]+1 \
                                or final[0] == inicial[0]+1 and final[1] == inicial[1]-1 or final[0] == inicial[0]-1 and final[1] == inicial[1]+1 \
                                or final[0] == inicial[0]-1 and final[1] == inicial[1]-1:
                                    # Si el destino de la ficha esta libre, ponemos el general en ese lugar
                                    if tablero.tab[final[0]][final[1]] is None:
                                        tablero.tab[final[0]][final[1]] = tablero.tab[inicial[0]][inicial[1]]
                                        tablero.tab[inicial[0]][inicial[1]] = None
                                        print("Pieza movida")
                                        return True
                                    else:
                                        # Si el destino está ocupado por una pieza del otro jugador se debe poner la pieza en estado muerta y cambiar el color, sino se cancela la jugada
                                        if tablero.tab[final[0]][final[1]].color == 'blanco':
                                            tablero.tab[final[0]][final[1]].estado = 'm'
                                            tablero.tab[final[0]][final[1]].estado = 'negro'
                                            tablero.tab[final[0]][final[1]] = tablero.tab[inicial[0]][inicial[1]]
                                            print("Pieza comida")
                                            return True
                                        else:
                                            # Cancelar jugada porque no puedo comer mi propia pieza
                                            print("Jugada no permitida")
                                            return False
                                else:
                                    print("Jugada no permitida")
                                    return False
                        else:
                            # Si es una pieza del jugador blanco solo puede mover hacia arriba
                            if final[0] == inicial[0]-1 and final[1] == inicial[1] or final[0] == inicial[0]-1 and final[0] == inicial[0]+1 \
                            or final[0] == inicial[0]-1 and final[1] == inicial[1]-1 or final[0] == inicial[0]+1 and final[1] == inicial[1] + 1 \
                            or final[0] == inicial[0]+1 and final[1] == inicial[1]-1:
                                # Si el destino de la ficha esta libre, ponemos el peon en ese lugar
                                if tablero.tab[final[0]][final[1]] is None:
                                    tablero.tab[final[0]][final[1]] = tablero.tab[inicial[0]][inicial[1]]
                                    tablero.tab[inicial[0]][inicial[1]] = None
                                    print("Pieza movida")
                                    return True
                                else:
                                    # Si el destino está ocupado por una pieza del otro jugador se debe poner la pieza en estado muerta y cambiar el color, sino se cancela la jugada
                                    if tablero.tab[final[0]][final[1]].color == 'negro':
                                        tablero.tab[final[0]][final[1]].estado = 'm'
                                        tablero.tab[final[0]][final[1]].estado = 'blanco'
                                        tablero.tab[final[0]][final[1]] = tablero.tab[inicial[0]][inicial[1]]
                                        print("Pieza comida")
                                        return True
                                    else:
                                        # Cancelar jugada porque no puedo comer mi propia pieza
                                        print("Jugada no permitida")
                                        return False
                            else:
                                print("Jugada no permitida")
                                return False
                    else:
                        self.promocion(color, inicial, final)

                elif tablero.tab[inicial[0]][inicial[1]].__class__ is Caballo:
                    # Verifico si la pieza tiene promocion
                    if tablero.tab[inicial[0]][inicial[1]].promocion == 'no':
                        # El caballo puede mover 2 hacia adelante y 1 a los costados
                        if tablero.tab[inicial[0]][inicial[1]].color == 'negro':
                                # Si es una pieza del jugador negro solo puede mover 2 lugares hacia abajo y 1 para la izquierda o derecha
                                if final[0] == inicial[0]+2 and final[1] == inicial[1]+1 or final[0] == inicial[0]+2 and final[0] == inicial[0]-1:
                                    # Si el destino de la ficha esta libre, ponemos el caballo en ese lugar
                                    if tablero.tab[final[0]][final[1]] is None:
                                        tablero.tab[final[0]][final[1]] = tablero.tab[inicial[0]][inicial[1]]
                                        tablero.tab[inicial[0]][inicial[1]] = None
                                        print("Pieza movida")
                                        return True
                                    else:
                                        # Si el destino está ocupado por una pieza del otro jugador se debe poner la pieza en estado muerta y cambiar el color, sino se cancela la jugada
                                        if tablero.tab[final[0]][final[1]].color == 'blanco':
                                            tablero.tab[final[0]][final[1]].estado = 'm'
                                            tablero.tab[final[0]][final[1]].estado = 'negro'
                                            tablero.tab[final[0]][final[1]] = tablero.tab[inicial[0]][inicial[1]]
                                            print("Pieza comida")
                                            return True
                                        else:
                                            # Cancelar jugada porque no puedo comer mi propia pieza
                                            print("Jugada no permitida")
                                            return False
                                else:
                                    print("Jugada no permitida")
                                    return False
                        else:
                            # Si es una pieza del jugador blanco solo puede mover 2 lugares hacia arriba y uno a la derecha o izquierda
                            if final[0] == inicial[0]-2 and final[1] == inicial[1]+1 or final[0] == inicial[0]-2 and final[0] == inicial[0]-1:
                                # Si el destino de la ficha esta libre, ponemos el peon en ese lugar
                                if tablero.tab[final[0]][final[1]] is None:
                                    tablero.tab[final[0]][final[1]] = tablero.tab[inicial[0]][inicial[1]]
                                    tablero.tab[inicial[0]][inicial[1]] = None
                                    print("Pieza movida")
                                    return True
                                else:
                                    # Si el destino está ocupado por una pieza del otro jugador se debe poner la pieza en estado muerta y cambiar el color, sino se cancela la jugada
                                    if tablero.tab[final[0]][final[1]].color == 'negro':
                                        tablero.tab[final[0]][final[1]].estado = 'm'
                                        tablero.tab[final[0]][final[1]].estado = 'blanco'
                                        tablero.tab[final[0]][final[1]] = tablero.tab[inicial[0]][inicial[1]]
                                        print("Pieza comida")
                                        return True
                                    else:
                                        # Cancelar jugada porque no puedo comer mi propia pieza
                                        print("Jugada no permitida")
                                        return False
                            else:
                                print("Jugada no permitida")
                                return False
                    else:
                        self.promocion(color, inicial, final)

                elif tablero.tab[inicial[0]][inicial[1]].__class__ is Alfil:
                    # Verifico si la pieza tiene promocion
                    if tablero.tab[inicial[0]][inicial[1]].promocion == 'no':
                        pass
                    else:
                        self.promocion(color, inicial, final)

                elif tablero.tab[inicial[0]][inicial[1]].__class__ is Torre:
                    # Verifico si la pieza tiene promocion
                    if tablero.tab[inicial[0]][inicial[1]].promocion == 'no':
                        pass
                    else:
                        self.promocion(color, inicial, final)

                elif tablero.tab[inicial[0]][inicial[1]].__class__ is Lancero:
                    # Verifico si la pieza tiene promocion
                    if tablero.tab[inicial[0]][inicial[1]].promocion == 'no':
                        pass
                    else:
                        self.promocion(color, inicial, final)
            else:
                print("Pieza de adversario")
                return False
        else:
            print("No hay pieza para esa ubicacion")
            return False

    def ingresar_pieza(self, color, inicial, final):
        pass

class Pieza:

    def __init__(self, estado, color, nombre):
        self.estado = estado
        self.color = color
        self.nombre = nombre

    def imprimir(self):
        return self.nombre


class Rey(Pieza):

    def __init__(self, estado, color, nombre, jaque):
        super().__init__(estado, color, nombre)  # Pongo super() para usar herencia sin self

        self.estado = estado
        self.nombre = nombre
        self.color = color
        self.jaque = jaque

    def __str__(self):
        return self.nombre


class Lancero(Pieza):

    def __init__(self, estado, promocion, color, nombre):
        super().__init__(estado, color, nombre)  # Pongo super() para usar herencia sin self

        self.estado = estado
        self.nombre = nombre
        self.color = color
        self.promocion = promocion


class Caballo(Pieza):

    def __init__(self, estado, promocion, color, nombre):
        super().__init__(estado, color, nombre)  # Pongo super() para usar herencia sin self

        self.estado = estado
        self.nombre = nombre
        self.color = color
        self.promocion = promocion


class GeneralOro(Pieza):

    def __init__(self, estado, color, nombre):
        super().__init__(estado, color, nombre)  # Pongo super() para usar herencia sin self

        self.estado = estado
        self.nombre = nombre
        self.color = color


class GeneralPlata(Pieza):

    def __init__(self, estado, promocion, color, nombre):
        super().__init__(estado, color, nombre)  # Pongo super() para usar herencia sin self

        self.estado = estado
        self.nombre = nombre
        self.color = color
        self.promocion = promocion


class Alfil(Pieza):

    def __init__(self, estado, promocion, color, nombre):
        super().__init__(estado, color, nombre)  # Pongo super() para usar herencia sin self

        self.estado = estado
        self.nombre = nombre
        self.color = color
        self.promocion = promocion


class Torre(Pieza):

    def __init__(self, estado, promocion, color, nombre):
        super().__init__(estado, color, nombre)  # Pongo super() para usar herencia sin self

        self.estado = estado
        self.nombre = nombre
        self.color = color
        self.promocion = promocion


class Peon(Pieza):

    def __init__(self, estado, promocion, color, nombre):
        super().__init__(estado, color, nombre)  # Pongo super() para usar herencia sin self

        self.estado = estado
        self.nombre = nombre
        self.color = color
        self.promocion = promocion



