import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING


class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_SPEED = 8.5

    def __init__(self):      
        self.duck_image = DUCKING
        self.run_image = RUNNING
        self.jump_image = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_speed = self.JUMP_SPEED
        self.image = self.run_image[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
    
    def update(self, user_input):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True            
            self.dino_jump = False
            self.dino_run = False
        elif not (self.dino_jump):
            self.dino_run = True  
            self.dino_jump = False
            self.dino_duck = False

    def run(self):
        self.image = self.run_image[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS     
        self.step_index += 1

    def duck(self):
        self.image = self.duck_image[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK    
        self.step_index += 1

    def jump(self):
        self.image = self.jump_image
        if self.dino_jump:
            self.dino_rect.y -= self.jump_speed * 4  
            self.jump_speed -= 0.8 
        if self.jump_speed < - self.JUMP_SPEED:
            self.dino_jump = False
            self.jump_speed = self.JUMP_SPEED
        
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
