import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader")
player_x= 370
player_y= 520
player_speed = 5 
enemy_x = random.randint(0, 736)
enemy_y = 50
enemy_speed = 3
bullet_x = 0 
bullet_y = 520
bullet_speed = 7
bullet_state = "ready"
score = 0 
font = pygame.font.SysFont(None,36)
def show_score():
    text = font.render("Score : "+ str(score),True,(255,255,255))
    screen.blit(text,(10,10))

running =True
while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x + 16
                    bullet_state = "fire"

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
      player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < 736:
      player_x += player_speed

    enemy_y +=enemy_speed
    if enemy_y> 600:
        enemy_x = random.randint(0,736)
        enemy_y = 50

    if bullet_state == "fire":
        bullet_y -=bullet_speed
        pygame.draw.rect(screen,(255,255,0),(bullet_x,bullet_y,4,10))
        if bullet_y < 0:
            bullet_y = 520
            bullet_state = "ready"

    if enemy_y < bullet_y < enemy_y + 40 and enemy_x < bullet_x < enemy_x + 40:
        bullet_y = 520
        bullet_state = "ready"
        score += 1
        enemy_x = random.randint(0,736)
        enemy_y = 50
    pygame.draw.rect(screen,(0,255,0),(player_x,player_y,40,40))
    pygame.draw.rect(screen,(255,0,0),(player_x,player_y,40,40))

    show_score()
    pygame.display.update()