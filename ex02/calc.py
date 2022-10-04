import random
import tkinter as tk
from tkinter import messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    if txt == "=":
        a = entry.get()
        entry.delete(0,tk.END)
        ans = eval(a)
        entry.insert(tk.END, ans)
    elif "AC" in txt:
        entry.delete(0,tk.END)
    elif "Rnd"in txt:
        Rnd = random.randint(1,100)
        entry.insert(tk.END, Rnd)
    else:entry.insert(tk.END, txt)

root = tk.Tk()
root.geometry("400x600")

##数字盤
x = 0#column
y = 1#row
for i, num in enumerate(range(9,-1,-1),1):
    btn= tk.Button(root, text=f"{num}",font=("",30),width=4,height=2)
    btn.bind("<1>",button_click)
    btn.grid(row=y,column=x)
    x += 1
    if i%3 == 0:
        y += 1
        x = 0

###数字盤追加
#0.
btn= tk.Button(root, text="0.",font=("",30),width=4,height=2)
btn.bind("<1>",button_click)
btn.grid(row=4,column=1)
#00
btn= tk.Button(root, text="00",font=("",30),width=4,height=2)
btn.bind("<1>",button_click)
btn.grid(row=4,column=2)

##＋ボタン
pls = tk.Button(root, text=f"+",font=("",30),width=4,height=1,bg="Orange")
pls.bind("<1>",button_click)
pls.grid(row=5,column=0)
##-ボタン
pls = tk.Button(root, text=f"-",font=("",30),width=4,height=1,bg="Orange")
pls.bind("<1>",button_click)
pls.grid(row=5,column=1)
##*ボタン
pls = tk.Button(root, text=f"*",font=("",30),width=4,height=1,bg="Orange")
pls.bind("<1>",button_click)
pls.grid(row=5,column=2)
##/ボタン
pls = tk.Button(root, text=f"/",font=("",30),width=3,height=1,bg="Orange")
pls.bind("<1>",button_click)
pls.grid(row=5,column=3)
##=ボタン
pls = tk.Button(root, text=f"=",font=("",30),width=3,height=2,bg="Orange")
pls.bind("<1>",button_click)
pls.grid(row=3,column=3)
#ACボタン
pls = tk.Button(root, text=f"AC",font=("",30),width=3,height=2,bg="Orange")
pls.bind("<1>",button_click)
pls.grid(row=1,column=3)
#乱数randomボタン
pls = tk.Button(root, text=f"Rnd",font=("",30),width=3,height=2,bg="Orange")
pls.bind("<1>",button_click)
pls.grid(row=2,column=3)
#%ボタン
pls = tk.Button(root, text=f"%",font=("",30),width=3,height=2,bg="Orange")
pls.bind("<1>",button_click)
pls.grid(row=4,column=3)

##入力欄
entry = tk.Entry(root, width=14, font=("",40),justify="right")
entry.grid(row=0,column=0,columnspan=5)
root.mainloop()