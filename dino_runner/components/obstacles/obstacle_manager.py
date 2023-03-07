import pygame

from dino_runner.components.obstacles.cactus import SmallCactus, LargeCactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS


class ObctacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            cactus = SmallCactus(SMALL_CACTUS)
            self.obstacles.append(cactus)
        elif len(self.obstacles) == 0:
            cactus = LargeCactus(LARGE_CACTUS)
            self.obstacles.append(cactus)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

        if game.player.dino_rect.colliderect(obstacle.rect):
            print("Collision")

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)