from konstanter import *
from random import randint
import pygame as pg
import numpy as np
from score import *

class Ball:
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
        self.farge=BALLFARGE
        self.sprettCooldown=2
        self.sisteSprettX=0
        self.sisteSprettY=0
        self.spøkelse=False
        self.spøkelsestart=-10000
        self.instaBreak=False
        baller.append(self)

    
    def kill(self):
        self.baller.remove(self)
        
        

    def oppdater(self,paddle):
        self.x+=self.vx
        self.y+=self.vy
        if self.x-self.størrelse<0:
            self.x=self.størrelse
            self.vx*=-1
        elif self.x+self.størrelse>VINDU_BREDDE:
            self.x = VINDU_BREDDE-self.størrelse
            self.vx*=-1
        if self.y-self.størrelse<0:
            self.y = self.størrelse
            self.vy*=-1
        if self.y-self.størrelse>VINDU_HOYDE:
            self.kill()
        pg.draw.circle(self.vindu,self.farge,(self.x,self.y),self.størrelse)
        self.sjekkKollisjon(paddle)
        
        
    def sjekkKollisjon(self, paddle):
        nå=pg.time.get_ticks()
        if pg.Rect(self.x - self.størrelse, self.y - self.størrelse, self.størrelse * 2, self.størrelse * 2).colliderect(pg.Rect(paddle.x, paddle.y, paddle.bredde, 1)):
            self.vy*=-1
            self.y = paddle.y - self.størrelse - 2
            
            nyvinkel = (paddle.x+paddle.bredde/2-self.x)/180*-np.pi+randint(-100,100)/1000
            self.vx = np.sin(nyvinkel)*self.fart
            self.vy = -np.cos(nyvinkel)*self.fart
            if nå-self.spøkelsestart <= SPØKELSESVARIGHET:
                self.spøkelse = True
            else:
                self.spøkelse = False
        
        
def spawnBall(baller:list, x, y, vindu):
    Ball(x, y, baller, vindu)

def oppdaterAlleBaller(baller:list,paddle):
    for b in baller:
        b.oppdater(paddle)



        
