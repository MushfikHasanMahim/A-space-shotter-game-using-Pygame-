import pygame
import time
import random
import os
from pygame.locals import*

pygame.font.init()
WIDTH, HEIGHT = 720, 1280
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My first Game 😀")
WHITE = (72, 89, 97)
FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
font = pygame.font.SysFont("comicsans", 40)
BULLET_VEL = 20
score = 0
MAX_BULLETS = 30
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
RED_HIT = pygame.USEREVENT + 2
YELLOW_HIT = pygame.USEREVENT + 1
# yellow spaceship 

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

# red spaceship 

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), -90)

# Space 
SPACE = pygame.transform.rotate(pygame.image.load(os.path.join("Assets", "space.png")), 90)
SPACE = pygame.transform.scale(SPACE, (WIDTH, HEIGHT))

# bullets 
yellow_bullets = []
red_bullets = []

# handle bullets 
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if yellow.colliderect(bullet):
             pygame.event.post(pygame.event.Event(YELLOW_HIT))
             yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if red.colliderect(bullet):
             pygame.event.post(pygame.event.Event(RED_HIT))
             yellow_bullets.remove(bullet) 
# draw

def draw(red, yellow, yellow_bullets, red_bullets):
    # color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
    # Texts 
    score_label = font.render(f"Score : {score}",1, (255, 255, 255))
    yellowX_label = font.render(f"Yellow (Bullets): {len(yellow_bullets)}",1, (255, 255, 255))
    redX_label = font.render(f"Red (Bullets) : {len(red_bullets)}",1, (255, 255, 255))

    WIN.fill(WHITE)
    WIN.blit(SPACE,(0, 0))   
    WIN.blit(score_label, (30, 30)) 
    WIN.blit(yellowX_label, (30, 100)) 
    WIN.blit(redX_label, (WIDTH - 200, 100)) 
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))  
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet) 
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet) 
    
    pygame.display.update()
    # time.sleep(0.2)
        

# mainloop 
       
def main():
    global score
    clock = pygame.time.Clock()
    run = True
    yellow = pygame.Rect(10, 500, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)    
    red = pygame.Rect(640, 500, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    space = pygame.Rect(0, 0, WIDTH, HEIGHT)
   
    moving = moving2 = False
    while run:
       
        clock.tick(FPS)
        draw(red, yellow, yellow_bullets,red_bullets)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            elif event.type == MOUSEBUTTONDOWN: 
                if red.collidepoint(event.pos): 
                    moving = True 
             
                if yellow.collidepoint(event.pos): 
                    moving2 = True
                    
            elif event.type == MOUSEBUTTONUP: 
    
                moving = False 
                moving2 = False   
            elif event.type == MOUSEMOTION and moving: 
    
                red.move_ip(event.rel) 
            elif event.type == MOUSEMOTION and moving2:
                yellow.move_ip(event.rel)
            elif event.type == KEYDOWN:
                if event.key == pygame.K_LCTRL and  len(yellow_bullets) < MAX_BULLETS :
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height/2 , 10, 5)
                    
                    yellow_bullets.append(bullet)
                    
                if event.key == pygame.K_RCTRL and  len(red_bullets) < MAX_BULLETS :
                    bullet = pygame.Rect(red.x, red.y + red.height // 2, 10, 5)
                    red_bullets.append(bullet)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        
        key =  pygame.key.get_pressed()
        
        # keyboard binding for yellow spaceship 
        
        if key[pygame.K_a] and yellow.x > space.x:
             yellow.x -= 5
        elif key[pygame.K_s]  and (yellow.y + 100) < HEIGHT:
             yellow.y += 5
        elif key[pygame.K_d]  and (yellow.x + 90) < WIDTH:
             yellow.x += 5
        elif key[pygame.K_w]  and yellow.y >  space.y:
             yellow.y -= 5
             
        # keyboard binding for red spaceship 
        
        if key[pygame.K_LEFT] and red.x > space.x:
             red.x -= 5
        elif key[pygame.K_DOWN] and (red.y + 97) < HEIGHT:
             red.y += 5
        elif key[pygame.K_RIGHT] and (red.x + 90) < WIDTH:
             red.x += 5
        elif key[pygame.K_UP] and red.y >  space.y:
             red.y -= 5
         
         
                          
    pygame.Quit()


# run game 

if __name__=="__main__":
    main()
    
    