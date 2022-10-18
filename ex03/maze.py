import tkinter as tk
#------------------import/def





#------------------def/main
root = tk.Tk()
root.title("迷えるこうかとん")

canv = tk.Canvas(width=1500,height=900,bg="Black")
canv.pack()

chkn = tk.PhotoImage(file="./ex03/fig/1.png")
cx, cy = 300, 400
canv.create_image(cx, cy, image=chkn, tag = "KoKaTon")

root.mainloop()