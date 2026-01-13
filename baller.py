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
    
    def oppdater(self):
        self.x+=self.vx
        self.y+=self.vy



        
