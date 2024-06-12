import math
import pygame
import random

# Variables globales
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 750
COLUMNAS = 10
FILAS = 10
CELL_SIZE = min(SCREEN_WIDTH // COLUMNAS, SCREEN_HEIGHT // FILAS)


class Color:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BROWN = (153, 76, 0)
    YELLOW = (255, 255, 0)


# Cantidad de elementos no atravesables
OBSTACULOS = 15
obstaculos = set()

pygame.init()
canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("🐀 vs 🐈‍⬛")


class Entidad:
    es_visible = True

    def __init__(self, x: int, y: int, color) -> None:
        self.x = x
        self.y = y
        self.color = color

    def get_posicion(self) -> tuple:
        return self.x, self.y


class Jugador(Entidad):
    def __init__(self, posicion: tuple, color: tuple) -> None:
        super().__init__(posicion[0], posicion[1], color=color)

    def mover(self, movimiento: str) -> None:
        coordenada = Utiles.mapear_movimiento(movimiento)
        self.x += coordenada[0]
        self.y += coordenada[1]


class IA(Jugador):
    def __init__(self, posicion: tuple, color: tuple) -> None:
        super().__init__(posicion, color=color)

    @staticmethod
    def mover_evaluacion(posicion, movimiento) -> tuple:
        coordenada = Utiles.mapear_movimiento(movimiento)
        new_x, new_y = posicion
        new_x += coordenada[0]
        new_y += coordenada[1]
        return new_x, new_y

    @staticmethod
    def movimientos_posibles(posicion: tuple) -> list:
        movimientos = ["ARRIBA", "ABAJO", "DERECHA", "IZQUIERDA"]
        return [mov for mov in movimientos if Utiles.evaluar_movimiento(posicion, mov)]

    def __minimax(self, jugador: tuple, objetivo: tuple, maximizar: bool, profundidad: int,
                  alpha: float = -math.inf, beta: float = math.inf, movimiento: str = None):
        if profundidad == 0 or jugador == objetivo:
            return Utiles.calcular_distancia(jugador, objetivo), movimiento

        if maximizar:
            max_eval = -math.inf
            mejor_movimiento = None
            for mov in self.movimientos_posibles(jugador):
                nueva_posicion = self.mover_evaluacion(jugador, mov)
                curr_max_eval, _ = self.__minimax(nueva_posicion, objetivo, False, profundidad - 1, alpha, beta, mov)
                if curr_max_eval > max_eval:
                    max_eval = curr_max_eval
                    mejor_movimiento = mov
                alpha = max(alpha, max_eval)
                if alpha >= beta:
                    break
            return max_eval, mejor_movimiento
        else:
            min_eval = math.inf
            mejor_movimiento = None
            for mov in self.movimientos_posibles(objetivo):
                nueva_posicion = self.mover_evaluacion(objetivo, mov)
                curr_min_eval, _ = self.__minimax(jugador, nueva_posicion, True, profundidad - 1, alpha, beta, mov)
                if curr_min_eval < min_eval:
                    min_eval = curr_min_eval
                    mejor_movimiento = mov
                beta = min(beta, min_eval)
                if alpha >= beta:
                    break
            return min_eval, mejor_movimiento

    def generar_movimiento(self, jugador: tuple, objetivo: tuple, maximizar=True) -> str:
        depth = 4
        if maximizar:
            _, movimiento = self.__minimax(jugador, objetivo, maximizar, depth)
        else:
            _, movimiento = self.__minimax(objetivo, jugador, maximizar, depth)
        return movimiento


class Tablero:
    def __init__(self):
        self.objetos: list[Entidad] = []

    def agregar_objetos(self, *objetos) -> None:
        self.objetos.extend(objetos)

    def generar_obstaculos(self) -> None:
        global obstaculos
        obstaculos = set(Utiles.generar_obstaculos(OBSTACULOS, self.objetos))

    @staticmethod
    def mostrar_mensaje(mensaje: str) -> None:
        canvas.fill(Color.WHITE)
        fuente = pygame.font.SysFont("Segoe UI", 90)
        render = fuente.render(mensaje, True, Color.BLACK)
        canvas.blit(render, (100, 100))
        pygame.display.flip()

    def dibujar(self):
        canvas.fill(Color.WHITE)
        celdas: list[tuple] = [(x, y) for x in range(FILAS) for y in range(COLUMNAS)]
        entidades = {objeto.get_posicion(): {"color": objeto.color, "es_visible": objeto.es_visible} for objeto in
                     self.objetos}

        for celda in celdas:
            rectangulo = pygame.Rect(celda[0] * CELL_SIZE, celda[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if celda in entidades and entidades[celda]["es_visible"]:
                pygame.draw.rect(canvas, entidades[celda]["color"], rect=rectangulo)
            elif celda in obstaculos:
                pygame.draw.rect(canvas, Color.BROWN, rect=rectangulo)
            else:
                pygame.draw.rect(canvas, Color.BLACK, rect=rectangulo, width=1)

        pygame.display.flip()


class Utiles:
    @staticmethod
    def calcular_distancia(jugador, objetivo):
        return abs(objetivo[0] - jugador[0]) + abs(objetivo[1] - jugador[1])

    @staticmethod
    def mapear_input() -> dict:
        return {
            pygame.K_LEFT: "IZQUIERDA",
            pygame.K_RIGHT: "DERECHA",
            pygame.K_DOWN: "ABAJO",
            pygame.K_UP: "ARRIBA"
        }

    @staticmethod
    def generar_obstaculos(cantidad: int, objetos: list = None) -> list:
        # Inicializar una coleccion inmutable
        lista_obstaculos = set()
        # Inicializar las posiciones de los objetos del tablero en un set
        objetos_posiciones = {objeto.get_posicion() for objeto in objetos} if objetos else set()

        # Mientras n obstaculos generados < cantidad
        while len(lista_obstaculos) < cantidad:
            posicion_generada = Utiles.rand_pos()

            # Si la posicion no fue generada y no es la posicion de un objeto
            if posicion_generada not in lista_obstaculos and posicion_generada not in objetos_posiciones:
                lista_obstaculos.add(posicion_generada)

        return list(lista_obstaculos)

    @staticmethod
    def rand_pos() -> tuple:
        return random.randint(0, FILAS - 1), random.randint(0, COLUMNAS - 1)

    @staticmethod
    def mapear_movimiento(movimiento: str) -> tuple:
        mapeo = {
            "ARRIBA": (0, -1),
            "ABAJO": (0, 1),
            "DERECHA": (1, 0),
            "IZQUIERDA": (-1, 0)
        }
        return mapeo.get(movimiento, (0, 0))

    @staticmethod
    def evaluar_movimiento(posicion: tuple, movimiento: str) -> bool:
        new_x, new_y = Utiles.mapear_movimiento(movimiento)
        nueva_posicion = (posicion[0] + new_x, posicion[1] + new_y)
        return nueva_posicion not in obstaculos and 0 <= nueva_posicion[0] < FILAS and 0 <= nueva_posicion[1] < COLUMNAS
