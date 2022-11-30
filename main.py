import sys, pygame
pygame.init()
test_surface = pygame.Surface((100,200))
test_surface.fill('Red')
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
while True:
    screen.blit(test_surface,(0,0))
    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


pygame.display.update()
