import pygame as pg 
from konstanter import *
from paddle import *
from baller import *
from klosser import *

pg.init()

vindu = pg.display.set_mode((VINDU_BREDDE, VINDU_HOYDE))
clock = pg.time.Clock()

def main():
    running = True
    
    baller=[]
    paddle = Paddle()

    ball = Baller(VINDU_BREDDE/2,VINDU_HOYDE-62,baller,vindu)


    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and paddle.x>0:
            paddle.x -= paddle.fart
        if keys[pg.K_RIGHT] and paddle.x+paddle.bredde<VINDU_BREDDE:
            paddle.x += paddle.fart

        vindu.fill(WHITE)

        
        paddle.tegnSelv(vindu)
        oppdaterAlleBaller(baller)
        ball.sjekkKollisjon(paddle)

        pg.display.flip()
        clock.tick(FPS)
        
if __name__ == "__main__":
    main()