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
    klosser = []
    paddle = Paddle()
    
    lagKlosser(klosser, vindu)
    print(len(klosser))

    Baller(VINDU_BREDDE/2,VINDU_HOYDE-62,baller,vindu)

    framecounter = 0
    while running:
        framecounter+=1
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

        
        paddle.tegnSelv(vindu)
        oppdaterAlleBaller(baller,paddle)
        
        tegnKlosser(klosser)
        
        
        if framecounter % FPS == 0:
            print("Antall klosser:", len(klosser)) 
        

        pg.display.flip()
        clock.tick(FPS)
        
if __name__ == "__main__":
    main()