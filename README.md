# shogi
Juego shogi en python

Funcionalidades implementadas:

<p>
Se define un tablero con piezas y 2 usuarios (negro y blanco).

Las piezas tienen definidas el jugador correspondiente, el estado (muerta o viva), y un nombre utilziado para mostrar en el tablero y si es de tipo promocionada(para la pieza que corresponda).Falta agregar en el tablero algo que identifique de que jugador es.

Cuando se ingresa las posiciones de la pieza a mover y a donde, sobre esta se verifica que tipo de pieza es y en base a esto los movimientos que puede realizar (hasta el momento solo esta emplementado el movimiento de peon con y sin promocion). Tambien se detecta si al mover se come alguna pieza y de ser asi esta pasa a ser del otro jugador en estado muerta.

Existe una funcion imprimir tablero que es llamada cada vez que se realiza una jugada valida.

Esta implemendato utilziando clases para definir tablero, jugadores y piezas.

El archivo test contiene los test para validar movimientos de piezas
</p> 
