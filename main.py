import pygame
from fighter import Fighter

pygame.init()

# Creat game window
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PyPunchKick")

# set framerate
clock = pygame.time.Clock()
FPS = 60

# Load Background Assets
bg_image = pygame.image.load("assets/images/background/background.jpg").convert_alpha()

# Draw Background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

# Create fighters
fighter_1 = Fighter(200, SCREEN_HEIGHT - 280)
fighter_2 = Fighter(1720, SCREEN_HEIGHT - 280)

# set game loop
run = True
while run:
    clock.tick(FPS)

    # Draw BG
    draw_bg()

    fighter_1.move(screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT)
    fighter_2.move(screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT)

    # draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # Update Display
    pygame.display.update()
    

# Exit PyGame
pygame.quit()