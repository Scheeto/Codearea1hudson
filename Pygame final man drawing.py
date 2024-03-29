# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE

    #Draw head circle
    pygame.draw.circle(screen,"orange",(640,180),50)

    #Draw main body
    pygame.draw.polygon(screen,"orange", [(590, 230), (690,230), (690,380),(590,380)])

    #Draw left arm
    pygame.draw.polygon(screen,"orange",[(590,230),(590,250),(500,250),(500,230)])

    #Draw right arm
    pygame.draw.polygon(screen,"orange",[(690,230),(690,250),(780,250),(780,230)])

    #Draw left leg
    pygame.draw.polygon(screen,"orange",[(590,380),(590,480),(620,480),(620,380)])

    #Draw right leg
    pygame.draw.polygon(screen,"orange",[(690,380),(690,480),(660,480),(660,380)])

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()