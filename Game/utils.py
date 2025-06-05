from .piece import Piece

def generate_all_pieces():
    piezas = []
    for i in range(16):
        attributes = [int(b) for b in format(i, "04b")]
        piezas.append(Piece(attributes))
    return piezas.copy()