import pygame as pg
import sys

pg.font.init()

font = pg.font.SysFont("Arial", 24)

def poengTavle(vindu):
    global poeng
    poeng += 1
    tekst = font.render(f'Poeng: {poeng}', False, (255, 255, 255))
    
    vindu.blit(tekst, (10, 10))
