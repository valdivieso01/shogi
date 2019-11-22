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
        if tablero.mostrar_piezas_muertas(j1.color):
            entrada = input("Desea incorporar pieza? S/N")
            if entrada == 'S':
                pieza_muerta = input("¿que pieza desea incorporar?")
                if tablero.incorporar_piezas(j1.color, pieza_muerta):
                    print("Pieza incorporada")
                else:
                    print("No hay piezas para incorporar")
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
        # Realizo la jugada, si es una jugada permitida termino el turno e imprimo el tablero
        if j1.jugar_pieza(tablero, j1.color, negro_inicial, negro_final) is True:
            turno1 = False
            # Cambio la variable controlando para que la funcion mover pieza no saque al rey del tablero, luego la vuelvo a dejar en False
            tablero.controlando = True
            if j1.verificar_jaque(j2, tablero) is True:
                print("El rey blanco está en jaque")
            tablero.controlando = False
            tablero.verificar_promociones()
            tablero.imprimir()
        else:
            tablero.imprimir()

    while turno2 is True:
        print("JUGADOR BLANCO")
        print("Piezas capturadas")
        if tablero.mostrar_piezas_muertas(j2.color):
            entrada = input("Desea incorporar pieza? S/N")
            if entrada == 'S':
                pieza_muerta = input("¿que pieza desea incorporar?")
                if tablero.incorporar_piezas(j2.color, pieza_muerta):
                    print("Pieza incorporada")
                else:
                    print("No hay piezas para incorporar")
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
        # Realizo la jugada, si es una jugada permitida termino el turno e imprimo el tablero
        if j2.jugar_pieza(tablero, j2.color, blanco_inicial, blanco_final) is True:
            turno2 = False
            # Cambio la variable controlando para que la funcion mover pieza no saque al rey del tablero, luego la vuelvo a dejar en False
            tablero.controlando = True
            if j2.verificar_jaque(j1, tablero) is True:
                print("El rey negro está en jaque")
            tablero.controlando = False
            tablero.verificar_promociones()
            tablero.imprimir()
        else:
            tablero.imprimir()
