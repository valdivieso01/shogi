# Juego shogi desarrollado en python 

# Librerias utilizadas: numpy

# Ejecucion

Descargar repositorio y desde consola correr el comando python main.py

# Como jugar

Al ingresar comienza jugando el jugador negro(las piezas en la parte superior)
Se ingresan dos valores que corresponden primero a la fila y luego la columna con un espacio entre los dos valores

![ScreenShot](https://github.com/valdivieso01/shogi/blob/develop/assets/Screenshot_2.png)
![ScreenShot](https://github.com/valdivieso01/shogi/blob/develop/assets/Screenshot_1.png)

Luego el turno pasa automaticamente al jugador blanco (las piezas en la parte inferior)
Se ingresan dos valores que corresponden primero a la fila y luego la columna con un espacio entre los dos valores

Cuando una de las piezas llega a las 3 filas del adversario esta pasa a ser una pieza promocionada

Para reingresar piezas el juego pregunta automaticamente si desea ingresar cuando es posible

Cuando el rey está en jaque el juego avisa por pantalla con un mensaje y cuadno uno de los reyes queda en jaque mate la partida termina

# Funcionalidades implementadas:

<p>

El tablero se genera con las piezas de los jugadores donde en la aprte superior se encuentran las piezas negras y en la inferior las blancas, comienza a mover el jugador negro.

El programa cuenta con un archivo main donde se instancian los objetos tablero y jugador (blanco y negro). Luego se implementa la logica de los turnos y se llama a las funciones de verificacionde promociones y verificaciond e jaque. los demas archivos se utilzian apra definir las clases y metodos  para piezas, jugador y tablero.

Las piezas tienen definidas el color del jugador correspondiente, el estado de promocion (verdadero o falso) y un nombre utilziado para mostrar en el tablero.

Cuando se ingresa las posiciones de la pieza a mover y a donde (primero fila y separada por un espacio la columna), sobre esta se verifica que tipo de pieza es y en base a esto los movimientos que puede realizar (los movimientos con promocion estan realizados y el tablero verifica al llegar a las 3 ultimas casillas del rival para pasarla a estado promocionado. Tambien se detecta si al mover se come alguna pieza y de ser asi esta pasa a ser del otro jugador y la saca del tablero a una lista.

Existe una funcion imprimir tablero que es llamada cada vez que se realiza una jugada valida.

En cada turnos se verifica si el jugador tiene piezas en la lista de piezas muertas a mover, si encuentra pregunta si desea reincorporarla

Esta implemendato utilziando clases para definir tablero, jugadores y piezas. La clase pieza contiene metodos y variables que son heredadas a cada pieza en especial, pero cada pieza cuenta con movimientos individuales que le corresponden

La funciona para verificar jaque se implemento realizando un analisis en el tablero luego de cada jugada para verificar si en la siguiente jugada el rey puede ser comido, dentro de la funcion se modifica la variable de control para que las piezas no se muevan durante el control

La funcion jaque mate identifica el rey contrario al jugador que realizo la ultima jugada y controla que al hacer todos los movimientos posibles el rey siga en jaque.

La reincorporacion de piezas se realiza segun las reglas definidas por el juego
</p> 

