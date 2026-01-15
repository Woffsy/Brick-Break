import pygame as pg
from baller import *
from konstanter import *
from powerups import *
from random import randint

class Kloss:
    def __init__(self, posisjoner: list, klosser: list, vindu) -> None:
        self.vindu = vindu
        
        self.posisjoner = posisjoner
        self.kant={
            "venstre": self.posisjoner[0][0],
            "høyre": self.posisjoner[0][0]+self.posisjoner[0][2],
            "top": self.posisjoner[0][1],
            "bunn": self.posisjoner[0][1]+self.posisjoner[0][3]
        }

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
        
    def sjekkKollisjon(self, ball:Ball):
        nå=pg.time.get_ticks()
        ball.sisteKloss=self
        if pg.Rect(self.rect).colliderect(pg.Rect(ball.x-ball.størrelse, ball.y-ball.størrelse, ball.størrelse*2, ball.størrelse*2)):
            if min(abs(ball.y-ball.størrelse-self.kant["bunn"]), abs(self.kant["top"]-ball.y-ball.størrelse)) < min(abs(ball.x-self.kant["høyre"]-ball.størrelse), abs(self.kant["venstre"]-ball.x-ball.størrelse)):
                if nå-ball.sisteSprettY>=ball.sprettCooldown:
                    ball.vy *= -1
                    ball.sisteSprettY=nå
            else:
                if nå-ball.sisteSprettX>=ball.sprettCooldown:
                    ball.vx *= -1
                    ball.sisteSprettX=nå
            if ball.instaBreak == False:
                self.health -= 1
                if self.health > 0:
                    self.color = KLOSSFARGER[self.health-1]
            if ball.instaBreak == True:
                self.health = 0
                ball.instaBreak = False
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



def oppdaterKloss(klosser, baller: list, vindu, powerUps):
    for kloss in klosser:
        if kloss.health > 0:
            kloss.vindu.blit(kloss.image, kloss.rect)
            for b in baller:
                kloss.sjekkKollisjon(b)
        else:
            klosser.remove(kloss)
            if randint(0, 100) > 90:
                spawnPowerUp(kloss, powerUps) #type: ignore
            
    if len(klosser) == 0:
        lagKlosser(klosser, vindu)
        for ball in baller:
            ball.fart += 1
            
