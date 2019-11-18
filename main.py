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
            x1, y1 = (int(item) for item in entrada.split())
        except ValueError:
            print("Valor incorrecto")
            continue
        if j1.validar_posiciones(x1, y1) is True:
            negro_inicial = (x1, y1)
        else:
            print("Valor fuera de tablero")
            continue
        entrada = input("Jugador negro, ingrese posicion x e y de destino de pieza (Separados por un espacio): ")
        try:
            x1, y1 = (int(item) for item in entrada.split())
        except ValueError:
            print("Valor incorrecto")
            continue
        if j1.validar_posiciones(x1, y1) is True:
            negro_final = (x1, y1)
        else:
            print("Valor fuera de tablero")
            continue
        if tablero.verificar_jaque(j1.color) is False:
            if j1.jugar_pieza(tablero, j1.color, negro_inicial, negro_final) is True:
                turno1 = False
            else:
                tablero.imprimir()
        else:
            if j1.jugar_pieza_en_jaque(tablero, j1.color, negro_inicial, negro_final) is True:
                turno1 = False
            else:
                tablero.imprimir()

    tablero.imprimir()

    while turno2 is True:
        entrada = input("Jugador blanco, ingrese posicion x e y de pieza a mover (Separados por un espacio):")
        try:
            x2, y2 = (int(item) for item in entrada.split())
        except ValueError:
            print("Valor incorrecto")
            continue
        if j2.validar_posiciones(x2, y2) is True:
            blanco_inicial = (x2, y2)
        else:
            print("Valor fuera de tablero")
            continue
        entrada = input("Jugador blanco, ingrese posicion x e y de destino de pieza (Separados por un espacio): ")
        try:
            x2, y2 = (int(item) for item in entrada.split())
        except ValueError:
            print("Valor incorrecto")
            continue
        if j2.validar_posiciones(x2, y2) is True:
            blanco_final = (x2, y2)
        else:
            print("Valor fuera de tablero")
            continue
        if tablero.verificar_jaque(j2.color) is False:
            if j2.jugar_pieza(tablero, j2.color, blanco_inicial, blanco_final) is True:
                turno2 = False
            else:
                tablero.imprimir()
        else:
            if j2.jugar_pieza_en_jaque(tablero, j2.color, blanco_inicial, blanco_final) is True:
                turno2 = False
            else:
                tablero.imprimir()
