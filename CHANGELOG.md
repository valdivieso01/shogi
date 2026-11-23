# Changelog 📜

Todos los cambios notables y correcciones de reglas en este proyecto se registrarán en este archivo.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y este proyecto se adhiere al versionado semántico.

---

## [1.1.1] - 2026-11-23

### 🐛 Corregido (Bugs de Movimiento y Reglas)
- **Movimiento del General de Plata (*Ginshō*):** Se corrigió la condición de diagonal delantera derecha para el jugador negro y blanco (`posicion_final[1] == posicion_inicial[1] + 1`), así como el parámetro `posicion_final` en `mover_pieza` para el jugador blanco.
- **Movimiento de Torre Coronada (*Dragón* / *Ryūō*):** Se corrigió el desplazamiento ortogonal en `mover_como_torre_coronada` (`piezas.py`), que anteriormente iteraba en diagonal por error, manteniendo además el paso de 1 casilla en las 4 diagonales.
- **Retorno de piezas promocionadas (*Keima* y *Kyōsha*):** Se añadió el `return` faltante al delegar en `mover_pieza_promocionada` dentro de `mover_caballo` y `mover_lancero`.
- **Límites de tablero en piezas deslizantes:** Se agregaron validaciones de rango (`0 <= nr < 9` y `0 <= nc < 9`) en `Alfil`, `Torre` y `Lancero` (normales y coronados) para evitar `IndexError` durante la proyección de líneas de ataque en `verificar_jaque`.
- **Verificación de clase en promociones y *Uchifuzume*:** En `tablero.py`, se corrigió la comparación de clase para `GeneralOro` y `Rey` en `verificar_promociones` y la validación de jaque mate por reincorporación de peón (*Uchifuzume*) en `reintroducir_pieza`, aceptando coordenadas tanto en cadena (`"3 0"`) como en tupla (`(3, 0)`).

---

## [1.1.0] - 2026-11-22

### 🐛 Corregido (Bugs y Reglas de Movimiento)
- **Movimiento lateral del Caballo (*Keima*):** Se corrigió la comparación de coordenadas en `mover_caballo` (`piezas.py`), donde un error tipográfico comparaba la fila dos veces en lugar de la columna (`posicion_final[0]` por `posicion_final[1]`). Ahora el caballo puede saltar tanto hacia adelante-derecha como hacia adelante-izquierda.
- **Movimiento de piezas promovidas como General de Oro:** En `mover_como_general_oro` (`piezas.py`) para el jugador blanco, se eliminó la comprobación duplicada a la diagonal derecha y se habilitó la diagonal hacia adelante-izquierda (`posicion_inicial[1] - 1`).
- **Prevención de `IndexError` en Nifu:** En `reintroducir_pieza` (`tablero.py`), se eliminó la iteración `fila + j` que desbordaba el índice del tablero (`IndexError: out of bounds`) al colocar peones en filas intermedias o bajas.

### ♟️ Reglas Oficiales de Shōgi Añadidas / Alineadas
- **Regla estricta de *Nifu* (二歩 - Dos Peones):** La validación ahora comprueba exhaustivamente toda la columna (filas 0 a 8) y permite reincorporar un peón si los otros peones de la columna ya se encuentran promovidos (*Tokin*), tal como dictan las reglas oficiales.
- **Pérdida de promoción al capturar:** En `mover_pieza` (`piezas.py`), cuando un jugador captura una pieza enemiga que estaba promovida (*Tokin*, *Dragón*, etc.), su estado se reinicia a `promocion = False`. Las piezas caídas vuelven a la mano en su forma básica antes de ser reincorporadas.
- **Restricción de reincorporación de Caballos (*Keima*):** Ahora se prohíbe reincorporar un caballo en casillas donde no tiene jugadas legales posibles: filas 7 y 8 para el jugador negro, y filas 0 y 1 para el jugador blanco.
- **Protección contra movimientos fuera de rango en Jaque Mate:** Se añadió verificación de límites de fila (`fila > 0` y `fila < 8`) al comprobar si un peón colocado frente al rey lo deja en jaque mate inmediato (*Uchifuzume*).

### 🛡️ Robustez y UX
- **Manejo seguro de inputs:** En `main.py`, se envolvieron las entradas de reincorporación en bloques `try/except ValueError` para evitar que el juego se interrumpa si el usuario presiona Enter sin coordenadas o escribe texto inválido.
- **Cancelación limpia de drops:** Se añadió la instrucción `break` para salir del submenú de incorporación inmediatamente cuando el usuario tipea `"Salir"`.

### 📚 Documentación
- Creación de este archivo `CHANGELOG.md`.
- Rediseño completo del `README.md` con glosario de piezas, diagrama de tablero ASCII, arquitectura POO y guía de instalación.
- Inclusión de `requirements.txt` (`numpy>=1.20.0`).
