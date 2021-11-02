'''
Autor:
    Nombre: Álvaro Carrera
    Mail: a.carrera@upm.es
    Github: alvarocarrera
Fecha (Versión): 19-10-2021 (0.1-dev)
Descripción:
    Módulo que incluye clases para el juego desarrollado durante el curso
    2021-2022 de la asignatura Programación (PROG) del Grado de Ingeniería
    y Sistemas de Datos (GISD) en el Universidad Politécnica de Madrid (UPM).
'''
import random
from enum import Enum

class TipoFicha(Enum):
    '''Diferentes tipos de fichas del juego'''
    JUGADOR = 1
    ESPIA = 2
    MURO = 3

class Ficha:
    '''
    Clase que representa una Ficha en el Tablero

    Atributos:
        pos: dict[str, int] contiene las coordenadas x,y de
            la ficha en el tablero
        tipo: str contiene el tipo de la ficha
    '''
    def __init__(self, tipo: TipoFicha, x:int, y:int):
        '''
        Parámetros:
            tipo: tipo de la ficha del juego
            x: coordenada x de la ficha
            y: coordenada y de la ficha
        '''
        self.pos: dict[str,int] = {
            "x": x,
            "y": y
        }
        self.tipo: TipoFicha = tipo

class Jugador(Ficha):
    '''Clase que representa a un jugador de mi juego
    
    Atributos:
        nombre: str con el nombre del jugador
    '''
    def __init__(self, nombre: str, x: int, y: int):
        super().__init__(TipoFicha.JUGADOR, x, y)
        self.nombre: str = nombre
        self.pide_secretos()

    def pide_secretos(self, num: int = 2):
        '''TODO: implementar en el futuro,
        para pedir un número de secretos
        igual a num al usuario'''
        pass

class Espia(Ficha):
    '''TODO: ¿me interesa?'''
    pass

class Muro(Ficha):
    '''TODO: ¿me interesa?'''
    pass

class Tablero:
    '''
    Clase que representa el tablero de juego del spy_game. El tablero es
    rectangular al estilo de un tablero de ajedrez y su tamaño es 
    configurable en el momento de la creación del objeto.

    Atributos:
        casillas: list[list[Ficha]] representación de las casillas del tablero
        ancho: int: ancho del tablero (número de columnas)
        alto: int: alto del tablero (número de filas)
    '''
    def __init__(self, ancho: int = 10, alto: int = 5):
        '''
        El constructor puede recibir el número de columnas (ancho) y 
        el número de filas (alto), ambos como parámetros opcionales
        
        Parámetros:
            ancho: número de columnas del tablero
            alto: número de filas del tablero
        '''
        if ancho < 1 or alto < 1:
            print("No puedo hacer un tablero con dimensiones menores que 1.")
            print("No se puede iniciar el juego")
            exit(1)
        
        self.casillas: list[list[Ficha]] = []
        self.ancho: int = ancho
        self.alto: int = alto
        for i in range(alto):
            self.casillas.append([])
            for j in range(ancho):
                self.casillas[i].append(None)

    def imprime(self, nombre: str = "TABLERO DE JUEGO") -> None:
        '''
        Imprime por consola una representación del tablero.
        
        Parámetros:
            nombre: mensaje que se imprime antes del tablero (opcional)
        '''
        print("\n"+nombre+"\n")

        print("-"*(self.ancho*2+1))
        for fila in self.casillas:
            msg = "|" # Barra inicial
            for ficha in fila: # ficha: Ficha
                if not ficha:
                    msg += " "
                else:
                    match ficha.tipo:
                        case TipoFicha.MURO:
                            msg += "*"
                        case TipoFicha.ESPIA:
                            msg += 'e'
                        case TipoFicha.JUGADOR:
                            msg += ficha.nombre.capitalize()[0]
                        case _:
                            msg += '?'
                msg += '|' # Barra después de cada casilla
            print(msg)
            print("-"*(self.ancho*2+1))
    
    def pon_ficha(self, ficha: Ficha) -> None:
        '''
        Pone una ficha en el tablero. Consulta la posición de la ficha
        a través de su atributo pos y la posiciona en el tablero, es
        decir, en la casilla correspondiente del atributo casillas.
        
        Parámetros:
            ficha: objeto de la clase Ficha para poner sobre el tablero
        '''
        x: int = ficha.pos["x"]
        y: int = ficha.pos["y"]
        self.casillas[y][x] = ficha

    def pon_obstaculos(self, prob: float = 0.15) -> None:
        '''
        Pone muros con una probabilidad (15% por defecto).

        Parámetros:
            prob: probabilidad de que se ponga una ficha tipo Muro en
                una casilla. La probabilidad debe ser un número 
                real menor que 1.
        '''
        for num_fila in range(self.alto):
            for num_columna in range(self.ancho):
                x: float = random.random()
                if x < prob:
                    ficha = Ficha(TipoFicha.MURO, num_columna, num_fila)
                    self.pon_ficha(ficha)

class Turno:
    '''TODO: ¿Cómo es un turno?'''
    pass

class Combate:
    '''TODO: ¿Cómo es un combate/encuentro
     entre espías y jugadores?
     
     ¿Hay espías que son aliados entre ellos?'''
    pass