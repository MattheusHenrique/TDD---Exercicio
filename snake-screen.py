import os
import time
from pynput import keyboard

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
                    print("[]", end="")
                elif item == 2:
                    print("<>", end="")
                elif item == 3:
                    print("()", end="")
                else:
                    print("  ", end="")
            print("|")

        os.system("cls" if os.name == "nt" else "clear")
        display_h_line()
        for line in self.matrix:
            display_content_line(line)
        display_h_line()


### exemplo do uso da classe io_handler
instance = io_handler((10, 15), 0.2)


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


def _draw_snake_and_fruit(io, snake, fruit_pos):
    fx, fy = fruit_pos
    if 0 <= fx < io.x_size and 0 <= fy < io.y_size:
        io.matrix[fy][fx] = 3
    for seg in snake.body[1:]:
        x, y = seg
        if 0 <= x < io.x_size and 0 <= y < io.y_size:
            io.matrix[y][x] = 1
    hx, hy = snake.head
    if 0 <= hx < io.x_size and 0 <= hy < io.y_size:
        io.matrix[hy][hx] = 2


def _find_first_empty(io):
    for y in range(io.y_size):
        for x in range(io.x_size):
            if io.matrix[y][x] == 0:
                return (x, y)
    return (0, 0)


def game_loop():
    snake = Snake(
        start=(1, 1), direction="RIGHT", bounds=(instance.x_size, instance.y_size)
    )
    fruit_pos = (3, 0)

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

        if snake.head == fruit_pos:
            snake.grow()
            _clear_matrix(instance)
            _draw_snake_and_fruit(instance, snake, fruit_pos)
            fruit_pos = _find_first_empty(instance)

        _clear_matrix(instance)
        _draw_snake_and_fruit(instance, snake, fruit_pos)

        instance.display()
        print("Mova com WASD, saia com ESC. Último botão:", instance.last_input)

        if instance.last_input == "end":
            print("Saindo do jogo...")
            break

        time.sleep(instance.game_speed)


if __name__ == "__main__" and not os.environ.get("SNAKE_TESTING"):
    game_loop()
