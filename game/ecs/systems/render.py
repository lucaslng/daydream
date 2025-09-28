import pygame as pg

from game.ecs.components.circle import Circle
from game.ecs.components.bullet import Bullet
from game.ecs.components.death import Death
from game.ecs.components.player import PlayerComponent
from game.ecs.entity import Entity
from game.ecs.components.physics import Position, Rotation
from game.ecs.components.person_sprite import PersonSprite
from game.resources.levels import LEVELS
from util.prepare import SURF
from game.sprites.sprite import Sprite


class RenderSystem():

  def __init__(self):
    death_animation_filename = "death_animation"
    self._death_sprites = (Sprite(death_animation_filename, "0"), Sprite(death_animation_filename, "1"), Sprite(
      death_animation_filename, "2"), Sprite(death_animation_filename, "3"), Sprite(death_animation_filename, "4"), Sprite(death_animation_filename, "5"))
    self._bullet_sprite = pg.transform.scale_by(Sprite("weapons", "bullet").get(), 0.35) # scale the bullet
    self._gun_sprites = {
      "ar": Sprite("weapons", "assault_rifle").get(),
      "lmg": Sprite("weapons", "lmg").get(),
      "revolver": Sprite("weapons", "revolver").get()
    }
    self._body_surface = Sprite("body", "base_chest").get()
    for part in ["head", "legs", "arms"]:
      self._body_surface.blit(Sprite("body", f"base_{part}").get(), (0,0))
    self._upgraded_sprites = {
      "head": Sprite("body", "upgraded_head").get(),
      "chest": Sprite("body", "upgraded_chest").get(),
      "arms_top": Sprite("body", "upgraded_arms_top").get(),
      "arms_bottom": Sprite("body", "upgraded_arms_bottom").get(),
      "legs_top": Sprite("body", "upgraded_legs_top").get(),
      "legs_bottom": Sprite("body", "upgraded_legs_bottom").get()
    }

    self._blood_sprite = Sprite("death_animation", "blood").get()
    self.blood_positions: set[Position] = set()

    self._maps = [pg.transform.scale_by(pg.image.load(f"game/resources/maps/map_{i}.png"), 4) for i in range(len(LEVELS))]
    # self._collision_mask = pg.transform.scale_by(pg.mask.from_surface(pg.image.load(
    #   "game/resources/collision_masks/collision_mask_0.png").convert_alpha()).to_surface(), 4)

  def update(self, entities: set[Entity], player: Entity, level: int, weapon_system=None):
    # draw player

    player_pos: Position = player.get_component(Position)  # type: ignore
    offset_x = SURF.get_rect().centerx - player_pos.x
    offset_y = SURF.get_rect().centery - player_pos.y

    SURF.blit(self._maps[level], (offset_x, offset_y))

    for entity in entities:
      if entity.has_component(Position):
        entity_pos: Position = entity.get_component(Position)  # type: ignore
        new_pos = (entity_pos.x + offset_x, entity_pos.y + offset_y)
        #gun tio plaer fx osffset latear change x falveu up
        if entity == player and entity.has_components(PersonSprite, Rotation):
          angle: float = entity.get_component(Rotation).angle  # type: ignore
          current_weapon_type = weapon_system.get_current_weapon().weapon_type if weapon_system else "ar"
          gun_sprite = self._gun_sprites[current_weapon_type]
          gun_rotated = pg.transform.rotate(gun_sprite, -angle)
          gun_offset_x = 25 * pg.math.Vector2(1, 0).rotate(angle).x + 12 * pg.math.Vector2(0, 1).rotate(angle).x
          gun_offset_y = 25 * pg.math.Vector2(1, 0).rotate(angle).y + 12 * pg.math.Vector2(0, 1).rotate(angle).y
          gun_pos = (new_pos[0] + gun_offset_x, new_pos[1] + gun_offset_y + 16)
          SURF.blit(gun_rotated, gun_rotated.get_rect(center=gun_pos))
        
        if entity.has_components(PersonSprite, Rotation):
          angle: float = entity.get_component(Rotation).angle
          person_sprite: PersonSprite = entity.get_component(
            PersonSprite)
          sprite_surface = person_sprite.body_sprite.get()
          rotated = pg.transform.rotate(
            sprite_surface, -angle)
          SURF.blit(rotated, rotated.get_rect(center=new_pos))
        
        if entity.has_component(Death) and entity.get_component(Death).death:
          frame = entity.get_component(Death).frame // 2
          if frame < 6:
            death_sprite = self._death_sprites[frame].get()
            SURF.blit(death_sprite, death_sprite.get_rect(center=new_pos))
        if entity.has_component(Bullet):
          if entity.has_component(Rotation):
            angle: float = entity.get_component(Rotation).angle
            rotated_bullet = pg.transform.rotate(self._bullet_sprite, -angle)
            SURF.blit(rotated_bullet, rotated_bullet.get_rect(center=new_pos))
          else:
            SURF.blit(self._bullet_sprite, self._bullet_sprite.get_rect(center=new_pos))
        if entity.has_component(Circle):
          circle: Circle = entity.get_component(Circle)  # type: ignore
          pg.draw.circle(SURF, circle.color, new_pos, circle.size)

    for blood_pos in self.blood_positions:
      SURF.blit(self._blood_sprite, self._blood_sprite.get_rect(center=(blood_pos.x + offset_x, blood_pos.y + offset_y)))
    
    body_dest = self._body_surface.get_rect(bottomleft=(SURF.get_rect().bottomleft))
    SURF.blit(self._body_surface, body_dest)
    player_component: PlayerComponent = player.get_component(PlayerComponent) # type: ignore
    for upgrade, obtained in player_component.upgrades.items():
      if obtained:
        SURF.blit(self._upgraded_sprites[upgrade], body_dest)

    # insanity bar
    bar = pg.Rect(0, 30, 800, 30)
    bar.centerx = SURF.get_rect().centerx
    progress = bar.copy()
    progress.width = bar.width * min(100, player_component.kills) // 100
    pg.draw.rect(SURF, (196,40,28), bar, border_radius=2)
    pg.draw.rect(SURF, (117,0,0), progress, border_radius=2)