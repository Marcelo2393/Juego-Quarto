from .piece import Piece

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(4)] for _ in range(4)]

    def place_piece(self, x, y, piece):
        if self.grid[x][y] is None:
            self.grid[x][y] = piece
            return True
        return False

    def get_piece(self, x, y):
        return self.grid[x][y]

    def available_positions(self):
        return [(i, j) for i in range(4) for j in range(4) if self.grid[i][j] is None]

    def is_full(self):
        return all(self.grid[i][j] is not None for i in range(4) for j in range(4))

    def check_winner(self):
        lines = []

        for i in range(4):
            lines.append([self.grid[i][j] for j in range(4)])  # filas
            lines.append([self.grid[j][i] for j in range(4)])  # columnas

        lines.append([self.grid[i][i] for i in range(4)])      # diagonal principal
        lines.append([self.grid[i][3 - i] for i in range(4)])  # diagonal secundaria

        for line in lines:
            if None in line:
                continue
            for i in range(4):  # 4 atributos
                if all(p.attributes[i] == line[0].attributes[i] for p in line):
                    return True
        return False

    def print_board(self):
        """Imprime el tablero en formato 4x4 con separaciones visuales."""
        for i in range(4):
            row = []
            for j in range(4):
                piece = self.grid[i][j]
                if piece:
                    row.append(str(piece))
                else:
                    row.append("    ")  # espacio vacío
            print(" │ ".join(row))
            if i < 3:
                print("────┼────┼────┼────")