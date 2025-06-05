class Piece:
    def __init__(self, attributes):
        """
        Una pieza tiene 4 atributos binarios: [alto/bajo, claro/oscuro, sólido/hueco, cuadrado/redondo]
        """
        self.attributes = tuple(attributes)
        self.id = self.get_id()

    def get_id(self):
        return int(''.join(map(str, self.attributes)), 2)

    def __repr__(self):
 
        unicode_repr = [
            ["▼", "▲"],     # Bajo / Alto
            ["⚪", "⚫"],     # Claro / Oscuro
            ["■","⭗"],     # Sólido / Hueco
            ["◼", "🔵"]      # Cuadrado / Redondo
        ]
        symbols = [unicode_repr[i][val] for i, val in enumerate(self.attributes)]
        return ''.join(symbols)

    def __eq__(self, other):
        return isinstance(other, Piece) and self.attributes == other.attributes

    def __hash__(self):
        return hash(self.attributes)