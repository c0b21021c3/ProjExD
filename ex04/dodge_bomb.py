import pygame as pg
import sys
from random import randint

def check_bound(obj_rct, scr_rct):
    """
    obj_rct：こうかとんrct，または，爆弾rct
    scr_rct：スクリーンrct
    領域内：+1／領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate

    
def main():
    # 練習1
    n = 4 #残機=n-1
    for dy in range(1,n+1):
        pg.display.set_caption("逃げろ！こうかとん")
        scrn_sfc = pg.display.set_mode((1600, 900))
        scrn_rct = scrn_sfc.get_rect()
        bg_sfc = pg.image.load("fig/pg_bg.jpg")
        bg_rct = bg_sfc.get_rect()

        # 練習3
        tori_sfc = pg.image.load("fig/6.png")
        tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
        tori_rct = tori_sfc.get_rect()
        tori_rct.center = 900, 400

        # 練習5
        bomb_sfc = pg.Surface((20, 20)) # 空のSurface
        bomb_sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10) # 円を描く
        bomb_rct = bomb_sfc.get_rect()
        bomb_rct.centerx = randint(0, scrn_rct.width)
        bomb_rct.centery = randint(0, scrn_rct.height)
        # 練習6
        vx, vy = +1, +1

        
        tori_move = 1       #機能01の為に鳥の動く速さを変数化
        tri_size = 2.0      #同、大きさを変数化


        clock = pg.time.Clock() # 練習1
        while True:

            scrn_sfc.blit(bg_sfc, bg_rct) # 練習2
            
            for event in pg.event.get(): # 練習2
                if event.type == pg.QUIT:
                    return

            key_states = pg.key.get_pressed()
            if key_states[pg.K_LSHIFT]:   #左shiftを押すとこーかとんが加速する
                tori_move = 3               #早さを変更
                tori_sfc = pg.image.load("fig/3.png")   #画像変更
                if randint(1,100) == 1: tri_size *= 1.05    #確率でデメリット:鳥、肥大化す
                tori_sfc = pg.transform.rotozoom(tori_sfc, 0, tri_size)
            else : 
                tori_move = 1
                tori_sfc = pg.image.load("fig/6.png")
                tori_sfc = pg.transform.rotozoom(tori_sfc, 0, tri_size)

            if key_states[pg.K_UP]:    tori_rct.centery -= tori_move
            if key_states[pg.K_DOWN]:  tori_rct.centery += tori_move
            if key_states[pg.K_LEFT]:  tori_rct.centerx -= tori_move
            if key_states[pg.K_RIGHT]: tori_rct.centerx += tori_move
            yoko, tate = check_bound(tori_rct, scrn_rct)
            if yoko == -1:
                if key_states[pg.K_LEFT]: tori_rct.centerx += tori_move
                if key_states[pg.K_RIGHT]:tori_rct.centerx -= tori_move
                    
            if tate == -1:
                if key_states[pg.K_UP]: tori_rct.centery += tori_move
                if key_states[pg.K_DOWN]:tori_rct.centery -= tori_move  
            scrn_sfc.blit(tori_sfc, tori_rct) # 練習3

            # 連取7
            yoko, tate = check_bound(bomb_rct, scrn_rct)
            vx *= yoko
            vy *= tate
            bomb_rct.move_ip(vx, vy) # 練習6
            scrn_sfc.blit(bomb_sfc, bomb_rct) # 練習5



            # 練習8
            if tori_rct.colliderect(bomb_rct): # こうかとんrctが爆弾rctと重なったら
                break
                if dy == n:
                    return

            pg.display.update() #練習2
            clock.tick(1000)

if __name__ == "__main__":
    pg.init() # 初期化
    main() # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()