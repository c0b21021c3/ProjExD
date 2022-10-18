import tkinter as tk
#------------------import/def
def key_down(event):
    global key
    key = event.keysym





#------------------def/main
root = tk.Tk()
root.title("迷えるこうかとん")
#キャンバス
canv = tk.Canvas(width=1500,height=900,bg="Black")
canv.pack()
##こーかとん採取
chkn = tk.PhotoImage(file="./ex03/fig/1.png")
cx, cy = 300, 400
canv.create_image(cx, cy, image=chkn, tag = "KoKaTon")#はっつける
#キー関連
key = ""#現在押されているキーを表す変数
root.bind("<KeyPress>", key_down)


root.mainloop()