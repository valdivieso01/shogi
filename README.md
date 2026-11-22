# Shōgi (将棋) - Ajedrez Japonés en Python ⚔️🏯

Implementación completa en consola del **Shōgi (Ajedrez Japonés)** desarrollada en **Python 3** utilizando **NumPy** y programación orientada a objetos (POO). 

Incluye todas las reglas oficiales y complejas del juego tradicional japonés: movimiento individual de piezas, tablero 9x9, sistema de promociones automáticas en zona enemiga, captura y reincorporación (*drops*) de piezas caídas, detección algorítmica de jaque y verificación de jaque mate.

---

## 📸 Capturas del Juego

El juego se ejecuta directamente en la terminal con una cuadrícula 9x9 limpia y descriptiva:

```text
       0    1    2    3    4    5    6    7    8  
  -------------------------------------------------
0 | [L_] [C_] [S_] [G_] [K_] [G_] [S_] [C_] [L_] |
1 | [  ] [R_] [  ] [  ] [  ] [  ] [  ] [B_] [  ] |
2 | [P_] [P_] [P_] [P_] [P_] [P_] [P_] [P_] [P_] |
3 | [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ] |
4 | [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ] |
5 | [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ] |
6 | [P^] [P^] [P^] [P^] [P^] [P^] [P^] [P^] [P^] |
7 | [  ] [B^] [  ] [  ] [  ] [  ] [  ] [R^] [  ] |
8 | [L^] [C^] [S^] [G^] [K^] [G^] [S^] [C^] [L^] |
  -------------------------------------------------
```

---

## ✨ Características y Reglas Implementadas

- 🏯 **Tablero Tradicional 9x9:** Representado como matriz estructurada en NumPy con coordenadas de filas y columnas (0 a 8).
- 🔄 **Reincorporación de Piezas (Drops):** A diferencia del ajedrez occidental, en Shōgi las piezas que capturas del adversario pasan a tu reserva y puedes reintroducirlas al tablero en tu turno como propias.
- ⚡ **Promoción de Piezas:** Al alcanzar las 3 filas más lejanas del rival (filas 0-2 para el jugador blanco, 6-8 para el negro), las piezas pueden ser promovidas, adquiriendo nuevos patrones de movimiento (por ejemplo: la Torre pasa a *Dragón* y el Alfil a *Caballo Dragón*).
- 🛡️ **Detección Algorítmica de Jaque:** Verificación tras cada jugada proyectando todas las líneas de ataque posibles hacia el Rey enemigo.
- 👑 **Verificación de Jaque Mate:** Comprueba exhaustivamente si el Rey bajo amenaza tiene escapatorias posibles, piezas interponibles o capturas disponibles antes de declarar el final de la partida.
- 👥 **Partidas para 2 Jugadores:** Turnos alternados (Jugador Negro vs Jugador Blanco) con validación estricta de movimientos legales.

---

## ♟️ Glosario de Piezas

| Símbolo | Nombre Japonés | Equivalente Occidental | Promoción |
| :---: | :--- | :--- | :--- |
| **K** | *Gyoku / Ōshō* | Rey | — (No promueve) |
| **R** | *Hisha* | Torre | Dragón (+ Rey de un paso) |
| **B** | *Kaku* | Alfil | Caballo Dragón (+ Cruz de un paso) |
| **G** | *Kinshō* | General de Oro | — (No promueve) |
| **S** | *Ginshō* | General de Plata | Promovido a Oro |
| **C** | *Keima* | Caballo | Promovido a Oro |
| **L** | *Kyōsha* | Lancero | Promovido a Oro |
| **P** | *Fuhyō* | Peón | *Tokin* (Promovido a Oro) |

*Nota:* Los sufijos `_` y `^` indican la orientación de las piezas en el tablero según el bando (negras o blancas).

---

## 🏛️ Arquitectura del Código

El proyecto sigue una arquitectura orientada a objetos modular y extensible:

```
shogi/
├── main.py          # Bucle principal del juego, gestión de turnos e inputs
├── tablero.py       # Clase Tablero: matriz NumPy, renderizado, jaque y jaque mate
├── jugador.py       # Clase Jugador: validación de jugadas y piezas capturadas
├── piezas.py        # Jerarquía de clases de piezas y lógica individual de movimiento
├── assets/          # Capturas de pantalla e imágenes de referencia
└── requirements.txt # Dependencias del proyecto
```

---

## 🚀 Instalación y Ejecución

### 1. Clonar el repositorio
```bash
git clone https://github.com/valdivieso01/shogi.git
cd shogi
```

### 2. Crear y activar entorno virtual (Recomendado)
```bash
# En Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# En Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Jugar
```bash
python main.py
```

### 🎮 Cómo ingresar los movimientos:
Cuando sea tu turno, ingresa la fila y columna separadas por un espacio:
1. **Posición de origen:** Por ejemplo, `6 0` para seleccionar la pieza en la fila 6, columna 0.
2. **Posición de destino:** Por ejemplo, `5 0` para avanzar.
3. Si tienes piezas capturadas, el juego te preguntará automáticamente al inicio de tu turno si deseas reincorporar alguna al tablero.

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.
