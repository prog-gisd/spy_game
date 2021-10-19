'''
Fichero: game.py
Módulo: game
Autor:
    Nombre: Álvaro Carrera
    Mail: a.carrera@upm.es
    Github: alvarocarrera
    En el resto del móludo, este autor será considerado como:
        a.carrera
Fecha (Versión): 19-10-2021 (0.1-dev)
Descripción:
    Módulo que incluye clases para el juego desarrollado durante el curso
    2021-2022 de la asignatura Programación (PROG) del Grado de Ingeniería
    y Sistemas de Datos (GISD) en el Universidad Politécnica de Madrid (UPM).
'''


class Ficha:
    '''
    Clase: Ficha
    Autor: a.carrera
    Fecha (Versión): 19-10-2021 (0.1)
    Descripción:
        Clase que representa una Ficha en el Tablero

    Atributos:
        pos: dict[str, int] contiene las coordenadas x,y de
            la ficha en el tablero
        tipo: str contiene el tipo de la ficha
    
    Métodos:
        __init__: constructor
    '''
    def __init__(self, tipo: str, x:int, y:int):
        '''
        Función: __init__ -  Constructor de Ficha
        Autor: a.carrera
        Fecha (Versión): 19-10-2021 (0.1)
        Descripción:
            El constructor recibe tanto el tipo como las coordenadas
            como números enteros
        Parámetros:
            tipo: str: tipo de la ficha del juego
            x: int: coordenada x de la ficha
            y: int: coordenada y de la ficha
        '''
        self.pos: dict[str,int] = {
            "x": x,
            "y": y
        }
        self.tipo: str = tipo

class Tablero:
    '''
    Clase: Tablero
    Autor: a.carrera
    Fecha (Versión): 19-10-2021 (0.1)
    Descripción:
        Clase que representa el tablero de juego del spy_game. El tablero es
        rectangular al estilo de un tablero de ajedrez y su tamaño es 
        configurable en el momento de la creación del objeto.

    Atributos:
        casillas: list[list[Ficha]] representación de las casillas del tablero
        ancho: int: ancho del tablero (número de columnas)
        alto: int: alto del tablero (número de filas)
    
    Métodos:
        __init__: constructor
        imprime: método que imprime una representación del tablero por consola
        pon_ficha: método que una ficha en la posición proporcionada
    '''
    def __init__(self, ancho: int = 10, alto: int = 5):
        '''
        Función: __init__ -  Constructor de Tablero
        Autor: a.carrera
        Fecha (Versión): 19-10-2021 (0.1)
        Descrpición:
            El constructor puede recibir el número de columnas (ancho) y 
            el número de filas (alto), ambos como parámetros opcionales
        Parámetros:
            ancho: int: número de columnas del tablero
            alto: int: número de filas del tablero
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
        Función: imprime
        Autor: a.carrera
        Fecha (Versión): 19-10-2021 (0.1)
        Descrpición:
            Imprime por consola una representación del tablero.
        Parámetros:
            nombre: str: mensaje que se imprime antes del tablero (opcional)
        '''
        print("\n"+nombre+"\n")

        print("-"*(self.ancho*2+1))
        for fila in self.casillas:
            msg = "|"
            for casilla in fila:
                if casilla is None:
                    msg += " |"
                elif isinstance(casilla, Ficha):
                    msg += casilla.tipo.capitalize()[0]+"|"
            print(msg)
            print("-"*(self.ancho*2+1))
    
    def pon_ficha(self, ficha: Ficha) -> None:
        '''
        Función: pon_ficha
        Autor: a.carrera
        Fecha (Versión): 19-10-2021 (0.1)
        Descrpición:
            Pone una ficha en el tablero. Consulta la posición de la ficha
            a través de su atributo pos y la posiciona en el tablero, es
            decir, en la casilla correspondiente del atributo casillas.
        Parámetros:
            ficha: Ficha: objeto de la clase Ficha para poner sobre el tablero
        '''
        x: int = ficha.pos["x"]
        y: int = ficha.pos["y"]
        self.casillas[y][x] = ficha


'''
Inicio del programa
'''
# Se crea un tablero
mi_tablero: Tablero = Tablero(alto=6, ancho=12)


# Se crean algunas fichas
ficha1: Ficha = Ficha("Muro", x=6, y=2)
ficha2: Ficha = Ficha("Espía", x=9, y=4)
# y se ponen en el tablero
mi_tablero.pon_ficha(ficha=ficha1)
mi_tablero.pon_ficha(ficha=ficha2)

# Se imprime el estado del tablero
mi_tablero.imprime()