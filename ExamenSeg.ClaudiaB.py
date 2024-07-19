import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
NEGRO = (10, 10, 10)
BLANCO = (255, 255, 255)
VIOLETA= (76, 40, 130)
AZUL = (0, 0, 255)
ROJO = (227, 0, 82)

# Color de fondo
LILA= (204, 169, 221)

# Definir tamaño de pantalla y cuadrícula
ANCHO = 300
ALTO = 300
TAM_CUADRO = 100




# Definir funciones
def dibujar_tablero():

    pantalla.fill(LILA)

    for x in range(0, ANCHO, TAM_CUADRO):
        
        pygame.draw.line(pantalla, VIOLETA, (50, 50), (250, 250), 3)
        pygame.draw.line(pantalla, VIOLETA, (250, 50), (50, 250), 3)
        pygame.draw.rect(pantalla, VIOLETA, (50, 50, 200, 200), 2)
        pygame.draw.line(pantalla, VIOLETA, (50, 150), (250, 150), 2)
        pygame.draw.line(pantalla, VIOLETA, (150, 50), (150, 250), 2)
    

def dibujar_x_y_o(row, col, player):
    cuadrado_pos = col * TAM_CUADRO + TAM_CUADRO // 2
    y_pos = row * TAM_CUADRO + TAM_CUADRO // 2

    if player == 1:
        pygame.draw.line(pantalla, ROJO, (cuadrado_pos - 30, y_pos - 30), (cuadrado_pos + 30, y_pos + 30), 30)
        pygame.draw.line(pantalla, ROJO, (cuadrado_pos + 30, y_pos - 30), (cuadrado_pos - 30, y_pos + 30), 30)
    elif player == 2:
        pygame.draw.circle(pantalla, AZUL, (cuadrado_pos, y_pos), 30, 30)

def obtener_celda(mouse_pos):
    x, y = mouse_pos
    row = y // TAM_CUADRO
    col = x // TAM_CUADRO
    return row, col

def verificar_ganador(board):
    # Verificar filas
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != 0:
            return board[row][0]

    # Verificar columnas
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            return board[0][col]

    # Verificar diagonales
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]

    return 0

# Inicializar pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Tres en Raya")

# Mostrar mensaje de bienvenida
pantalla.fill(LILA)

font = pygame.font.Font(None, 36)
mensaje_bienvenida = font.render("¡BIENVENIDO AL JUEGO!", True, VIOLETA)
pantalla.blit(mensaje_bienvenida, (ANCHO // 2 - mensaje_bienvenida.get_width() // 2, ALTO // 2 - mensaje_bienvenida.get_height() // 2))
pygame.display.flip()

# Esperar unos segundos antes de cerrar
pygame.time.wait(3000)


# Inicializar variables del juego
tablero = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
turno = 1
ganador = 0
jugando = True

# Bucle principal del juego
while jugando:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
        elif event.type == pygame.MOUSEBUTTONDOWN and ganador == 0:
            mouse_pos = pygame.mouse.get_pos()
            row, col = obtener_celda(mouse_pos)

            if tablero[row][col] == 0:
                tablero[row][col] = turno
                if turno == 1:
                    turno = 2
                else:
                    turno = 1

    # Actualizar pantalla
    pantalla.fill(BLANCO)
    dibujar_tablero()
    for row in range(3):
        for col in range(3):
            if tablero[row][col] != 0:
                dibujar_x_y_o(row, col, tablero[row][col])

    ganador = verificar_ganador(tablero)
    if ganador != 0:
        font = pygame.font.Font(None, 36)
        texto = font.render(f"¡El jugador {ganador} ha ganado!", True, NEGRO)
        pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2 - texto.get_height() // 2))

    pygame.display.flip()

# Salir del juego
pygame.quit()
sys.exit()