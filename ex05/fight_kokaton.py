import pygame as pg
import sys
from random import randint

BOMBSNUM = randint(3,10)

class Screen:

    def __init__(self, title, width_height:tuple, bg_file_name:str):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(width_height)
        self.rct = self.sfc.get_rect()
        # スクリーン   /   背景
        self.bg_sfc = pg.image.load(bg_file_name)
        self.bg_rct = self.bg_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bg_sfc, self.bg_rct)


class Bird:

    key_delta = key_delta = {
    pg.K_UP:    [0, -1],
    pg.K_DOWN:  [0, +1],
    pg.K_LEFT:  [-1, 0],
    pg.K_RIGHT: [+1, 0],
}

    def __init__(self, img_name, zoom, xy:tuple):
        sfc = pg.image.load(img_name)
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():

            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]

                if check_bound(self.rct, self.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        self.blit(scr)


class Bomb:

    def __init__(self, color:tuple, r, vxy:tuple, scr:Screen):
        self.sfc = pg.Surface((r*2, r*2)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (r, r), r) # 爆弾用の円を描く
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr) # 練習5
    
    def kkt_bound(self,kkt:Bird, scr:Screen):#こうかとんに当たったら跳ね返る機能
        self.vx *= -1
        self.vy *= -1
        self.blit(scr)


class Baby: #赤ちゃんのクラス

    def __init__(self, img, scr:Screen):
        sfc = pg.image.load(img)
        self.sfc = pg.transform.rotozoom(sfc, 0, 0.8)
        self.rct = self.sfc.get_rect()
        x, y = randint(10, scr.rct.width), randint(10, scr.rct.height)#画面上でランダムに設置
        self.rct.center = ((x,y))

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

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

    scr = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")

    kkt = Bird("fig/6.png", 2.0, (900, 400))
    bab = Baby("fig/1.png", scr) #赤ちゃんの設置

    bkds = [Bomb((randint(0,255),randint(0,255) , randint(0,255)), 10, (+1, +1), scr) for i in range(BOMBSNUM)]

    clock = pg.time.Clock() # 練習1
    while True:
        scr.blit() #背景貼り付け
        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return

        kkt.update(scr)#こーかとんを移動後の座標に貼り付ける
        bab.blit(scr)
        
        #爆弾を移動後の座標に貼り付ける
        for bkd2 in bkds:
            bkd2.update(scr)
            if kkt.rct.colliderect(bkd2.rct):
                bkd2.kkt_bound(kkt,scr)
            if bab.rct.colliderect(bkd2.rct):
                return

        pg.display.update() #練習2
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()
