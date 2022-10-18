import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm
import random
#------------------import/def
def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global mx, my
    global cx, cy, key
    
    delta = {
        # [横座標移動分, 縦座標移動分]
        ""     : [0,  0], 
        "Up"   : [0, -1],
        "Down" : [0, +1],
        "Left" : [-1, 0],
        "Right": [+1, 0],
    }
    
    if maze[my][mx]  == 1: #壁なら
        pass
    else:#床なら
        if maze[my+delta[key][1]][mx+delta[key][0]] != 1:
            mx, my = mx+delta[key][0], my+delta[key][1] 
            
    cx, cy = mx*100+50, my*100+50
    canv.coords("k",cx, cy)
    canv.create_image(cx, cy, image=chkn,tag="tori")#足跡的に落ちてる鳥
    if maze[my][mx]  == 2: #ゴールなら
        tkm.showinfo("ゴールにつきました","ごーるですウィンドウを閉じてください")
        return
    root.after(100,main_proc)


#------------------def/main
root = tk.Tk()
root.title("迷えるこうかとん")

#キャンバス
canv = tk.Canvas(width=1500,height=900,bg="Black")
canv.pack()

###キー関連
key = ""#現在押されているキーを表す変数
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

####迷路つくる
maze=mm.make_maze(15, 9)#データとしてつくる
mm.show_maze(canv, maze)#迷路の描画

#####こーかとん
chkn = tk.PhotoImage(file=f"./ex03/fig/{str(random.randint(1,9))}.png")#こーかとｎ捕獲
cx, cy = 300, 400#こーかとｎ座標
mx, my = 1, 1 #練習11にて
canv.create_image(cx, cy, image=chkn, tag = "k")#はっつける
main_proc()#こーかとん動く

root.mainloop()