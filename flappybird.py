import pygame
import sys
import random

def gameFloor():
    screen.blit(floor_base,(floor_base_x,900))
    screen.blit(floor_base,(floor_base_x + 576 ,900))

def checkCollisions(pipes):
    #When the bird hits the pipes
    for pipe in pipes:
        if bird_box.colliderect(pipe):
            return False
    #Makes sures the bird does not hit the floor and dosen't go to high
    if bird_box.top<=-100 or bird_box.bottom>=900:
        return False
    return True

def create_pipe():
    random_pipe_pos=random.choice(pipe_height)
    top_pipe=pipe_surface.get_rect(midbottom=(700,random_pipe_pos-300))
    bottom_pipe=pipe_surface.get_rect(midtop=(700,random_pipe_pos))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx-=5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom>=1024:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe=pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe) 



pygame.init()
clock=pygame.time.Clock()
#Variables
gravity=0.55
bird_movement=0
screen=pygame.display.set_mode((576,1024))

bg=pygame.image.load("C:\\Users\\Amsan\Desktop\\Side Projects\\Flappy Bird\\Images\\bg.png").convert()
bg=pygame.transform.scale2x(bg)

bird=pygame.image.load("C:\\Users\\Amsan\Desktop\\Side Projects\\Flappy Bird\\Images\\bird1.png").convert_alpha()
bird=pygame.transform.scale2x(bird)
bird_box=bird.get_rect(center=(100,512))

floor_base=pygame.image.load("C:\\Users\\Amsan\Desktop\\Side Projects\\Flappy Bird\\Images\\base.png").convert()
floor_base=pygame.transform.scale2x(floor_base)
floor_base_x=0 

message=pygame.image.load("C:\\Users\\Amsan\Desktop\\Side Projects\\Flappy Bird\\Images\\message.png").convert_alpha()
message=pygame.transform.scale2x(message)
game_over_rect=message.get_rect(center=(288,512))

#Creates Pipes
pipe_surface=pygame.image.load("C:\\Users\\Amsan\Desktop\\Side Projects\\Flappy Bird\\Images\\pipe.png")
pipe_surface=pygame.transform.scale2x(pipe_surface)
pipe_list=[]
pipe_height=[400,600,800]

SPAWNPIPE=pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)

game_active=True

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and game_active:
                bird_movement=0
                bird_movement-=10
            if event.key==pygame.K_SPACE and game_active==False:
                bird_box.center=(100,512)
                bird_movement=0
                pipe_list.clear()
                game_active=True
        if event.type==SPAWNPIPE and game_active:
            pipe_list.extend(create_pipe())
                

    screen.blit(bg,(0,0))
    if game_active:
        bird_movement+=gravity
        bird_box.centery+=bird_movement
        screen.blit(bird,bird_box)

        #Pipes
        pipe_list=move_pipes(pipe_list)
        draw_pipes(pipe_list)

        #Checking Collisons on the Floor
        game_active=checkCollisions(pipe_list)
    else:
        screen.blit(message,game_over_rect)

    #Creating Game Floor
    floor_base_x-=1
    gameFloor()
    if floor_base_x<=-576:
        floor_base_x=0

    pygame.display.update()
    clock.tick(120)
    