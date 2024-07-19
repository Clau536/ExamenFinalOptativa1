INTRODUCCION
El juego "Tres en raya" o "Tic-Tac-Toe", es un juego de mesa clásico que ha cautivado a personas de todas las edades durante muchos años. En este documento, vamos a explorar el proceso de creación de una versión digital de este juego utilizando Python y Pygame. Nuestra meta es crear una experiencia interactiva que refleje la esencia del juego original, mientras aprovechamos las capacidades tecnológicas modernas. A lo largo de este proyecto, cubriremos diversos aspectos del desarrollo de juegos, desde el diseño de la interfaz hasta la implementación de la lógica del juego. Este documento es una guía para cualquier persona interesada en el desarrollo de juegos, independientemente de su nivel de experiencia.
 

ELECCION DE HERRAMIENTA

Pygame

Pygame es un conjunto de módulos del lenguaje Python que permiten la creación de videojuegos en dos dimensiones de una manera sencilla. Está orientado al manejo de sprites.
Gracias al lenguaje, se puede prototipar y desarrollar rápidamente. Esto se puede comprobar en las competiciones que se disputan en línea, donde es cada vez más usado. Los resultados pueden llegar a ser profesionales.



Librería a Utilizar PyGame
Pygame es una librería para el desarrollo de videojuegos en segunda dimensión 2D con el lenguaje de programación Python. Pygame está basada en SDL, que es una librería que nos provee acceso de bajo nivel al audio, teclado, ratón y al hardware gráfico de nuestro ordenador. Es un producto que funciona en cualquier sistema: Mac OS, Windows o Linux.

Caracteristicas


Pygame es una biblioteca de Python que facilita la creación de videojuegos y aplicaciones multimedia interactivas. Ofrece herramientas para manejar gráficos, sonido, entrada de usuario y físicas, permitiendo a los desarrolladores concentrarse en la lógica del juego y la creatividad visual. Además, simplifica la creación de la ventana del juego y es compatible con múltiples plataformas, lo que facilita la distribución de los juegos en diferentes sistemas operativos. En resumen, Pygame es una herramienta poderosa para el desarrollo de juegos en Python.
 
VIDEO JUEGO TRES EN RAYA
El juego "Tres en raya" o "Tic-Tac-Toe", es simple de aprender y jugar, beneficioso para el desarrollo cognitivo al requerir estrategia y anticipación. Además, proporciona estimulación mental y es una actividad social divertida que ofrece entretenimiento rápido y amigable.
Los juegos tradicionales son siempre un éxito asegurado para los niños. Por su sencillez y por los pocos materiales necesarios, juegos como el 'tres en raya' o 'tres en línea' son ideales para empezar a divertirnos con los pequeños. Este juego también es conocido como 'equis punto', 'juego del gato', o Tic-Tac-Toe.
En el tablero formado con dos líneas horizontales y dos verticales que a su vez estarán formando una cuadrícula de nueve espacios. Por turnos, cada jugador deberá poner una X o un O, intentando hacer una línea vertical, horizontal o diagonal.
Aunque sea un juego muy sencillo, este ofrece algunos beneficios para el aprendizaje de los niños. Te contamos algunos:
-	Es un juego para niños de todas las edades.
-	Es muy bueno para estimular la concentración y la atención.
-	Enseña estrategias a los niños.
-	Desarrolla el pensamiento lógico de los niños.
Estructura del Código Importar módulos
import pygame import sys

•	pygame: Es una biblioteca de Python diseñada para crear videojuegos. Proporciona funcionalidades para gráficos, sonido, entrada de usuario, entre otros.
•	sys: Es un módulo que proporciona acceso a algunas variables utilizadas o mantenidas por el intérprete y a funciones que interactúan fuertemente con el intérprete.

Inicialización de Pygame
pygame.init()

•	pygame.init(): Inicializa todos los módulos de pygame que se han importado anteriormente. Es crucial llamar a esta función antes de usar cualquier otro módulo de Pygame.

Definición de colores
NEGRO = (10, 10, 10)
BLANCO = (255, 255, 255)
VIOLETA = (76, 40, 130)
AZUL = (0, 0, 255)
ROJO = (227, 0, 82)
 
•	Se definen varios colores utilizando tuplas RGB para representar sus componentes rojo, verde y azul.

Definición del color de fondo
LILA = (204, 169, 221)

•	Se define el color de fondo llamado "LILA" utilizando una tupla RGB.

Definición del tamaño de pantalla y tamaño de cuadrícula
ANCHO = 300
ALTO = 300
TAM_CUADRO = 100

•	ANCHO y ALTO determinan las dimensiones de la ventana del juego.
•	TAM_CUADRO define el tamaño de los cuadros en la cuadrícula del juego.

Funciones definidas Función dibujar_tablero def dibujar_tablero():
pantalla.fill(LILA)

for x in range(0, ANCHO, TAM_CUADRO):
pygame.draw.line(pantalla, VIOLETA, (50, 50), (250, 250), 3)
pygame.draw.line(pantalla, VIOLETA, (250, 50), (50, 250), 3)
pygame.draw.rect(pantalla, VIOLETA, (50, 50, 200, 200), 2)
pygame.draw.line(pantalla, VIOLETA, (50, 150), (250, 150), 2)
pygame.draw.line(pantalla, VIOLETA, (150, 50), (150, 250), 2)

