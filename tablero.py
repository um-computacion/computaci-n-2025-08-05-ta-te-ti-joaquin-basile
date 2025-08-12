class PosOcupadaException(Exception):
    ...


class Tablero:
    def __init__(self):
        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]

    def poner_la_ficha(self, fil, col, ficha):
        if self.contenedor[fil][col] == "":
            self.contenedor[fil][col] = ficha
        else:
            raise PosOcupadaException("pos ocupada!")

    def ganador(self, ficha):
        #Comprobar horizontal
        for fila in self.contenedor:
            if all(col == ficha for col in fila):
                return True
        #Comprobar vertical
        for col in range(3):
            if all(self.contenedor[f][col] == ficha for f in range(3)):
                return True

        # Diagonales
        if all(self.contenedor[i][i] == ficha for i in range(3)):
            return True
        if all(self.contenedor[i][2 - i] == ficha for i in range(3)):
            return True
        return False
    
    def empate(self):
        return all(c != "" for fila in self.contenedor for c in fila)
