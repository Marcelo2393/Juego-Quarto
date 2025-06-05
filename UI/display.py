def print_board(board):
    print("\nTablero actual:")
    for i in range(4):
        fila = []
        for j in range(4):
            piece = board.grid[i][j]
            fila.append(str(piece) if piece else "--")
        print(" ".join(fila))
    print()