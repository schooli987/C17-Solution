import pygame
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
class Paddle(pygame.sprite.Sprite):
    """A class to model the paddle"""
    
    def __init__(self, window_width, window_height):
        """Initialize the paddle"""
        super().__init__()
        self.image = pygame.image.load("paddle.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = window_width // 2
        self.rect.bottom = window_height - 10

        self.velocity = 100

    def update(self, event):
        """Update the paddle based on events"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.rect.x -= self.velocity
            if event.key == pygame.K_RIGHT:
                self.rect.x += self.velocity
