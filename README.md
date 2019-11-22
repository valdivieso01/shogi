# shogi
Juego shogi en python

Funcionalidades implementadas:

<p>
Se define un tablero con piezas y 2 usuarios (negro y blanco).

Las piezas tienen definidas el jugador correspondiente, el estado (muerta o viva), y un nombre utilziado para mostrar en el tablero y si es de tipo promocionada(para la pieza que corresponda).Falta agregar en el tablero algo que identifique de que jugador es.

Cuando se ingresa las posiciones de la pieza a mover y a donde (primero fila y separada por un espacio la columna), sobre esta se verifica que tipo de pieza es y en base a esto los movimientos que puede realizar (los movimientos con promocion estan realizados y el tablero verifica al llegar a las 3 ultimas casillas del rival para pasarla a estado promocionado pero todavia no implemento ninguna manera de cambiar como se muestra en el tablero ese cambio en la pieza). Tambien se detecta si al mover se come alguna pieza y de ser asi esta pasa a ser del otro jugador y la saca del tablero a una lista.

Existe una funcion imprimir tablero que es llamada cada vez que se realiza una jugada valida.

En cada turnos e verifica si el jugador tiene piezas en la lista de piezas muertas a mover, si encuentra pregunta si desea reincorporarla

Esta implemendato utilziando clases para definir tablero, jugadores y piezas. La clase pieza contiene metodos y variables que son heredadas a cada pieza en especial, pero cada pieza cuenta con movimientos individuales que le corresponden
</p> 

Funcionalidades no implementadas:

Todavia faltan las funcionalidades de jaque y jaque mate, estan definidasn pero no terminadas.

