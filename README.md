Culebrita con Enemigo
Descripción del Proyecto
Este proyecto es un juego sencillo inspirado en el clásico juego de la "Culebrita" (Snake), pero con una mecánica adicional: un enemigo que persigue a la culebra. El jugador controla una culebra que se mueve en una cuadrícula, tratando de comer comida para crecer, mientras evita al enemigo y las colisiones con los bordes de la pantalla o con su propio cuerpo.

El juego incluye música de fondo y efectos de sonido, y permite al jugador volver a jugar o salir cuando pierda. Está desarrollado utilizando la biblioteca Pygame.

Características
Culebrita: Controla una culebra que se mueve por el tablero y crece al comer la comida.
Enemigo: Un enemigo se mueve continuamente en dirección a la culebra, y si toca a la culebra, el juego termina.
Puntaje: El puntaje se basa en la cantidad de comida que ha comido la culebra.
Música y efectos de sonido: Incluye música de fondo y un sonido especial cuando la culebra come.
Menú de inicio: Con opciones para comenzar el juego o salir.
Pantalla de Game Over: Permite al jugador reiniciar el juego o salir después de perder.
Cierre mediante la ventana: El juego se cierra correctamente cuando se pulsa la "X" de la ventana.
Instrucciones de Instalación
Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde python.org.

Instala la biblioteca Pygame utilizando pip. Abre una terminal o línea de comandos y ejecuta el siguiente comando:

bash
Copiar código
pip install pygame
Clona este repositorio o descarga los archivos del proyecto en tu equipo.

Asegúrate de que la estructura del proyecto sea la siguiente:

css
Copiar código
tu_proyecto/
├── resources/
│   ├── background.png
│   ├── Body.png
│   ├── enemy.png
│   ├── Food.png
│   ├── Head.png
│   ├── head.wav
│   └── Intro.mp3
└── tu_script.py
Navega hasta la carpeta del proyecto y ejecuta el archivo principal (tu_script.py):

bash
Copiar código
python tu_script.py
Cómo Jugar
Controles:

Usa las flechas del teclado para mover la culebra:
Flecha izquierda: Moverse hacia la izquierda.
Flecha derecha: Moverse hacia la derecha.
Flecha arriba: Moverse hacia arriba.
Flecha abajo: Moverse hacia abajo.
Objetivo:

Come la comida para hacer crecer a la culebra y aumentar el puntaje.
Evita al enemigo, los bordes de la pantalla y colisionar con tu propio cuerpo.
Pantalla de Game Over:

Al perder, puedes presionar "Enter" para jugar de nuevo o "Q" para salir.
Recursos Utilizados
Pygame: Una biblioteca de Python para desarrollo de videojuegos.



