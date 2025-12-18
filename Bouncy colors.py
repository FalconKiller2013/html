import pygame
pygame.init
Screen = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()
x, y = 250,170
speed=10
color = (0, 128, 255)
running = True
while running:
    Screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
                x -= speed
    if keys[pygame.K_RIGHT]:
                x += speed
    if keys[pygame.K_UP]:
                y -= speed
    if keys[pygame.K_DOWN]:
                y += speed

    if x <=0 or x +50 >=600 or y <=0 or y +50 >=400:
                color=(255,0,0)
    else:
                color=(0,128,255)
            

    pygame.draw.rect(Screen, color, (x,y,50,50))
    pygame.display.update()
    clock.tick(60)
pygame.quit()