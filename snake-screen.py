import os
import time
from pynput import keyboard


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
instance = io_handler((10, 15), 0.5)
instance.matrix[0][0] = 1  # corpo
instance.matrix[0][1] = 2  # cabeça
instance.matrix[0][2] = 3  # fruta


def game_loop():
    instance.record_inputs()
    while True:
        instance.display()
        print("Mova com WASD, saia com ESC. Último botão:", instance.last_input)

        if instance.last_input == "end":
            print("Saindo do jogo...")
            break

        # aqui você pode adicionar a lógica do jogo
        time.sleep(instance.game_speed)


game_loop()
