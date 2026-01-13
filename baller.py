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
        self.vx=np.sin(self.vinkel)*5
        self.vy=-np.cos(self.vinkel)*5
        self.baller=baller
        self.vindu=vindu
        baller.append(self)
    
    def kill(self):
        self.baller.remove(self)
        
        

    def oppdater(self):
        self.x+=self.vx
        self.y+=self.vy
        if self.x-self.størrelse<=0 or self.x+self.størrelse>=VINDU_BREDDE:
            self.vx*=-1
        if self.y-self.størrelse<=0:
            self.vy*=-1
        if self.y-self.størrelse>VINDU_HOYDE:
            self.kill()
        pg.draw.circle(self.vindu,BLACK,(self.x,self.y),self.størrelse)
        
        
        

        
        
def spawnBall(baller:list):
    pass

def oppdaterAlleBaller(baller:list):
    for b in baller:
        b.oppdater()



        
