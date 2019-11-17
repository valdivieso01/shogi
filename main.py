from shogy import Tablero, Jugador

tablero = Tablero()
j1 = Jugador('negro')
j2 = Jugador('blanco')

while tablero.juego != 'termiando':
    tablero.imprimir()
    negro_inicial = [None, '']
    negro_final = [None, '']
    blanco_inicial = [None, '']
    blanco_final = [None, '']
    turno1 = True
    turno2 = True
    while turno1 is True:
        entrada = input("Jugador negro, ingrese posicion x e y de pieza a mover (Separados por un espacio):")
        try:
            x, y = (int(item) for item in entrada.split())
        except ValueError:
            print("Valor incorrecto")
            break
        if j1.validar_posiciones(x, y) is True:
            negro_inicial = (x, y)
        else:
            break
        entrada = input("Jugador negro, ingrese posicion x e y de destino de pieza (Separados por un espacio): ")
        try:
            x, y = (int(item) for item in entrada.split())
        except ValueError:
            print("Valor incorrecto")
        if j1.validar_posiciones(x, y) is True:
            negro_final = (x, y)
        else:
            break
        if j1.jugar_pieza(tablero, j1.color, negro_inicial, negro_final) is True:
            turno1 = False

    tablero.imprimir()

    while turno2 is True:
        entrada = input("Jugador blanco, ingrese posicion x e y de pieza a mover (Separados por un espacio):")
        try:
            x, y = (int(item) for item in entrada.split())
        except ValueError:
            print("Valor incorrecto")
            break
        if j2.validar_posiciones(x, y) is True:
            blanco_inicial = (x, y)
        else:
            break
        entrada = input("Jugador blanco, ingrese posicion x e y de destino de pieza (Separados por un espacio): ")
        try:
            x, y = (int(item) for item in entrada.split())
        except ValueError:
            print("Valor incorrecto")
        if j2.validar_posiciones(x, y) is True:
            blanco_final = (x, y)
        else:
            break
        if j2.jugar_pieza(tablero, j2.color, negro_inicial, negro_final) is True:
            turno2 = False

    turno1 = True
    turno2 = True
