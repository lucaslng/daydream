from game.ecs.component import Component


class PlayerComponent(Component):
  def __init__(self):
    self.kills = 0
    self.upgrades = {k: False for k in [
        "head",
        "chest",
        "arms_top",
        "arms_bottom",
        "legs_top",
        "legs_bottom"]}
