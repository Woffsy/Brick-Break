import pygame as pg
from random import choice
from klosser import *
from konstanter import *

powerUpTypes = ["dobbelDamage", "dobbelBall", "spøkelse"]
powerUps = []

class PowerUp:
    def __init__(self, powerUpType, kloss) -> None:
        self.x = kloss.rect.x + kloss.rect.width / 2
        self.y = kloss.rect.y
        
        self.radius = 10
        
        self.powerUpType = powerUpType
        self.color = POWERUPFARGER[powerUpType]
        
        

    def tegnPowerUp(self, vindu):
        pg.draw.circle(vindu, self.color, (self.x, self.y), self.radius)
        
        
        

def spawnPowerUp(kloss, powerUps: list):
    powerUpType = choice(powerUpTypes)
    
    powerUps.append(PowerUp(powerUpType, kloss))


def oppdaterPowerUps(powerUps: list, vindu):
    for powerUp in powerUps:
        powerUp.y += 2
        powerUp.tegnPowerUp(vindu)