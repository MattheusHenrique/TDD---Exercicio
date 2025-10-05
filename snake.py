class Snake:
    """Esqueleto inicial para TDD. Implementar a lógica para passar nos testes."""

    def __init__(self, start, direction):
        self.head = None
        self.direction = direction
        self.body = []

    def move(self):
        pass

    def grow(self):
        pass

    def turn(self, new_direction):
        pass

    def collides_with_self(self):
        return False
