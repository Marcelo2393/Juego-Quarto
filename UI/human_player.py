from Game.piece import Piece

class HumanPlayer:
    def __init__(self, name="Humano"):
        self.name = name

    def choose_move(self, state, current_piece):
        print(f"Te ha tocado la pieza: {current_piece}")
        while True:
            try:
                x = int(input("Fila (0-3): "))
                y = int(input("Columna (0-3): "))
                if (x, y) in state.board.available_positions():
                    return (x, y, current_piece)
                else:
                    print("Posición ocupada o inválida. Intenta de nuevo.")
            except Exception:
                print("Entrada no válida. Intenta de nuevo.")

    def choose_piece(self, state):
        print("\nElige la pieza que entregas al agente:")
        piezas = state.available_pieces
        for idx, pieza in enumerate(piezas):
            print(f"{idx}: {pieza}")
        while True:
            try:
                idx = int(input("Número de pieza: "))
                if 0 <= idx < len(piezas):
                    return piezas[idx]
                else:
                    print("Índice fuera de rango.")
            except Exception:
                print("Entrada no válida.")
