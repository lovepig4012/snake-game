class Food:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.position = self.spawn_food()

    def spawn_food(self):
        import random
        x = random.randint(0, (self.width // 10) - 1) * 10
        y = random.randint(0, (self.height // 10) - 1) * 10
        return (x, y)

    def get_position(self):
        return self.position

    def respawn(self):
        self.position = self.spawn_food()