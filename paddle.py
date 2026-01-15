import pygame as pg
from konstanter import *

class Paddle():
    def __init__(self) -> None:
        self.bredde = 100
        self.hoyde = 20
        self.x = VINDU_BREDDE/2-self.bredde/2
        self.y = VINDU_HOYDE-50
        
        self.fart = 5
        
        self.color = PADDLEFARGE
        
    def tegnSelv(self, vindu):
        pg.draw.rect(vindu, self.color, (self.x, self.y, self.bredde, self.hoyde))
        
    
    def powerUpKollisjon(self, powerUps: list):
        for powerUp in powerUps:
            if self.x < powerUp.x and self.x + self.bredde > powerUp.x and self.y < powerUp.y and self.y + self.hoyde > powerUp.y:
                powerUps.remove(powerUp)
                powerUp.powerUp()