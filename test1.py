
import pygame
import random
import time
pygame.init()
screen = pygame.display.set_mode((800,800))
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        self.score = 0
        
        self.x = random.randint(0,300)

        self.y = random.randint(0,300)
        self.photo = pygame.image.load("assets/bg/2744119.png")
        self.resize = pygame.transform.scale(self.photo,(120,120))
    def spawn(self):
        screen.blit(self.resize,[self.x,self.y])
        pygame.time.wait(1000)
        
       
       
        
background = pygame.image.load("assets/bg/bg.jpg")


while True:
    enemys = Enemy()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    enemys.spawn()
    pygame.time.wait(1000)
    del enemys
    

    
    pygame.display.update()
    screen.blit(background,(0,50))