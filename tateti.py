from tablero import Tablero

class Tateti:
    def __init__(self):
        self.turno = "X"
        self.tablero = Tablero()
        self.juego_terminado = False

    def ocupar_una_de_las_casillas(self, fil, col):
        if self.juego_terminado:
            raise Exception("El juego ya terminó")

        self.tablero.poner_la_ficha(fil, col, self.turno)

        if self.tablero.ganador(self.turno):
            print(f"¡Ganó {self.turno}!")
            self.juego_terminado = True
            return

        if self.tablero.empate():
            print("¡Empate!")
            self.juego_terminado = True
            return


        #Cambiar jugador 
        self.turno = "0" if self.turno == "X" else "X"
