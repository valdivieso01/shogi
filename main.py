from jugador import *
from tablero import *

tablero = Tablero()
j1 = Jugador('negro')
j2 = Jugador('blanco')
tablero.imprimir()


while tablero.juego != 'termiando':
    negro_inicial = []
    negro_final = []
    blanco_inicial = []
    blanco_final = []
    turno1 = True
    turno2 = True
    while turno1 is True:
        print("JUGADOR NEGRO")
        entrada = input("Desea incorporar pieza? S/N")
        if entrada == 'S':
            tablero.incorporar_piezas(j1.color)
        entrada = input("Ingrese fila y columna de pieza a mover (Separados por un espacio):")
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
        entrada = input("Ingrese fila y columna de destino de pieza (Separados por un espacio): ")
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
                tablero.imprimir()
            else:
                tablero.imprimir()
        else:
            print("Jugador en jaque, mueva el rey")
            if j1.jugar_pieza_en_jaque(tablero, j1.color, negro_inicial, negro_final) is True:
                turno1 = False
                tablero.imprimir()
            else:
                tablero.imprimir()

    while turno2 is True:
        print("JUGADOR BLANCO")
        print("Piezas capturadas")
        entrada = input("Desea incorporar pieza? S/N")
        if entrada == 'S':
            tablero.incorporar_piezas(j1.color)
        # Listo las piezas que el jugador a comido al adversario
        entrada = input("Ingrese fila y columna de pieza a mover (Primero fila y luego columna, separados por un espacio):")
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
        entrada = input("Ingrese fila y columna de destino de pieza (Primero fila y luego columna, separados por un espacio): ")
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
                tablero.imprimir()
            else:
                tablero.imprimir()
        else:
            print("Jugador en jaque, mueva el rey")
            if j2.jugar_pieza_en_jaque(tablero, j2.color, blanco_inicial, blanco_final) is True:
                turno2 = False
                tablero.imprimir()
            else:
                tablero.imprimir()
