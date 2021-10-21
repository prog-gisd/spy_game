'''
Lanzador del juego spy_game
'''
from game import Tablero, Ficha

'''
Inicio del programa
'''
# Se crea un tablero
mi_tablero: Tablero = Tablero(alto=6, ancho=12)

mi_tablero.pon_obstaculos()

# Se crean algunas fichas
ficha2: Ficha = Ficha("Espía", x=9, y=4)
# y se ponen en el tablero
mi_tablero.pon_ficha(ficha=ficha2)

# Se imprime el estado del tablero
mi_tablero.imprime()