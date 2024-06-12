# Minimax algorithm - Simulación Estratégica del Gato y el Ratón

## ¡Atención! Cuanto mejor leas las instrucciones, más fácil será el ejercicio. ¡Léelas como un ninja descifrando un pergamino secreto! 🥷


### La tecnología que debes utilizar en este ejercicio es Python 🐍

Implementa el algoritmo Minimax para simular estrategias de un gato y un ratón. El algoritmo Minimax es comúnmente utilizado en juegos de dos jugadores, como el ajedrez, para encontrar la mejor estrategia posible. En este ejercicio, el ratón debe ser capaz de evadir al gato de manera inteligente, y el gato debe anticipar los movimientos del ratón.

### Simulación de Estrategias:
Define un entorno en el que el gato y el ratón interactúan. Por ejemplo, un tablero o una cuadrícula, debes establecer reglas claras para el movimiento del gato y el ratón. 
Implementa el algoritmo de manera que el ratón pueda evadir al gato y el gato pueda anticipar los movimientos del ratón. Primeramente define que el ratón evada al gato de forma aleatoria, una vez que logres implementarlo haz que el ratón evada al gato de forma inteligente, esto podrías hacerlo por ejemplo utilizando una ruta de escape para el ratón. 
Por otra parte, el gato debe intentar predecir y reaccionar a los movimientos del ratón, implementa estrategias para que el gato atrape al ratón.

### Definición del Tablero de Juego:
Utiliza una estructura de datos bidimensional para modelar el tablero, puedes usar una matriz de enteros o una clase personalizada que represente el estado del juego. Define las dimensiones del tablero y el punto de inicio para el gato y el ratón.
Para los movimientos, puedes utilizar movimientos en las cuatro direcciones (arriba, abajo, izquierda, derecha) también puedes utilizar movimientos de ocho direcciones o en diagonal si lo deseas.

### Algoritmo Minimax:
Debes considerar el turno de cada jugador (gato y ratón). El ratón busca maximizar sus movimientos para evitar al gato, mientras que el gato busca minimizar la distancia para atrapar al ratón.
Cada nodo en el árbol Minimax representa un estado del juego, y cada rama representa un posible movimiento.

## Consideraciones para el ejercicio:
- Implementa la solución y luego optimizala.
    - Separa el problema en partes pequeñas.
    - Define el tablero.
    - Implementa los movimientos del ratón y el gato.
    - Implementa el algoritmo Minimax.
    - Define condiciones de finalización del juego.
    - Optimiza el programa.
- Realiza pruebas con diferentes tamaños de tablero.
- Utiliza estructuras de datos adecuadas para mejorar la velocidad del programa.
- Mientras cumplas con los requisitos anteriores, siente la libertad de ser creativo en tu implementación. Piensa, ¿Hay características únicas o interesantes que podrías añadir al juego?
