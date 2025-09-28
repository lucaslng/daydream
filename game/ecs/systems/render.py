import pygame as pg

from game.ecs.components.circle import Circle
from game.ecs.components.bullet import Bullet
from game.ecs.components.death import Death
from game.ecs.entity import Entity
from game.ecs.components.physics import Position, Rotation
from game.ecs.components.person_sprite import PersonSprite
from game.sprites.sprite import Sprite
from util.prepare import SURF


class RenderSystem():

  def __init__(self):
    death_animation_filename = "death_animation"
    self._death_sprites = (Sprite(death_animation_filename, "0"), Sprite(death_animation_filename, "1"), Sprite(
      death_animation_filename, "2"), Sprite(death_animation_filename, "3"), Sprite(death_animation_filename, "4"), Sprite(death_animation_filename, "5"))

  def update(self, entities: set[Entity], player: Entity, map: pg.Surface):
    # draw player

    player_pos: Position = player.get_component(Position)  # type: ignore
    offset_x = SURF.get_rect().centerx - player_pos.x
    offset_y = SURF.get_rect().centery - player_pos.y

    for entity in entities:
      if entity.has_component(Position):
        entity_pos: Position = entity.get_component(Position)  # type: ignore
        new_pos = (entity_pos.x + offset_x, entity_pos.y + offset_y)
        if entity.has_components(PersonSprite, Rotation):
          angle: float = entity.get_component(Rotation).angle  # type: ignore
          person_sprite: PersonSprite = entity.get_component(
            PersonSprite)  # type: ignore
					sprite_surface = person_sprite.body_sprite.get()
					
					#bullet scaled down might change lata
					if entity.has_component(Bullet):
						sprite_surface = pg.transform.scale(sprite_surface, 
							(int(sprite_surface.get_width() * 0.75), int(sprite_surface.get_height() * 0.75)))
					
          rotated = pg.transform.rotate(
            sprite_surface, -angle)  # type: ignore
          SURF.blit(rotated, rotated.get_rect(center=new_pos))
          if entity.has_component(Death) and entity.get_component(Death).death:
            frame = entity.get_component(Death).frame // 2
            death_sprite = self._death_sprites[frame].get()
            SURF.blit(death_sprite, death_sprite.get_rect(center=new_pos))
        if entity.has_component(Circle):
          circle: Circle = entity.get_component(Circle)  # type: ignore
          pg.draw.circle(SURF, circle.color, new_pos, circle.size)
