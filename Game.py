import pygame 
import random
import math

# Inicializar Pygame
pygame.init()

# Inicializar el mezclador de música y sonidos
pygame.mixer.init()

# Cargar la canción de fondo
pygame.mixer.music.load("resources/Intro.mp3")
pygame.mixer.music.play(-1)  # Reproducir en bucle

# Cargar el sonido de comer
eat_sound = pygame.mixer.Sound("resources/head.wav")
eat_sound.set_volume(0.5)  # Ajusta el volumen si es necesario

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Culebrita con Enemigo")

# Cargar imágenes
snake_head_img = pygame.image.load("resources/Head.png")  # Imagen de la cabeza
snake_body_img = pygame.image.load("resources/Body.png")  # Imagen del cuerpo
food_img = pygame.image.load("resources/Food.png")  # Imagen de la comida
background_img = pygame.image.load("resources/background.png")  # Imagen del fondo
enemy_img = pygame.image.load("resources/enemy.png")  # Imagen del enemigo

# Escalar imágenes al tamaño deseado
snake_block_size = 20
snake_head_img = pygame.transform.scale(snake_head_img, (snake_block_size, snake_block_size))
snake_body_img = pygame.transform.scale(snake_body_img, (snake_block_size, snake_block_size))
food_img = pygame.transform.scale(food_img, (snake_block_size, snake_block_size))
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))  # Escalar fondo al tamaño de la ventana
enemy_img = pygame.transform.scale(enemy_img, (snake_block_size, snake_block_size))  # Escalar enemigo al tamaño de un bloque

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Velocidad de la culebra
snake_speed = 15
enemy_speed = 5  # Velocidad del enemigo

# Función para mostrar el puntaje
def display_score(score):
    font = pygame.font.SysFont(None, 35)
    value = font.render("Puntuación: " + str(score), True, WHITE)
    screen.blit(value, [0, 0])

# Función para dibujar la culebra con imágenes
def draw_snake(snake_list, direction):
    for index, block in enumerate(snake_list):
        if index == 0:  # Dibuja la cabeza de la culebra
            if direction == "UP":
                head = pygame.transform.rotate(snake_head_img, 90)  # Rotar la cabeza hacia arriba
            elif direction == "DOWN":
                head = pygame.transform.rotate(snake_head_img, -90)  # Rotar la cabeza hacia abajo
            elif direction == "LEFT":
                head = pygame.transform.rotate(snake_head_img, 180)  # Rotar la cabeza hacia la izquierda
            else:
                head = snake_head_img  # No se rota la cabeza, va hacia la derecha
            screen.blit(head, (block[0], block[1]))
        else:  # Dibuja el cuerpo de la culebra
            screen.blit(snake_body_img, (block[0], block[1]))

# Función para mover el enemigo hacia la culebra
def move_enemy(enemy_pos, snake_head):
    enemy_x, enemy_y = enemy_pos
    snake_x, snake_y = snake_head

    # Calcular la dirección en la que debe moverse el enemigo
    distance_x = snake_x - enemy_x
    distance_y = snake_y - enemy_y
    distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

    # Normalizar la dirección y mover el enemigo hacia la serpiente
    if distance != 0:
        enemy_x += (distance_x / distance) * enemy_speed
        enemy_y += (distance_y / distance) * enemy_speed

    return [enemy_x, enemy_y]

# Función para detectar colisión entre la culebra y el enemigo
def detect_collision(enemy_pos, snake_head):
    distance = math.sqrt((enemy_pos[0] - snake_head[0]) ** 2 + (enemy_pos[1] - snake_head[1]) ** 2)
    return distance < snake_block_size  # Colisión si la distancia es menor al tamaño del bloque

# Función para mostrar el menú con imagen de fondo
def game_menu():
    # Cargar la imagen de fondo del menú
    menu_background_img = pygame.image.load("resources/snake.png")
    menu_background_img = pygame.transform.scale(menu_background_img, (WIDTH, HEIGHT))  # Escalar al tamaño de la pantalla

    waiting = True
    while waiting:
        screen.blit(menu_background_img, (0, 0))  # Dibujar la imagen de fondo en el menú
        font = pygame.font.SysFont(None, 55)
        text_play = font.render("Presiona Enter para Iniciar", True, WHITE)
        text_quit = font.render("Presiona Q para Salir", True, WHITE)

        screen.blit(text_play, [150, 250])
        screen.blit(text_quit, [150, 350])
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()  # Cerrar completamente el juego
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False  # Iniciar el juego
                if event.key == pygame.K_q:  # Pulsar 'Q' para salir
                    pygame.quit()
                    quit()  # Cerrar completamente el juego

