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

            [None, Alfil('v', 'no', 'blanco', 'B'), None, None, None, None, None, Torre('v', 'no', 'blanco', 'R'), None],

            [Lancero('v', 'no', 'blanco', 'L'), Caballo('v', 'no', 'blanco', 'N'), GeneralPlata('v', 'no', 'blanco', 'S'),
             GeneralOro('v', 'blanco', 'G'), Rey('v', 'blanco', 'K', False), GeneralOro('v', 'blanco', 'G'),
             GeneralPlata('v', 'no', 'blanco', 'S'), Caballo('v', 'no', 'blanco', 'N'), Lancero('v', 'no', 'blanco', 'L')],
        ]

        self.tab = numpy.array(self.t)

    def imprimir(self):
        k = 0
        print("| | ", end='')
        for k in range(len(self.columna)):
            print('|'+self.fila[k]+'| ', end='')
        print("")
        k = 0
        for i in self.tab:
            print('|'+self.fila[k]+'| ', end='')
            for j in i:
                if j:
                    print('|'+j.nombre+'| ', end='')
                else:
                    print('| | ', end='')
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

    def hacer_jugada(self, inicial, final):
        # Si es una pieza entro
        if tablero.tab[inicial[0]][inicial[1]]:
            # Verifico que tipo de pieza es para despues analizar el movimiento
            print(tablero.tab[inicial[0]][inicial[1]])
            if tablero.tab[inicial[0]][inicial[1]].__class__ is Peon:
                # Verifico en este caso si solo puede mover un lugar hacia adelante (Suponiendo que no es pieza con promocion)
                print(final[0])
                print(inicial[0])
                print(inicial[1])
                print(final[1]+1)
                if final[1] == inicial[1] and final[0] == inicial[0]+1:
                    print("entra")
                    #Verificamos que la posicion final este libre y asignamos la nueva posicion
                    if tablero.tab[final[0]+1][final[1]] == None:
                        tablero.tab[final[0]][final[1]] = tablero.tab[inicial[0]][inicial[1]]
                        tablero.tab[inicial[0]][inicial[1]] = None


class Pieza:

    def __init__(self, estado,color, nombre):
        self.estado = estado
        self.color = color
        self.nombre = nombre

    def imprimir(self):
        return self.nombre


class Rey(Pieza):

    def __init__(self, estado, color, nombre, jaque):
        super().__init__(estado, color, nombre)  # Pongo super() para usar herencia sin self

        self.nombre = nombre
        self.color = color
        self.jaque = jaque

    def __str__(self):
        return self.nombre


class Lancero(Pieza):

    def __init__(self, estado, promocion, color, nombre):
        super().__init__(estado, color, nombre)  # Pongo super() para usar herencia sin self

        self.nombre = nombre
        self.color = color
        self.promocion = promocion


class Caballo(Pieza):

    def __init__(self, estado, promocion, color, nombre):
        super().__init__(estado, color, nombre)  # Pongo super() para usar herencia sin self

        self.nombre = nombre
        self.color = color
        self.promocion = promocion

class GeneralOro(Pieza):

    def __init__(self, estado, color, nombre):
        super().__init__(estado, color, nombre)  # Pongo super() para usar herencia sin self

        self.nombre = nombre
        self.color = color


class GeneralPlata(Pieza):

    def __init__(self, estado, promocion, color, nombre):
        super().__init__(estado, color, nombre)  # Pongo super() para usar herencia sin self

        self.nombre = nombre
        self.color = color
        self.promocion = promocion


class Alfil(Pieza):

    def __init__(self, estado, promocion, color, nombre):
        super().__init__(estado, color, nombre)  # Pongo super() para usar herencia sin self

        self.nombre = nombre
        self.color = color
        self.promocion = promocion


class Torre(Pieza):

    def __init__(self, estado, promocion, color, nombre):
        super().__init__(estado, color, nombre)  # Pongo super() para usar herencia sin self

        self.nombre = nombre
        self.color = color
        self.promocion = promocion


class Peon(Pieza):

    def __init__(self, estado, promocion, color, nombre):
        super().__init__(estado, color, nombre)  # Pongo super() para usar herencia sin self

        self.nombre = nombre
        self.color = color
        self.promocion = promocion


j1 = Jugador('negro')
j2 = Jugador('blanco')
tablero = Tablero()

while tablero.juego != 'termiando':
    tablero.imprimir()
    negro_inicial = [None,'']
    negro_final = [None, '']
    blanco_inicial = [None, '']
    blanco_final = [None, '']
    if not tablero.verificar_jaque_negro():
        entrada = input("Jugador negro, ingrese posicion x e y de pieza a mover (Separados por un espacio):")
        x, y = (int(item) for item in entrada.split())
        negro_inicial = (x, y)
        entrada = input("Jugador negro, ingrese posicion x e y de destino de pieza (Separados por un espacio): ")
        x, y = (int(item) for item in entrada.split())
        negro_final = (x, y)
        try:
            j1.hacer_jugada(negro_inicial, negro_final)
        except ValueError:
            print("La jugada es incorrecta")
    tablero.imprimir()
    if not tablero.verificar_jaque_blanco():
        entrada = input("Jugador blanco, ingrese posicion x e y de pieza a mover (Separados por un espacio): ")
        x, y = (int(item) for item in entrada.split())
        blanco_inicial = (x, y)
        entrada = input("Jugador negro, ingrese posicion x e y de destino de pieza (Separados por un espacio): ")
        x, y = (int(item) for item in entrada.split())
        blanco_final = (x, y)
        try:
            j2.hacer_jugada(blanco_inicial, blanco_final)
        except ValueError:
            print("La jugada es incorrecta")

