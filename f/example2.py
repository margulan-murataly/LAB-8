import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Без update()")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 255))  # Должен закрасить фон в синий
    pygame.display.update()
    clock.tick(60)  # Ограничение FPS

pygame.quit()