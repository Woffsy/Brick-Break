import pygame as pg
from konstanter import *

class Kloss:
    def __init__(self, posisjoner: list, klosser: list, vindu) -> None:
        self.vindu = vindu
        
        self.posisjoner = posisjoner
        
        self.health = 2
        self.color = FARGER[self.health]
        
        self.klosser = klosser
        self.klosser.append(self)
        
    def lagKlosser(self):
        for kloss in self.klosser:
            pg.draw.rect(self.vindu, self.color, ())
