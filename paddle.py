import pygame as pg
from konstanter import *

class Paddle():
    def __init__(self) -> None:
        self.x = VINDU_BREDDE/2
        self.y = VINDU_HOYDE-50
        
        self.color = BLACK
        
    def tegnSelv(self, vindu):
        pg.draw.rect(vindu, self.color, (self.x, self.y, 50, 20))