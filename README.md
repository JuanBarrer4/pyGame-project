# Culebrita con Enemigo
Descripción del Proyecto
Este proyecto es un juego sencillo inspirado en el clásico juego de la "Culebrita" (Snake), pero con una mecánica adicional: un enemigo que persigue a la culebra. El jugador controla una culebra que se mueve en una cuadrícula, tratando de comer comida para crecer, mientras evita al enemigo y las colisiones con los bordes de la pantalla o con su propio cuerpo.

El juego incluye música de fondo y efectos de sonido, y permite al jugador volver a jugar o salir cuando pierda. Está desarrollado utilizando la biblioteca Pygame.

## Características
Culebrita: Controla una culebra que se mueve por el tablero y crece al comer la comida.
Enemigo: Un enemigo se mueve continuamente en dirección a la culebra, y si toca a la culebra, el juego termina.
Puntaje: El puntaje se basa en la cantidad de comida que ha comido la culebra.
Música y efectos de sonido: Incluye música de fondo y un sonido especial cuando la culebra come.
Menú de inicio: Con opciones para comenzar el juego o salir.
Pantalla de Game Over: Permite al jugador reiniciar el juego o salir después de perder.
Cierre mediante la ventana: El juego se cierra correctamente cuando se pulsa la "X" de la ventana.
## Instrucciones de Instalación
Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde python.org.

Instala la biblioteca Pygame utilizando pip. Abre una terminal o línea de comandos y ejecuta el siguiente comando:

bash
Copiar código
pip install pygame
Clona este repositorio o descarga los archivos del proyecto en tu equipo.
## Descripción del Código: Clases y Funciones Utilizadas
Clases usadas (de Pygame y otras librerías):
pygame.Surface: Se utiliza para manejar las imágenes del juego, como la cabeza y cuerpo de la serpiente, el enemigo, la comida, etc.
pygame.mixer: Se utiliza para cargar y reproducir efectos de sonido y música.
pygame.font: Maneja las fuentes para mostrar el puntaje y otros textos en la pantalla.
math.sqrt: Utilizado para calcular la distancia entre dos puntos (en la detección de colisiones).
random: Utilizado para generar posiciones aleatorias para la comida y el enemigo.
Funciones utilizadas:
display_score(score):

Muestra el puntaje en la esquina superior izquierda de la pantalla.
Utiliza pygame.font.SysFont para cargar la fuente y screen.blit para dibujar el puntaje en la pantalla.
draw_snake(snake_list, direction):

Dibuja la serpiente en la pantalla utilizando imágenes para la cabeza y el cuerpo.
Dependiendo de la dirección de la serpiente, rota la imagen de la cabeza utilizando pygame.transform.rotate.
move_enemy(enemy_pos, snake_head):

Mueve al enemigo hacia la cabeza de la serpiente utilizando un cálculo de distancia.
Normaliza el movimiento para que el enemigo siempre se mueva en dirección a la serpiente con una velocidad constante.
detect_collision(enemy_pos, snake_head):

Detecta si el enemigo ha chocado con la serpiente midiendo la distancia entre sus posiciones.
Utiliza la función math.sqrt para calcular la distancia y retorna True si la distancia es menor al tamaño de un bloque de la serpiente.
game_menu():

Muestra el menú principal del juego con la imagen de fondo (resources/snake.png) y opciones para iniciar el juego o salir.
Escucha eventos del teclado (Enter para iniciar, "Q" para salir) y de la ventana (cerrar la ventana con la "X").
game_loop():

Es el bucle principal del juego donde ocurre la mayoría de la lógica:
Maneja el movimiento de la serpiente.
Detecta colisiones con los bordes de la pantalla, el propio cuerpo de la serpiente y el enemigo.
Controla la lógica de crecimiento de la serpiente cuando come la comida.
Actualiza la pantalla con el estado actual del juego.
Eventos de entrada:

Se manejan dentro de game_loop() y game_menu() para capturar eventos del teclado (flechas de dirección, Enter, "Q") y la "X" de la ventana para salir del juego.
## Cómo Jugar
Controles:

Usa las flechas del teclado para mover la culebra:
Flecha izquierda: Moverse hacia la izquierda.
Flecha derecha: Moverse hacia la derecha.
Flecha arriba: Moverse hacia arriba.
Flecha abajo: Moverse hacia abajo.
## Objetivo:

Come la comida para hacer crecer a la culebra y aumentar el puntaje.
Evita al enemigo, los bordes de la pantalla y colisionar con tu propio cuerpo.
Pantalla de Game Over.
Pygame: Una biblioteca de Python para desarrollo de videojuegos.


