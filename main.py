from jugador import *
from tablero import *

tablero = Tablero()
j1 = Jugador('negro')
j2 = Jugador('blanco')
tablero.imprimir()

while tablero.juego != 'terminado':
    negro_inicial = []
    negro_final = []
    blanco_inicial = []
    blanco_final = []
    turno1 = True
    turno2 = True
    pieza_incorporada = False
    while turno1 is True:
        print("JUGADOR NEGRO")
        print("Piezas capturadas:")
        # Muestro las piezas que el jugador a comido al adversario, si tiene por lo menos una pregunto si quiere reincorporarla
        if tablero.mostrar_piezas_muertas(j1.color):
            entrada = input("Desea incorporar pieza? S/N")
            if entrada == 'S':
                while pieza_incorporada is False:
                    pieza_muerta = input("¿que pieza desea incorporar?")
                    posicion_donde_incorporar = input("Ingrese fila y columna de la posicion donde desea reincorporar (Separados por un espacio):")
                    x, y = (int(item) for item in posicion_donde_incorporar.split())
                    if j1.validar_posiciones(x, y) is True:
                        if tablero.incorporar_piezas(j1.color, pieza_muerta, posicion_donde_incorporar):
                            print("Pieza incorporada")
                            pieza_incorporada = True
                        else:
                            print("No es posible incorporar")
                    else:
                        print("Valores incorrectos")
                tablero.verificar_promociones()
                tablero.imprimir()
                if j1.verificar_jaque(j1, tablero) is True:
                    print("El rey negro está en jaque")
                    if j1.verificar_jaque_mate(j1, tablero) is True:
                        print("jaque mate al rey negro")
                        tablero.juego = 'terminado'
                break  # Al incorporar pierdo turno
        else:
            print("Ninguna")
        ###### TERMINA REINCORPORACION Y EMPIEZA JUGADA ######

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
            print("Jugada realizada")
            turno1 = False
            # Cambio la variable modo control para que el tablero no se modifique durante el control de jaque
            if j1.verificar_jaque(j1, tablero) is True:
                print("El rey blanco está en jaque")
                if j1.verificar_jaque_mate(j1, tablero) is True:
                    print("jaque mate al rey blanco")
                    tablero.juego = 'terminado'
            tablero.verificar_promociones()
            tablero.imprimir()
        else:
            print("No se puede realizar la jugada")
            tablero.imprimir()

    ###### FIN DE TURNO JUGADOR NEGRO ######
    ###### INICIO DE TURNO JUGADOR BLANCO ######

    while turno2 is True:
        print("JUGADOR BLANCO")
        print("Piezas capturadas:")
        # Muestro las piezas que el jugador a comido al adversario, si tiene por lo menos una pregunto si quiere reincorporarla
        if tablero.mostrar_piezas_muertas(j2.color):
            entrada = input("Desea incorporar pieza? S/N")
            if entrada == 'S':
                while pieza_incorporada is False:
                    pieza_muerta = input("¿que pieza desea incorporar?")
                    posicion_donde_incorporar = input("Ingrese fila y columna de la posicion donde desea reincorporar (Separados por un espacio):")
                    x, y = (int(item) for item in posicion_donde_incorporar.split())
                    if j2.validar_posiciones(x, y) is True:
                        if tablero.incorporar_piezas(j2.color, pieza_muerta, posicion_donde_incorporar):
                            print("Pieza incorporada")
                            pieza_incorporada = True
                        else:
                            print("No es posible incorporar")
                            continue
                    else:
                        print("Valores incorrectos")
                tablero.verificar_promociones()
                tablero.imprimir()
                if j2.verificar_jaque(j2, tablero) is True:
                    print("El rey negro está en jaque")
                    if j2.verificar_jaque_mate(j2, tablero) is True:
                        print("jaque mate al rey negro")
                        tablero.juego = 'terminado'
                        break
                break  # Al incorporar pierdo turno
        else:
            print("Ninguna")

        ###### TERMINA REINCORPORACION Y EMPIEZA JUGADA ######

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
            print("Jugada realizada")
            turno2 = False
            # Cambio la variable modo control para que el tablero no se modifique durante el control de jaque
            if j2.verificar_jaque(j2, tablero) is True:
                print("El rey negro está en jaque")
                if j2.verificar_jaque_mate(j2, tablero) is True:
                    print("jaque mate al rey negro")
                    tablero.juego = 'terminado'
                    break
            tablero.verificar_promociones()
            tablero.imprimir()
        else:
            print("No se puede realizar la jugada")
            tablero.imprimir()
