import pygame

from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu: 
    half_screen_height = SCREEN_HEIGHT // 2
    half_screen_width = SCREEN_WIDTH // 2

    def __init__(self, message, screen):
        screen.fill((225, 225, 225))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_height, self.half_screen_width)
        self.death_count = 0 

    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw(self, screen, score=None):
        screen.blit(self.text, self.text_rect)
        if score is not None:
            self.draw_score(screen, score)
        self.draw_death_count(screen) 

    def reset_screen_color(self, screen):
        screen.fill((225, 225, 225))

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.plauing = False
            elif event.type == pygame.KEYDOWN:
                game.run()

    def update_message(self, message):
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width, self.half_screen_height)

    def draw_score(self, screen, score):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {score}', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (self.half_screen_width, self.half_screen_height + 50)
        screen.blit(text, text_rect)

    def increment_death_count(self):
        self.death_count += 1

    def draw_death_count(self, screen):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Deaths: {self.death_count}', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (self.half_screen_width, self.half_screen_height + 100)
        screen.blit(text, text_rect)
