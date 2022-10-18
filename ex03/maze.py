import tkinter as tk
import maze_maker as mm
#------------------import/def
def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, key
    
    if key=="Up":#キーによる移動条件分岐
        cy -= 20
    if key=="Down":
        cy += 20
    if key=="Left":
        cx -= 20
    if key=="Right":
        cx += 20
    canv.coords("k",cx, cy)
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
chkn = tk.PhotoImage(file="./ex03/fig/1.png")#こーかとｎ捕獲
cx, cy = 300, 400#こーかとｎ座標
canv.create_image(cx, cy, image=chkn, tag = "k")#はっつける
main_proc()#こーかとん動く


root.mainloop()