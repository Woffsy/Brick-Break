import pygame as pg
from konstanter import *

pg.font.init()

font = pg.font.SysFont("Arial", 24)
gameOverFont = pg.font.SysFont("Arial", 96)

def poengTavle(poeng, vindu):
    poeng += 1
    tekst = font.render(f'Poeng: {poeng}', False, (200, 200, 200))
    
    vindu.blit(tekst, (10, 10))
    
    return poeng

def Tavle(poeng, liv, vindu):
    tekst = font.render(f'Poeng: {poeng}', False, (255, 255, 255))
    tekstLiv = font.render(f"Liv: {liv}", False, (255, 255, 255))
    
    vindu.blit(tekst, (10, 10))
    vindu.blit(tekstLiv, (VINDU_BREDDE-60, 10))
    
    if liv == 0:
        gameOverTekst = gameOverFont.render("Game Over", False, (255, 255, 255))
        
        vindu.blit(gameOverTekst, (46, VINDU_HOYDE/2-48))
        
        
def livTavle(liv, vindu):
    liv -= 1
    tekstLiv = font.render(f"Liv: {liv}", False, (255, 255, 255))
    
    vindu.blit(tekstLiv, (VINDU_BREDDE-60, 10))
    
    return liv