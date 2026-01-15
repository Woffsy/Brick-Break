import pygame as pg
from random import choice
from klosser import *
from konstanter import *
from baller import*
from main import*
from paddle import *

powerUpTypes = ["instaBreak", "dobbelBall", "spøkelse"]

class PowerUp:
    def __init__(self, powerUpType, kloss) -> None:
        self.x = kloss.rect.x + kloss.rect.width / 2
        self.y = kloss.rect.y
        
        self.radius = 10
        
        self.powerUpType = powerUpType
        self.color = POWERUPFARGER[powerUpType]
        
        

    def tegnPowerUp(self, vindu):
        pg.draw.circle(vindu, self.color, (self.x, self.y), self.radius)
    
    def powerUp(self, baller:list):
        if self.powerUpType == "dobbelBall":
            for i in range(len(baller)):
                dobbelBall(baller[i],baller)
        if self.powerUpType == "instaBreak":
            for b in baller:
                instabreak(b)
        if self.powerUpType == "spøkelse":
            for b in baller:
                spøkelse(b)
        
        
        

def spawnPowerUp(kloss, powerUps: list):
    powerUpType = choice(powerUpTypes)
    
    powerUps.append(PowerUp(powerUpType, kloss))


def oppdaterPowerUps(powerUps: list, vindu):
    for powerUp in powerUps:
        powerUp.y += 2
        powerUp.tegnPowerUp(vindu)


def dobbelBall(ball:Ball, baller:list):
    if len(baller) < 1000:
        Ball(ball.x, ball.y, baller, ball.vindu)

def instabreak(ball:Ball):
    ball.instaBreak=True

def spøkelse(ball:Ball):
    ball.spøkelsestart=pg.time.get_ticks()
    ball.spøkelse=True
