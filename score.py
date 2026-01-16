import pygame as pg
import sys

pg.font.init()

font = pg.font.SysFont("Arial", 24)

def poengTavle(poeng, vindu):
    poeng += 1
    tekst = font.render(f'Poeng: {poeng}', False, (200, 200, 200))
    
    vindu.blit(tekst, (10, 10))
    
    return poeng

def tegnPoengTavle(poeng, vindu):
    tekst = font.render(f'Poeng: {poeng}', False, (200, 200, 200))
    
    vindu.blit(tekst, (10, 10))

