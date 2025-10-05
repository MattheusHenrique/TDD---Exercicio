import random


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
        self._collision_blocks = []

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

        self._generate_collision_blocks()

    def grow(self):
        self._pending_growth += 1

    def turn(self, new_direction):
        if not new_direction:
            return
        if self._OPPOSITE.get(self.direction) == new_direction:
            return
        self.direction = new_direction

    def collides_with_self(self):
        if self.head in self.body[1:]:
            return True
        if self.head in self._collision_blocks:
            return True
        return False

    def num_frutas_ativas(self) -> int:
        tamanho = len(self.body)
        crescimentos = max(0, tamanho - 1)
        return 1 + (crescimentos // 10)

    def blocos_colisao(self):
        return self._collision_blocks.copy()

    def _generate_collision_blocks(self):
        tamanho = len(self.body)
        if tamanho < 21:
            return

        if self.bounds is None:
            return

        width, height = self.bounds
        if width <= 0 or height <= 0:
            return

        crescimentos_apos_20 = tamanho - 21
        blocos_esperados = (crescimentos_apos_20 // 5) + 1
        
        if len(self._collision_blocks) >= blocos_esperados:
            return

        blocos_a_adicionar = blocos_esperados - len(self._collision_blocks)
        occupied = set(self.body) | set(self._collision_blocks)

        for _ in range(blocos_a_adicionar):
            attempts = 0
            while attempts < 100: 
                x = random.randint(0, width - 1)
                y = random.randint(0, height - 1)
                pos = (x, y)

                if pos not in occupied:
                    self._collision_blocks.append(pos)
                    occupied.add(pos)
                    break
                attempts += 1
