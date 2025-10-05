import os
import time
from pynput import keyboard
import random

from snake import Snake


class io_handler:

    x_size: int
    y_size: int
    game_speed: float
    last_input: str
    matrix = []

    def __init__(self, dim, speed):
        self.x_size = dim[0]
        self.y_size = dim[1]
        self.game_speed = speed
        self.last_input = "w"

        for i in range(self.y_size):
            self.matrix.append([0] * self.x_size)

    def record_inputs(self):
        def on_press(key):
            try:
                if key.char in ["w", "a", "s", "d"]:
                    self.last_input = key.char
            except AttributeError:
                if key == keyboard.Key.esc:
                    self.last_input = "end"

        listener = keyboard.Listener(on_press=on_press)
        listener.daemon = True  # permite que o programa termine normalmente
        listener.start()

    def display(self):
        def display_h_line():
            print("+", end="")
            print("--" * len(self.matrix[0]), end="")
            print("+")

        def display_content_line(line):
            print("|", end="")
            for item in line:
                if item == 1:
                    print("🟩", end="")  # corpo
                elif item == 2:
                    print("🐍", end="")  # cabeça
                elif item == 3:
                    print("🍎", end="")  # fruta
                else:
                    print("  ", end="")
            print("|")

        os.system("cls" if os.name == "nt" else "clear")
        display_h_line()
        for line in self.matrix:
            display_content_line(line)
        display_h_line()


### exemplo do uso da classe io_handler
# Campo maior
instance = io_handler((30, 20), 0.12)


DIRECTION_MAP = {
    "w": "UP",
    "a": "LEFT",
    "s": "DOWN",
    "d": "RIGHT",
}


def _clear_matrix(io):
    for y in range(io.y_size):
        for x in range(io.x_size):
            io.matrix[y][x] = 0


def _draw_snake_and_fruits(io, snake, fruits):
    for fx, fy in fruits:
        if 0 <= fx < io.x_size and 0 <= fy < io.y_size:
            io.matrix[fy][fx] = 3
    for seg in snake.body[1:]:
        x, y = seg
        if 0 <= x < io.x_size and 0 <= y < io.y_size:
            io.matrix[y][x] = 1
    hx, hy = snake.head
    if 0 <= hx < io.x_size and 0 <= hy < io.y_size:
        io.matrix[hy][hx] = 2


def _random_empty(io, snake, occupied_extra=None):
    occupied = set(snake.body)
    if occupied_extra:
        occupied |= set(occupied_extra)
    candidates = [
        (x, y)
        for y in range(io.y_size)
        for x in range(io.x_size)
        if (x, y) not in occupied
    ]
    if not candidates:
        return (0, 0)
    return random.choice(candidates)


def _ensure_fruits(io, snake, fruits):
    alvo = snake.num_frutas_ativas()
    while len(fruits) > alvo:
        fruits.pop()
    while len(fruits) < alvo:
        pos = _random_empty(io, snake, fruits)
        if pos not in fruits:
            fruits.append(pos)


def game_loop():
    snake = Snake(
        start=(1, 1), direction="RIGHT", bounds=(instance.x_size, instance.y_size)
    )

    fruits = []
    _ensure_fruits(instance, snake, fruits)

    instance.record_inputs()
    while True:
        last = instance.last_input
        if last in DIRECTION_MAP:
            snake.turn(DIRECTION_MAP[last])

        snake.move()

        if snake.collides_with_self():
            _clear_matrix(instance)
            instance.display()
            print("Game Over!")
            break

        consumed = False
        if snake.head in fruits:
            fruits = [f for f in fruits if f != snake.head]
            snake.grow()
            consumed = True
        _ensure_fruits(instance, snake, fruits)

        _clear_matrix(instance)
        _draw_snake_and_fruits(instance, snake, fruits)

        instance.display()
        print(
            "Mova com WASD, ESC para sair | Frutas:",
            len(fruits),
            "| Tamanho:",
            len(snake.body),
        )

        if instance.last_input == "end":
            print("Saindo do jogo...")
            break

        time.sleep(instance.game_speed)


if __name__ == "__main__" and not os.environ.get("SNAKE_TESTING"):
    game_loop()
