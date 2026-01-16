import pygame as pg 
from konstanter import *
from paddle import *
from baller import *
from klosser import *
from powerups import *
from score import *

pg.init()

vindu = pg.display.set_mode((VINDU_BREDDE, VINDU_HOYDE))
clock = pg.time.Clock()

def main():
    running = True
    
    baller=[]
    klosser = []
    powerUps = []
    paddle = Paddle()
    
    poeng = 0
    liv = 3
    
    pg.display.set_caption("Brick Break")
    
    lagKlosser(klosser, vindu)
    
    Ball(VINDU_BREDDE/2,VINDU_HOYDE-62,baller,vindu)

    framecounter = 0
    while running:
        # framecounter+=1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                spawnBall(baller,paddle.x+paddle.bredde/2,paddle.y-12,vindu)

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and paddle.x>0:
            paddle.x -= paddle.fart
        if keys[pg.K_RIGHT] and paddle.x+paddle.bredde<VINDU_BREDDE:
            paddle.x += paddle.fart

        vindu.fill(BACKGROUNDFARGE)

        oppdaterAlleBaller(baller,paddle)
        
        if len(baller) == 0:
            if liv != 0:
                spawnBall(baller,paddle.x+paddle.bredde/2,paddle.y-12,vindu)
            liv = livTavle(liv, vindu)
        
        poeng = oppdaterKloss(klosser, baller, vindu, powerUps, poeng)
        
        paddle.tegnSelv(vindu)
        paddle.powerUpKollisjon(powerUps, baller)
        
        oppdaterPowerUps(powerUps, vindu)  

        Tavle(poeng, liv, vindu)
        
        # if framecounter % FPS == 0:
        #     print(poeng)
        
        pg.display.flip()
        clock.tick(FPS)
        
if __name__ == "__main__":
    main()