class AgentBase:
    def __init__(self, name="Agente"):
        self.name = name

    def choose_move(self, state, current_piece):
        """Debe devolver (x, y, piece)"""
        raise NotImplementedError

    def choose_piece(self, state):
        """Debe devolver una pieza para entregar al oponente"""
        raise NotImplementedError
