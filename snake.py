class Snake:
    """Implementação inicial da Snake para atender aos testes."""

    _OPPOSITE = {
        "UP": "DOWN",
        "DOWN": "UP",
        "LEFT": "RIGHT",
        "RIGHT": "LEFT",
    }

    def __init__(self, start, direction, bounds=None):
        self.head = start
        self.direction = direction
        self.body = [start]
        self._pending_growth = 0
        self.bounds = bounds

    def _direction_delta(self, direction):
        if direction == "RIGHT":
            return (1, 0)
        if direction == "LEFT":
            return (-1, 0)
        if direction == "DOWN":
            return (0, 1)
        if direction == "UP":
            return (0, -1)
        raise ValueError(f"Direção inválida: {direction}")

    def move(self):
        dx, dy = self._direction_delta(self.direction)
        next_x = self.head[0] + dx
        next_y = self.head[1] + dy

        if self.bounds is not None:
            width, height = self.bounds
            if width > 0:
                next_x = next_x % width
            if height > 0:
                next_y = next_y % height

        next_head = (next_x, next_y)

        self.body.insert(0, next_head)
        self.head = next_head

        if self._pending_growth > 0:
            self._pending_growth -= 1
        else:
            if len(self.body) > 1:
                self.body.pop()

    def grow(self):
        self._pending_growth += 1

    def turn(self, new_direction):
        if not new_direction:
            return
        if self._OPPOSITE.get(self.direction) == new_direction:
            return
        self.direction = new_direction

    def collides_with_self(self):
        return self.head in self.body[1:]
