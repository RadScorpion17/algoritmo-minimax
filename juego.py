from utiles import Jugador, IA, Tablero, pygame, Utiles, Color
from utiles import FILAS, COLUMNAS


def main():
    # Generar posiciones aleatorias para el gato y el raton
    posicion_uno: tuple = Utiles.rand_pos()
    posicion_dos: tuple = Utiles.rand_pos()
    while posicion_uno == posicion_dos:
        posicion_dos: tuple = Utiles.rand_pos()

    # Inicializar entidades
    madriguera = Jugador((FILAS - 1, COLUMNAS - 1), Color.BLUE)
    queso = Jugador((0, 0), Color.YELLOW)
    raton = Jugador(posicion_uno, Color.GREEN)
    gato_ia = IA(posicion_dos, Color.RED)

    # Inicializar tablero, agregar entidades y generar obstáculos
    tablero = Tablero()
    tablero.agregar_objetos(raton, gato_ia, madriguera, queso)
    tablero.generar_obstaculos()
    tablero.dibujar()

    jugando = True
    turno = "raton"
    turnos = 1

    while jugando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jugando = False
                break

            if turnos >= 30:
                tablero.mostrar_mensaje("No hay turnos!")
                pygame.time.wait(5000)
                jugando = False
                break

            if turno == "raton" and event.type == pygame.KEYDOWN:
                movimiento = Utiles.mapear_input().get(event.key)
                if movimiento and Utiles.evaluar_movimiento(raton.get_posicion(), movimiento):
                    raton.mover(movimiento)
                    turno = "gato_ia"
                    turnos += 1

        if turno == "gato_ia" and jugando:
            movimiento = gato_ia.generar_movimiento(gato_ia.get_posicion(), raton.get_posicion(), False)
            if movimiento:
                gato_ia.mover(movimiento)
                turno = "raton"

        if raton.get_posicion() == queso.get_posicion() and queso.es_visible:
            queso.es_visible = False

        if raton.get_posicion() == madriguera.get_posicion() and not queso.es_visible:
            tablero.mostrar_mensaje("¡Ganaste!")
            pygame.time.wait(5000)
            jugando = False

        if gato_ia.get_posicion() == raton.get_posicion():
            tablero.mostrar_mensaje("¡Perdiste!")
            pygame.time.wait(5000)
            jugando = False

        tablero.dibujar()


if __name__ == '__main__':
    main()
