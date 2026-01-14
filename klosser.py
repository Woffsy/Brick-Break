import pygame as pg
from konstanter import *

class Kloss:
    def __init__(self, posisjoner: list, klosser: list, vindu) -> None:
        self.vindu = vindu
        
        self.posisjoner = posisjoner
        
        self.health = 3
        self.color = KLOSSFARGER[self.health-1]
        
        self.klosser = klosser
        self.klosser.append(self)
        
        self.rect = pg.Rect(posisjoner[0])
        
        self.image = pg.Surface((self.rect.width, self.rect.height))
        
        self.tegn_bilde()
        
    def tegn_bilde(self):
        self.image.fill(self.color)
        pg.draw.rect(self.image, (0, 0, 0), self.image.get_rect(), 2)
        
    def sjekkKollisjon(self, ball):
        if pg.Rect(self.rect).colliderect(pg.Rect(ball.x, ball.y, ball.størrelse, ball.størrelse)):
            ball.vy *= -1
            self.health -= 1
            self.color = KLOSSFARGER[self.health-1]
            self.tegn_bilde()
    
        
        
def lagKlosser(klosser: list, vindu):
    rows = 6
    cols = 5
    block_width = 80
    block_height = 30
    start_x = 50
    start_y = 50
    spacing_x = 0
    spacing_y = 0
    
    for row in range(rows):
        for col in range(cols):
            x = start_x + col * (block_width + spacing_x)
            y = start_y + row * (block_height + spacing_y)
            
            Kloss([(x, y, block_width, block_height)], klosser, vindu)



def oppdaterKloss(klosser, baller: list):
    for kloss in klosser:
        if kloss.health > 0:
            kloss.vindu.blit(kloss.image, kloss.rect)
            for b in baller:
                kloss.sjekkKollisjon(b)
        else:
            klosser.remove(kloss)
            
