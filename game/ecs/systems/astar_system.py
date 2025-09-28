import heapq
from math import degrees, atan2

from game.ecs.components.speed import Speed
from game.ecs.entity import Entity
from game.ecs.components.enemy import AStarComponent
from game.ecs.components.physics import Position, Rotation, Velocity


def astar(grid: list[list[bool]], start: tuple[int, int], goal: tuple[int, int]):
  """
  grid: 2D list (0 = wall, 1 = walkable)
  start: (x, y) in grid coords
  goal: (x, y) in grid coords
  """
  # print(start, goal)
  rows, cols = len(grid), len(grid[0])
  open_set = []
  heapq.heappush(open_set, (0, start))
  came_from = {}
  g_score = {start: 0}

  def h(p1, p2):
    return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))

  while open_set:
    _, current = heapq.heappop(open_set)

    if current == goal:
      # Reconstruct path
      path = []
      while current in came_from:
        path.append(current)
        current = came_from[current]
      path.reverse()
      return path

    cx, cy = current
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1),
                   (1, 1), (1, -1), (-1, 1), (-1, -1)]:
      nx, ny = cx + dx, cy + dy
      neighbor = (nx, ny)
      if 0 <= nx < cols and 0 <= ny < rows:
        if grid[ny][nx] == 0:  # wall
          continue
        tentative_g = g_score[current] + 1
        if tentative_g < g_score.get(neighbor, float("inf")):
          came_from[neighbor] = current
          g_score[neighbor] = tentative_g
          f_score = tentative_g + h(neighbor, goal)
          heapq.heappush(open_set, (f_score, neighbor))

  return []  # no path


def lerp_angle(a, b, t):
  diff = (b - a + 180) % 360 - 180
  return a + diff * t


class AStarSystem():

  REPATH_TIME = 0.2
  TILE_SIZE = 4

  def __init__(self):
    self._repath_timer = 0.0

  def update(self, entities: set[Entity], player: Entity, grid: list[list[bool]], dt: float):
    repath = False
    self._repath_timer += dt
    if (self._repath_timer > AStarSystem.REPATH_TIME):
      self._repath_timer = 0.0
      repath = True
    player_pos: Position = player.get_component(Position)  # type: ignore
    for entity in entities:
      if entity.has_components(AStarComponent, Position, Velocity, Speed, Rotation):
        enemy_pos: Position = entity.get_component(Position)  # type: ignore
        vel: Velocity = entity.get_component(Velocity)  # type: ignore
        ai: AStarComponent = entity.get_component(
          AStarComponent)  # type: ignore
        speed: int = entity.get_component(Speed).speed  # type: ignore
        if repath:
          ai.path = astar(grid, (int(enemy_pos.x // AStarSystem.TILE_SIZE), int(enemy_pos.y // AStarSystem.TILE_SIZE)),
                          (int(player_pos.x // AStarSystem.TILE_SIZE), int(player_pos.y // AStarSystem.TILE_SIZE)))
          ai.target_index = 0
        if ai.path and ai.target_index < len(ai.path):
          tx, ty = ai.path[ai.target_index]
          target_x = tx * AStarSystem.TILE_SIZE + AStarSystem.TILE_SIZE // 2
          target_y = ty * AStarSystem.TILE_SIZE + AStarSystem.TILE_SIZE // 2
          dx = target_x - enemy_pos.x
          dy = target_y - enemy_pos.y
          rotation: Rotation = entity.get_component(Rotation)  # type: ignore
          rotation.angle = lerp_angle(
            rotation.angle, degrees(atan2(dy, dx)) + 90, dt * 5)
          dist = (dx**2 + dy**2) ** 0.5
          if dist > 2:  # move toward target tile
            # print("moving", target_x, target_y, ai.target_index, len(ai.path))
            vel.vx = (dx / dist) * speed
            vel.vy = (dy / dist) * speed
          else:
            vel.vx = vel.vy = 0
            ai.target_index += 1
