from konstanter import *
from random import randint
import pygame as pg
import numpy as np

class Baller:
    def __init__(self,x,y,baller:list,vindu):
        self.størrelse=10
        self.x=x
        self.y=y
        self.fart=5
        self.vinkel=randint(-80,80)/180*np.pi
        self.vx=np.sin(self.vinkel)*self.fart
        self.vy=-np.cos(self.vinkel)*self.fart
        self.baller=baller
        self.vindu=vindu
        baller.append(self)
    
    def kill(self):
        self.baller.remove(self)
        
        

    def oppdater(self,paddle):
        self.x+=self.vx
        self.y+=self.vy
        if self.x-self.størrelse<=0 or self.x+self.størrelse>=VINDU_BREDDE:
            self.vx*=-1
        if self.y-self.størrelse<=0:
            self.vy*=-1
        if self.y-self.størrelse>VINDU_HOYDE:
            self.kill()
        pg.draw.circle(self.vindu,BLACK,(self.x,self.y),self.størrelse)
        self.sjekkKollisjon(paddle)
        
        
    def sjekkKollisjon(self, paddle):
        if pg.Rect(self.x - self.størrelse, self.y - self.størrelse, self.størrelse * 2, self.størrelse * 2).colliderect(pg.Rect(paddle.x, 1, paddle.bredde, paddle.hoyde)):
            self.vy*=-1
            self.y = paddle.y - self.størrelse - 2
            
            nyvinkel = (paddle.x+paddle.bredde/2-self.x)/180*-np.pi
            self.vx = np.sin(nyvinkel)*self.fart
            self.vy = -np.cos(nyvinkel)*self.fart

            print(f"lengde fra sentrum {(paddle.x+paddle.bredde/2-self.x)*-1}")
        
        
def spawnBall(baller:list, x, y, vindu):
    newBall = Baller(x, y, baller, vindu)

def oppdaterAlleBaller(baller:list,paddle):
    for b in baller:
        b.oppdater(paddle)



        
