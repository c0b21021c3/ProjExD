import pygame as pg
import sys
from random import randint, choice

class Screen:
    
    def __init__(self,title:str,wh:tuple,color:tuple,bg_file=None):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.color = color
        self.sfc.fill(self.color)
        self.rct = self.sfc.get_rect()

        self.bg_sfc = None
        if bg_file:#背景画像が指定されていたら、セットする
            self.bg_sfc = pg.image.load(bg_file)
            self.bg_rct = self.bg_sfc.get_rect()

    def blit(self):
        if self.bg_sfc:#背景画像があったら背景を貼る
            self.sfc.blit(self.bg_sfc,self.bg_rct)
        else: 
            self.sfc.fill(self.color)
            self.sfc.blit(self.sfc,self.rct)


class Racket:
    """initの引数：
    scr: スクリーン
    who: 0なら敵、１なら自分を指定する。
    wh: 幅と長さの順で値の入ったタプル
    """

    key_delta = {
    pg.K_UP:    -1,
    pg.K_DOWN:  +1,
    }

    def __init__(self,scr:Screen,who:bool,wh:tuple):
        self.sfc = pg.Surface(wh) # 空のSurface
        self.who = who
        w,h = wh
        pg.draw.rect(self.sfc,(255,255,255),rect=(0,0,w,h),width=0)
        self.rct = self.sfc.get_rect()
        if self.who:#自分のラケットなら、画面左端の真ん中にセット
            self.rct.center = 50, scr.rct.height/2
        else:
            self.rct.center = scr.rct.width - 50, scr.rct.height/2
            self.vy = 1

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen, color:tuple):#updateで色指定します
        if self.who:#自分のラケット
            key_states = pg.key.get_pressed()
            for key, delta in Racket.key_delta.items():
                if key_states[key]:#十字キーでの移動(上下のみ)
                    self.rct.centery += delta
                    _, vvy = check_bound(self.rct, scr.rct) 
                    if vvy == -1:#画面の上端下端についたとき
                        self.rct.centery -= delta
            self.sfc.fill(color)
        else:#敵のラケット
            _, vvy = check_bound(self.rct,scr.rct)
            if vvy ==-1:#画面の上端下端についたとき
                self.vy *= vvy
            self.rct.centery += self.vy
            self.sfc.fill(color)
        self.blit(scr) 


class Ball:

    def __init__(self, color:tuple, r, scr:Screen):
        self.sfc = pg.Surface((r*2, r*2)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (r, r), r) # ボール用の円を描く
        self.rct = self.sfc.get_rect()
        self.rct.centerx = scr.rct.width//2
        self.rct.centery = scr.rct.height//2
        self.vx, self.vy = choice([-1,1]), choice([-1,1])

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)
    
    def rkt_bound(self,rkt:Racket, scr:Screen):#ラケットにあたったら
        self.vx *= -1
        self.vy *= -1
        self.blit(scr)


def Score(my,ur,scr:Screen):#スコアの表示をする関数
    font = pg.font.Font(None,40)
    mytxt = font.render(str(my),True, (255,255,255))
    urtxt = font.render(str(ur),True, (255,255,255))
    text = font.render("-Score-",True, (255,255,255))
    for txt, place in zip([mytxt,urtxt,text],[(scr.rct.width*0.8,0),(scr.rct.width*0.2,0),(scr.rct.width*0.4,0)]):
        scr.sfc.blit(txt,place)

def check_bound(obj_rct, scr_rct):#壁の当たり判定を行う
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        pass
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


def main():
    scr = Screen("ホッケーゲーム", (500, 500),(0,255,0))#スクリーン
    my_rkt = Racket(scr,1,(20,100))
    ur_rkt = Racket(scr,0,(20,100))
    b = Ball((255, 0, 0), 10, scr)

    my_score = 0
    ur_score = 0

    clock = pg.time.Clock()
    while True:
        scr.blit() #背景貼り付け
        for event in pg.event.get():
            if event.type == pg.QUIT : return #×ボタンでいつでも辞められるように
        my_rkt.update(scr,(0,0,0))
        ur_rkt.update(scr,(255,0,0))
        b.update(scr)
        if b.rct.centerx < 0: #画面左の壁に衝突
            b = Ball((255, 0, 0), 10, scr)
            my_score += 1
        if b.rct.centerx > scr.rct.width:#画面右の壁に衝突
            b = Ball((255, 0, 0), 10, scr)
            ur_score += 1
        Score(my_score,ur_score,scr)#スコアの表示
        if ur_score == 20 or my_score == 20:#20点先取
            return
        for rkt in [my_rkt,ur_rkt]:
            if rkt.rct.colliderect(b.rct):
                b.rkt_bound(rkt,scr)
        pg.display.update() #ディスプレイの更新
        clock.tick(1000)


###実行
if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()