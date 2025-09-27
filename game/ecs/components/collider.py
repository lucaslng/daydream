from game.ecs.Component import Component


class Collider(Component):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height