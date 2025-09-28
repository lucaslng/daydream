from game.ecs.components.player import PlayerComponent
from game.ecs.components.speed import Speed
from game.ecs.entity import Entity


class UpgradeSystem():
	def update(self, player: Entity):
		player_component: PlayerComponent = player.get_component(PlayerComponent) # type: ignore
		player_component.upgrades["arms_top"] = player_component.kills > 6
		player_component.upgrades["legs_bottom"] = player_component.kills > 13
		player_component.upgrades["arms_bottom"] = player_component.kills > 19
		player_component.upgrades["legs_top"] = player_component.kills > 26
		player_component.upgrades["chest"] = player_component.kills > 32
		player_component.upgrades["head"] = player_component.kills > 39
		
		if player_component.upgrades["legs_bottom"]:
			speed: Speed = player.get_component(Speed) # type: ignore
			speed.speed = 700
			if player_component.upgrades["legs_top"]:
				speed.speed = 900