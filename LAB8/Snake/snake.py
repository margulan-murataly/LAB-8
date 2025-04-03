import pygame
import sys
import random

pygame.init()
width, height = 500, 500
cell_size = 20
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Snake')

#COLORS
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)

#SNAKE
snake_pos = [100, 100]
snake_body = [[100, 100], [80, 100], [60, 100]]
direction = 'RIGHT'
change_to = direction
score = 0
level = 1
speed = 10
food_eaten = 0

#FOOD
def get_random_food(snake_body):
    while True:
        x = random.randrange(0, width, cell_size)
        y = random.randrange(0, height, cell_size)
        if [x, y] not in snake_body:
            return [x, y]

food_pos = get_random_food(snake_body)

clock = pygame.time.Clock()
font = pygame.font.Font("Pixeltype.ttf", 20)

#LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    direction = change_to

    if direction == 'UP':
        snake_pos[1] -= cell_size
    elif direction == 'DOWN':
        snake_pos[1] += cell_size
    elif direction == 'LEFT':
        snake_pos[0] -= cell_size
    elif direction == 'RIGHT':
        snake_pos[0] += cell_size

#COLLIDES
    if (snake_pos[0] < 0 or snake_pos[0] >= width or
        snake_pos[1] < 0 or snake_pos[1] >= height):
        running = False
    snake_body.insert(0, list(snake_pos))
    
#EATING FOOD CHECK
    if snake_pos == food_pos:
        score += 1
        food_eaten += 1
        food_pos = get_random_food(snake_body)
        if food_eaten % 5 == 0:
            level += 1
            speed += 2
    else:
        snake_body.pop()

    if snake_pos in snake_body[1:]:
        running = False

#FINAL DRAWING
    screen.fill(black)
    for block in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], cell_size, cell_size))
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], cell_size, cell_size))

#SCORES
    score_text = font.render(f'Score: {score}  Level: {level}', True, white)
    screen.blit(score_text, [10, 10])

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
sys.exit()





