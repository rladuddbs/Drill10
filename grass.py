from pico2d import load_image


class Grass:
    def __init__(self, h):
        self.image = load_image('grass.png')
        self.high = h
    def draw(self):
        self.image.draw(400, self.high)

    def update(self):
        pass
