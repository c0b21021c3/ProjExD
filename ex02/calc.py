from re import X
import tkinter as tk
from tkinter import messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    if txt == "=":
        a = entry.get()
        entry.delete(0,tk.END)
        ans = eval(a)
        txt = ans
        

    entry.insert(tk.END, txt)

root = tk.Tk()
root.geometry("300x600")

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

##＋ボタン
pls = tk.Button(root, text=f"+",font=("",30),width=3,height=2)
pls.bind("<1>",button_click)
pls.grid(row=4,column=1)

##=ボタン
pls = tk.Button(root, text=f"=",font=("",30),width=4,height=2)
pls.bind("<1>",button_click)
pls.grid(row=5,column=2)

##入力欄
entry = tk.Entry(root, width=10, font=("",40),justify="right")
entry.grid(row=0,column=0,columnspan=3)
    
root.mainloop()