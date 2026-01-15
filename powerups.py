import pygame as pg
from random import choice
from klosser import *
from konstanter import *
from baller import*
from main import*
from paddle import *

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
    
    def powerUp(self, baller:list):
        if self.powerUpType == "dobbelBall":
            for i in range(len(baller)):
                dobbelBall(baller[i],baller)
        
        
        

def spawnPowerUp(kloss, powerUps: list):
    powerUpType = choice(powerUpTypes)
    
    powerUps.append(PowerUp(powerUpType, kloss))


def oppdaterPowerUps(powerUps: list, vindu, paddle):
    for powerUp in powerUps:
        powerUp.y += 2
        powerUp.tegnPowerUp(vindu)


def dobbelBall(ball:Ball, baller:list):
    Ball(ball.x, ball.y, baller, vindu)