# Función principal del juego
def game_loop():
    game_over = False
    game_close = False

    # Posición inicial de la culebra
    x = WIDTH // 2
    y = HEIGHT // 2
    x_change = 0
    y_change = 0
    direction = "RIGHT"  # Dirección inicial

    # Segmentos de la culebra (cabeza al inicio, luego los segmentos del cuerpo)
    snake_list = []
    snake_length = 1

    # Comida inicial
    food_x = round(random.randrange(0, WIDTH - snake_block_size) / snake_block_size) * snake_block_size
    food_y = round(random.randrange(0, HEIGHT - snake_block_size) / snake_block_size) * snake_block_size

    # Posición inicial del enemigo
    enemy_x = random.randint(0, WIDTH - snake_block_size)
    enemy_y = random.randint(0, HEIGHT - snake_block_size)
    enemy_pos = [enemy_x, enemy_y]

    clock = pygame.time.Clock()

    while not game_over:
        while game_close:
            # Detener la música cuando el juego se cierra (pierdes)
            pygame.mixer.music.stop()

            screen.fill(BLACK)
            font = pygame.font.SysFont(None, 50)

            # Dividir el mensaje en varias líneas para que no se corte
            message1 = font.render("Perdiste.", True, RED)
            message2 = font.render("Presiona Enter para jugar de nuevo.", True, RED)
            message3 = font.render("Presiona Q para Salir.", True, RED)

            # Mostrar las líneas de texto en posiciones adecuadas
            screen.blit(message1, [WIDTH // 4, HEIGHT // 3])
            screen.blit(message2, [WIDTH // 4 - 80, HEIGHT // 3 + 50])
            screen.blit(message3, [WIDTH // 4, HEIGHT // 3 + 100])

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Salir cuando se presione la "X" de la ventana
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # Reiniciar la música cuando el juego vuelve a comenzar
                        pygame.mixer.music.play(-1)
                        game_loop()
                    if event.key == pygame.K_q:  # Pulsar 'Q' para salir
                        pygame.quit()
                        quit()

        # Eventos de movimiento
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Salir cuando se presione la "X" de la ventana
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -snake_block_size
                    y_change = 0
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = snake_block_size
                    y_change = 0
                    direction = "RIGHT"
                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -snake_block_size
                    x_change = 0
                    direction = "UP"
                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = snake_block_size
                    x_change = 0
                    direction = "DOWN"

        # Actualizar la posición de la cabeza
        x += x_change
        y += y_change

        # Chequear si la culebra toca los bordes del mapa
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        # Añadir la posición de la cabeza al principio de la lista
        snake_head = [x, y]
        snake_list.insert(0, snake_head)  # Inserta la cabeza al inicio de la lista

        # Controlar el tamaño de la culebra (si es más larga, eliminar el último segmento)
        if len(snake_list) > snake_length:
            snake_list.pop()  # Elimina el último segmento para mantener la longitud correcta

        # Verificar colisiones con el propio cuerpo
        for block in snake_list[1:]:  # No incluir la cabeza en la verificación
            if block == snake_head:
                game_close = True

        # Mover el enemigo hacia la culebra
        enemy_pos = move_enemy(enemy_pos, snake_head)

        # Detectar colisión con el enemigo
        if detect_collision(enemy_pos, snake_head):
            game_close = True

        # Dibujar todo el juego
        screen.blit(background_img, (0, 0))  # Dibuja el fondo en la posición (0, 0)
        screen.blit(food_img, (food_x, food_y))  # Dibuja la comida
        draw_snake(snake_list, direction)  # Dibuja la culebra
        screen.blit(enemy_img, (enemy_pos[0], enemy_pos[1]))  # Dibuja el enemigo
        display_score(snake_length - 1)  # Muestra el puntaje

        # Actualizar la pantalla
        pygame.display.update()

        # Si la culebra come la comida
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - snake_block_size) / snake_block_size) * snake_block_size
            food_y = round(random.randrange(0, HEIGHT - snake_block_size) / snake_block_size) * snake_block_size
            snake_length += 1  # Aumenta la longitud de la culebra
            eat_sound.play()  # Reproduce el sonido de comer

        # Controlar la velocidad del juego
        clock.tick(snake_speed)

    pygame.quit()

# Ejecutar el menú y luego el juego
game_menu()
game_loop()
