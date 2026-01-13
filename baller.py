from konstanter import *
from random import randint
import numpy as np

class Baller:
    def __init__(self,x,y):
        self.størrelse=10
        self.x=x
        self.y=y
        self.fart=5
        self.vinkel=randint(80,-80)
        self.vx=np.sin(self.vinkel)*5
        self.vy=-np.cos(self.vinkel)*5
    
    def kill(self,baller:list):
        baller.remove(self)
        

    def oppdater(self):
        self.x+=self.vx
        self.y+=self.vy
        if self.x-self.størrelse<=0 or self.x+self.størrelse>=VINDU_BREDDE:
            self.vx*=-1
        if self.y-self.størrelse<=0:
            self.vy*=-1
        if self.y-self.størrelse>VINDU_HOYDE:
            self.kill()
    



def spawnBall(baller:list):
    pass

def oppdaterAlleBaller(baller:list):
    for b in baller:
        b.oppdater()



        
