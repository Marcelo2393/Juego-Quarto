import random
from .agent_base import AgentBase

class RuleBasedAgent(AgentBase):
    def choose_move(self, state, current_piece):
        # Escoge un movimiento al azar
        possible_moves = state.get_possible_moves(current_piece)
        return random.choice(possible_moves)

    def choose_piece(self, state):
        return random.choice(state.available_pieces)
