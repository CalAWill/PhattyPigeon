import pygame
pygame.init()

# Set up screen and window
screen = pygame.display.set_mode((500, 800))
screen.fill((0, 0, 0))
pygame.display.set_caption("Phatty Pigeon")
pygame.display.set_icon(pygame.image.load("pixelPigeon.png"))
back1 = pygame.image.load("phattyBackground800.png")
back2 = pygame.image.load("phattyBackground800.png")
back1Val = 0
back2Val = 500

running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(back1, (back1Val, 0))
    screen.blit(back2, (back2Val, 0))

    for gameEvent in pygame.event.get():
        # Quits the game loop if the player quits the game window
        if gameEvent.type == pygame.QUIT:
            running = False

    back1Val -= 1
    back2Val -= 1
    if back1Val == -500:
        back1Val = 500
    if back2Val == -500:
        back2Val = 500

    pygame.display.update()