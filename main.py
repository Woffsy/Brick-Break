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
    
    paddle = Paddle()
    
    
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and paddle.x>0:
            paddle.x -= 5
        if keys[pg.K_RIGHT] and paddle.x+paddle.bredde<VINDU_BREDDE:
            paddle.x += 5

        vindu.fill(WHITE)
        
        paddle.tegnSelv(vindu)
        
        pg.display.flip()
        clock.tick(FPS)
        
if __name__ == "__main__":
    main()