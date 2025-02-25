import pygame
from paddle import Paddle
from ball import Ball
from bricks import Bricks

# Initialize pygame
pygame.init()

# Set display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface= pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Paddle and Ball")

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)  # Default font, size 36
# Colors
BLACK = (0, 0, 0)
WHITE=(255,255,255)
# Create sprite groups
paddle_group = pygame.sprite.Group()
ball_group = pygame.sprite.Group()
bricks_group=pygame.sprite.Group()

# Create paddle and ball objects
paddle = Paddle(WINDOW_WIDTH, WINDOW_HEIGHT)
ball = Ball(WINDOW_WIDTH, WINDOW_HEIGHT)


# Add objects to their respective groups
paddle_group.add(paddle)
ball_group.add(ball)

num_rows = 7
num_cols = 7
start_x = 80
start_y = 60
spacing_x = 100  # horizontal spacing between bacteria
spacing_y = 30   # vertical spacing between rows

for row in range(num_rows):
    for col in range(num_cols):
        x = start_x + col * spacing_x
        y = start_y + row * spacing_y
        # Provide velocity (e.g., 2) and bullet_group (nanobot_laser_group)
        brick = Bricks(x, y)
        bricks_group.add(brick)


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Pass the event to the paddle's update method
        paddle.update(event)

    # Update
    ball_group.update()


    # Draw everything
    display_surface.fill(BLACK)
    paddle_group.draw(display_surface)
    ball_group.draw(display_surface)
    bricks_group.update()

    bricks_group.draw(display_surface)
    # Update the display
   
    score_text = font.render(f"Score: {ball.score}", True, WHITE)
    score_rect = score_text.get_rect(centerx=WINDOW_WIDTH // 2, top=20)
    
    lives_text = font.render(f"Lives: {ball.lives}", True, WHITE)
    lives_rect = lives_text.get_rect(topright=(WINDOW_WIDTH - 20, 20))
    
    # Draw on screen
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)
    pygame.draw.line(display_surface, WHITE, (0, 50), (WINDOW_WIDTH, 50), 4)
    pygame.draw.line(display_surface, WHITE, (0, WINDOW_HEIGHT - 100), (WINDOW_WIDTH, WINDOW_HEIGHT - 100), 4)
    if pygame.sprite.spritecollide(ball,bricks_group, True):
        ball.speed_y*=-1
        ball.score+=10

     
    if ball.rect.colliderect(paddle.rect):
        ball.speed_y*=-1

        
    if ball.rect.bottom <= 0:
            ball.lives-=1

    pygame.display.update()

    # Cap the frame rate
    clock.tick(FPS)

# End the game
pygame.quit()