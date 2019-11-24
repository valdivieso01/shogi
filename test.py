import unittest


from jugador import Jugador
from piezas import *
from tablero import Tablero


class TestBasicos(unittest.TestCase):

    def setUp(self):
        self.j1 = Jugador('negro')
        self.j2 = Jugador('blanco')
        self.tablero = Tablero()

    def test_verificar_tablero(self):
        self.assertEqual(Rey, self.tablero.tab[0][4].__class__)
        self.assertEqual(Rey, self.tablero.tab[8][4].__class__)
        self.assertEqual(Lancero, self.tablero.tab[0][0].__class__)
        self.assertEqual(Lancero, self.tablero.tab[8][0].__class__)
        self.assertEqual(Torre, self.tablero.tab[1][1].__class__)
        self.assertEqual(Torre, self.tablero.tab[7][7].__class__)

    def test_verificar_jugada(self):
        negro_inicial = (int(10),int(0))
        negro_final = (int(-1),int(1))
        self.assertEqual(False, self.j1.validar_posiciones(negro_inicial[0],negro_inicial[1]))
        self.assertEqual(False, self.j1.validar_posiciones(negro_final[0], negro_final[1]))
        negro_inicial = (int(0),int(10))
        negro_final = (int(1),int(-1))
        self.assertEqual(False, self.j1.validar_posiciones(negro_inicial[0],negro_inicial[1]))
        self.assertEqual(False, self.j1.validar_posiciones(negro_final[0], negro_final[1]))
        negro_inicial = (int(10),int(1))
        negro_final = (int(1),int(-1))
        self.assertEqual(False, self.j1.validar_posiciones(negro_inicial[0],negro_inicial[1]))
        self.assertEqual(False, self.j1.validar_posiciones(negro_final[0], negro_final[1]))

    def test_mover_peon(self):
        negro_inicial = (int(2),int(0))
        negro_final = (int(3),int(0))
        self.assertEqual(True, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))
        negro_inicial = (int(3),int(0))
        negro_final = (int(4),int(0))
        self.assertEqual(True, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))
        negro_inicial = (int(4),int(0))
        negro_final = (int(4),int(1))
        self.assertEqual(False, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))

    def test_mover_rey(self):
        negro_inicial = (int(0),int(4))
        negro_final = (int(1),int(4))
        self.assertEqual(True, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))
        negro_inicial = (int(1),int(4))
        negro_final = (int(1),int(5))
        self.assertEqual(True, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))
        negro_inicial = (int(1),int(5))
        negro_final = (int(1), int(4))
        self.assertEqual(True, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))
        negro_inicial = (int(1),int(4))
        negro_final = (int(0),int(4))
        self.assertEqual(True, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))
        negro_inicial = (int(0),int(4))
        negro_final = (int(2),int(4))
        self.assertEqual(False, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))

    def test_mover_general_oro(self):
        negro_inicial = (int(0),int(3))
        negro_final = (int(1),int(3))
        self.assertEqual(True, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))
        negro_inicial = (int(1),int(3))
        negro_final = (int(0),int(3))
        self.assertEqual(True, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))
        negro_inicial = (int(0), int(3))
        negro_final = (int(1), int(4))
        self.assertEqual(True, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))
        negro_inicial = (int(1),int(4))
        negro_final = (int(0),int(3))
        self.assertEqual(False, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))
        negro_inicial = (int(0),int(3))
        negro_final = (int(4),int(3))
        self.assertEqual(False, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))

    def test_mover_general_plata(self):
        negro_inicial = (int(0),int(2))
        negro_final = (int(1),int(3))
        self.assertEqual(True, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))
        negro_inicial = (int(1),int(3))
        negro_final = (int(0),int(2))
        self.assertEqual(True, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))
        negro_inicial = (int(0), int(2))
        negro_final = (int(0), int(3))
        self.assertEqual(False, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))
        negro_inicial = (int(0),int(2))
        negro_final = (int(1),int(2))
        self.assertEqual(True, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))

    def test_mover_caballo(self):
        negro_inicial = (int(2),int(2))
        negro_final = (int(3),int(2))
        self.assertEqual(True, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))
        negro_inicial = (int(0),int(1))
        negro_final = (int(2),int(2))
        self.assertEqual(True, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))
        negro_inicial = (int(2),int(2))
        negro_final = (int(0), int(1))
        self.assertEqual(False, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))
        negro_inicial = (int(0),int(1))
        negro_final = (int(2),int(0))
        self.assertEqual(False, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))

    def test_mover_alfil(self):
        negro_inicial = (int(2),int(6))
        negro_final = (int(3),int(6))
        self.assertEqual(True, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))
        negro_inicial = (int(1),int(7))
        negro_final = (int(2),int(6))
        self.assertEqual(True, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))
        negro_inicial = (int(2),int(6))
        negro_final = (int(6), int(2))
        self.assertEqual(True, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))
        negro_inicial = (int(6),int(2))
        negro_final = (int(8),int(0))
        self.assertEqual(False, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))

    def test_mover_torre(self):
        negro_inicial = (int(1),int(1))
        negro_final = (int(1),int(0))
        self.assertEqual(True, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))
        negro_inicial = (int(1),int(0))
        negro_final = (int(1),int(5))
        self.assertEqual(True, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))
        negro_inicial = (int(2),int(5))
        negro_final = (int(3), int(5))
        self.assertEqual(True, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))
        negro_inicial = (int(1),int(5))
        negro_final = (int(2),int(5))
        self.assertEqual(True, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))
        negro_inicial = (int(2),int(5))
        negro_final = (int(3),int(5))
        self.assertEqual(False, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))

    def test_jaque_mate(self):
        negro_inicial = (int(2), int(4))
        negro_final = (int(3), int(4))
        self.assertEqual(True, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))
        negro_inicial = (int(3), int(4))
        negro_final = (int(4), int(4))
        self.assertEqual(True, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))
        negro_inicial = (int(4), int(4))
        negro_final = (int(5), int(4))
        self.assertEqual(True, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))
        negro_inicial = (int(5), int(4))
        negro_final = (int(6), int(4))
        self.assertEqual(True, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))
        negro_inicial = (int(6), int(4))
        negro_final = (int(7), int(4))
        self.assertEqual(True, self.j1.jugar_pieza(self.tablero, self.j1.color, negro_inicial, negro_final))

if __name__ == "__main__":
    unittest.main()
