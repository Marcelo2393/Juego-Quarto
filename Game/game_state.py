from .board import Board
from .piece import Piece
from .utils import generate_all_pieces

class GameState:
    def __init__(self):
        self.board = Board()
        self.available_pieces = generate_all_pieces()
        self.current_piece = None
        self.history = []

    def play_move(self, move):
        x, y, piece = move
        success = self.board.place_piece(x, y, piece)
        if success:
            self.available_pieces.remove(piece)
            self.current_piece = piece
            self.history.append(move)
        return success

    def get_possible_moves(self, piece):
        return [(x, y, piece) for (x, y) in self.board.available_positions()]

    def is_game_over(self):
        return self.board.check_winner() or self.board.is_full()

    def get_winner(self):
        return "Agente IA" if self.board.check_winner() else None
