import random
from .agent_base import AgentBase
import copy

class MinimaxAgent(AgentBase):
    def __init__(self, name="Minimax AI", depth=2):
        super().__init__(name)
        self.depth = depth

    def choose_move(self, state, current_piece):
        _, best_move = self.minimax(state, current_piece, self.depth, True)
        return best_move if best_move else random.choice(state.get_possible_moves(current_piece))

    def choose_piece(self, state):
        return random.choice(state.available_pieces)

    def minimax(self, state, piece, depth, maximizing):
        if depth == 0 or state.is_game_over():
            return self.evaluate(state), None

        best_score = float("-inf") if maximizing else float("inf")
        best_move = None

        for move in state.get_possible_moves(piece):
            new_state = copy.deepcopy(state)
            new_state.play_move(move)

            if new_state.is_game_over():
                score = self.evaluate(new_state)
            else:
                next_piece = random.choice(new_state.available_pieces)
                score, _ = self.minimax(new_state, next_piece, depth - 1, not maximizing)

            if maximizing and score > best_score:
                best_score, best_move = score, move
            elif not maximizing and score < best_score:
                best_score, best_move = score, move

        return best_score, best_move

    def evaluate(self, state):
        if state.board.check_winner():
            return 100
        return -len(state.board.available_positions())  # menos es mejor
