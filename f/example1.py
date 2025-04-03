import pygame
from sys import exit

from random import randint

def display_score():
    cur_time = pygame.time.get_ticks() - start_time
    score_surf = example_font.render(f"{cur_time // 100}", False, "Black")
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return cur_time

def object_movement(object_rect_list):
    if object_rect_list:
        for object_rect in object_rect_list:
            object_rect.right = object_rect.right + 5
            
            if object_rect.bottom == 300: screen.blit(zombie_minecraft, object_rect)
            else: screen.blit(fly_surf, object_rect)
            
    object_rect_list = [obstacle for obstacle in object_rect_list if obstacle.right >= 900]  
            #return object_rect_list
            
    #else: return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    
    return True

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("margulan")
clock = pygame.time.Clock()
game_active = False
start_time = 0
score = 0

example_font = pygame.font.Font("Pixeltype.ttf", 50)

example_surface = pygame.image.load("skyy.jpeg").convert()
example_surface = pygame.transform.scale(example_surface, (800, 300))

example2_surface = pygame.image.load("groundd.jpeg").convert()
example2_surface = pygame.transform.scale(example2_surface, (800, 300))

text_surface = example_font.render("margulan", False, "Black")
text_rect = text_surface.get_rect(center = (400, 50))

#Obstacles
zombie_minecraft = pygame.image.load("snail1.png").convert_alpha()
#zombie_minecraft = pygame.transform.scale(zombie_minecraft, (50, 25))
#zombie_rect = zombie_minecraft.get_rect(midbottom = (0, 300))

fly_surf = pygame.image.load("Fly1.png").convert_alpha()
#fly_rect = fly_surf.get_rect(midbottom = (0, 300))

object_rect_list = []

#player_surface = pygame.image.load("player_walk_1.png").convert_alpha()
#player_surface = pygame.transform.scale(player_surface, (100, 50))
player_rect = player_surface.get_rect(midbottom = (400, 315))
player_gravity = 0

#INTRO SCREEN
player_stand = pygame.image.load("player_walk_1.png").convert_alpha()
#player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand = pygame.transform.scale(player_stand, (300, 200))
player_stand_rect = player_stand.get_rect(midbottom = (400, 300))

    #TEXTS
title_text = example_font.render("Intro", False, "Black")
title_text_rect = title_text.get_rect(center = (400, 50))

start_text = example_font.render("Press SPACE to Start", False, "White")
start_text_rect = start_text.get_rect(center = (200, 300))

#TIMER

object_timer = pygame.USEREVENT + 1
pygame.time.set_timer(object_timer, 900)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if game_active:
            
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom == 300:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()
        
        if event.type == object_timer and game_active:
            if randint(0, 2):
                object_rect_list.append(zombie_minecraft.get_rect(midbottom = (randint(-300, -100), 300)))
            else:
                object_rect_list.append(fly_surf.get_rect(midbottom = (randint(-300, -100), 200)))

            
    if game_active:
        
        screen.blit(example_surface, (0, 0))
        screen.blit(example2_surface, (0, 300))
        #pygame.draw.rect(screen, "Violet", text_rect)
        #pygame.draw.line(screen, "Red", (0, 0), pygame.mouse.get_pos(), 10)
        #screen.blit(text_surface, text_rect)
        display_score()
        
        #Zombie
        
        """ screen.blit(zombie_minecraft, zombie_rect)
        zombie_rect.right = zombie_rect.right + 5
        if zombie_rect.left >= 800: zombie_rect.right = 0 """
        
        #Steve
        
        screen.blit(player_surface, player_rect)
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        
        #Object movements
        
        object_movement(object_rect_list)
            
        
        
        """ keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            print("pin") """
            
        #COLLISION
        
        game_active = collisions(player_rect, object_rect_list)
        
        """ if player_rect.colliderect(zombie_rect):
            game_active = False """
            
        score = display_score() // 100
        
        """ mouse_pos = pygame.mouse.get_pos()
        
        if player_rect.collidepoint(mouse_pos):
            print(pygame.mouse.get_pressed()) """
    
    else:
        screen.fill("Red")
        screen.blit(player_stand, player_stand_rect)
        screen.blit(title_text, title_text_rect)
        
        object_rect_list.clear()
        player_rect.midbottom = (400, 315)
        
        score_message = example_font.render(f"Final Score: {score}", False, "White")
        score_message_rect = score_message.get_rect(center = (200, 300))
        
        if score == 0: screen.blit(start_text, start_text_rect)
        else: screen.blit(score_message, score_message_rect)
        
    
    pygame.display.update()
    clock.tick(60)