•	Descripción: Esta función se encarga de dibujar el tablero en la pantalla. Llena la pantalla con el color LILA y luego dibuja líneas y un rectángulo en color VIOLETA para representar el tablero de Tres en Raya.

Función dibujar_x_y_o

def dibujar_x_y_o(row, col, player):
cuadrado_pos = col * TAM_CUADRO + TAM_CUADRO // 2 y_pos = row * TAM_CUADRO + TAM_CUADRO // 2

if player == 1:
pygame.draw.line(pantalla, ROJO, (cuadrado_pos - 30, y_pos - 30), (cuadrado_pos + 30, y_pos + 30), 30)
pygame.draw.line(pantalla, ROJO, (cuadrado_pos + 30, y_pos - 30), (cuadrado_pos - 30, y_pos + 30), 30)
elif player == 2:
pygame.draw.circle(pantalla, AZUL, (cuadrado_pos, y_pos), 30,
30)

•	Descripción: Esta función dibuja una 'X' o un círculo ('O') en la posición especificada (row, col) dependiendo del jugador (player).

Función obtener_celda
def obtener_celda(mouse_pos): x, y = mouse_pos
 
row = y // TAM_CUADRO col = x // TAM_CUADRO return row, col

•	Descripción: Esta función toma la posición del mouse (mouse_pos) y devuelve las coordenadas de la celda de la cuadrícula correspondiente.

Función verificar_ganador
def verificar_ganador(board): for row in range(3):
if board[row][0] == board[row][1] == board[row][2] != 0: return board[row][0]

for col in range(3):
if board[0][col] == board[1][col] == board[2][col] != 0: return board[0][col]

if board[0][0] == board[1][1] == board[2][2] != 0: return board[0][0]
if board[0][2] == board[1][1] == board[2][0] != 0: return board[0][2]

return 0

•	Descripción: Esta función verifica si hay un ganador en el juego de Tres en Raya. Recibe como parámetro board, que es una lista de listas que representa el estado actual del tablero. Comprueba todas las filas, columnas y diagonales para ver si hay tres marcas consecutivas del mismo jugador.

Inicialización de la pantalla y mensaje de bienvenida pantalla = pygame.display.set_mode((ANCHO, ALTO)) pygame.display.set_caption("Tres en Raya")

pantalla.fill(LILA)

font = pygame.font.Font(None, 36)
mensaje_bienvenida = font.render("¡BIENVENIDO AL JUEGO!", True, VIOLETA)
pantalla.blit(mensaje_bienvenida, (ANCHO // 2 - mensaje_bienvenida.get_width() // 2, ALTO // 2 - mensaje_bienvenida.get_height() // 2)) pygame.display.flip()

•	Descripción: Aquí se inicializa la pantalla del juego con las dimensiones especificadas por Ancho y Alto. Se establece el título de la ventana como "Tres en Raya". Se llena la pantalla con el color LILA y se muestra un mensaje de bienvenida centrado usando la fuente definida, en color VIOLETA.

Bucle principal del juego
while jugando:
for event in pygame.event.get(): if event.type == pygame.QUIT:
jugando = False
elif event.type == pygame.MOUSEBUTTONDOWN and ganador == 0: mouse_pos = pygame.mouse.get_pos()
 
row, col = obtener_celda(mouse_pos)

if tablero[row][col] == 0: tablero[row][col] = turno if turno == 1:
turno = 2 else:
turno = 1

pantalla.fill(BLANCO) dibujar_tablero()
for row in range(3):
for col in range(3):
if tablero[row][col] != 0:
dibujar_x_y_o(row, col, tablero[row][col])

ganador = verificar_ganador(tablero) if ganador != 0:
font = pygame.font.Font(None, 36)
texto = font.render(f"¡El jugador {ganador} ha ganado!", True,
NEGRO)
pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2,
ALTO // 2 - texto.get_height() // 2)) pygame.display.flip()
•	Descripción: Este es el bucle principal del juego. Maneja eventos, actualiza el estado del juego y dibuja la pantalla en cada iteración. Se verifica si el jugador ha hecho clic en una celda válida y actualiza el tablero. Luego, verifica si hay un ganador muestra un mensaje en la pantalla. Finalmenteactualiza la pantalla en cada iteración del bucle.

Finalización del juego pygame.quit() sys.exit()

•	Descripción: Cierra adecuadamente Pygame y sale del programa cuando el bucle principal termina (cuando jugando se establece en False o cuando el usuario cierra la ventana del juego).
 
CONCLUSIONES
En conclusión, el juego Tres en raya, con su simplicidad y profundidad estratégica, sigue siendo un pasatiempo atemporal que ha entretenido a generaciones enteras. Su capacidad para desafiar la mente y ofrecer diversión rápida lo convierte en una opción popular tanto para momentos de ocio como para desafíos intelectuales más serios.
el juego del Gato sigue siendo popular debido a su combinación única de simplicidad y desafío estratégico, lo que lo convierte en un pasatiempo perdurable para todas las edades. Además de proporcionar entretenimiento, el Gato ofrece valiosas lecciones de planificación y tácticas, siendo un ejercicio mental beneficioso para los jugadores. Tanto en su forma tradicional como en su versión digital, el Gato continúa siendo una opción excelente para disfrutar con amigos y familiares. Es un recordatorio de que la diversión y el aprendizaje pueden encontrarse incluso en los juegos más simples.
