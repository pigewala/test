import pygame
from pygame import *
import time
class heroplay(object):
    def __init__(self,screen):
        self.player=pygame.image.load("鸽鸽.png")
        self.x=240-92
        self.y=600
        self.speed=4
        self.screen=screen
        self.bullets=[]

    def key_countrol(self):
        key_pressed=pygame.key.get_pressed()
        if key_pressed[K_a]or key_pressed[K_LEFT]:
            self.x -= self.speed
        if key_pressed[K_s]or key_pressed[K_DOWN]:
            self.y += self.speed
        if key_pressed[K_d]or key_pressed[K_RIGHT]:
            self.x += self.speed
        if key_pressed[K_w]or key_pressed[K_UP]:
            self.y -= self.speed
        if key_pressed[K_SPACE]:
            bullet=Bullet(self.screen,self.x,self.y)
            self.bullets.append(bullet)
    def display(self):
        self.screen.blit(self.player,(self.x,self.y))
        for bullet in self.bullets:
            bullet.auto_move()
            bullet.display()



class Bullet(object):
    def __init__(self,screen,x,y):
        self.x=x
        self.y=y
        self.bullet=pygame.image.load("bullet(1)(1).png")
        self.speed=6
        self.screen=screen
    def display(self):
        self.screen.blit(self.bullet,(self.x-20,self.y+50))

    def auto_move(self):
        self.y+=self.speed



def main():
    screen=pygame.display.set_mode((480,800),0,32)
    background=pygame.image.load("bg3_爱给网_aigei_com.jpg")
    player=heroplay(screen)
    while True:
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
        player.key_countrol()
        player.display()
        pygame.display.update()
        time.sleep(0.01)
if __name__=='__main__':
    main()



