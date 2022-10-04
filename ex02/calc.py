from re import X
import tkinter as tk
from tkinter import messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo("警告",f"{txt}ボタンが押されました")

root = tk.Tk()
root.geometry("300x500")

x = 0
y = 1
for i, num in enumerate(range(9,-1,-1),1):
    btn= tk.Button(root, text=f"{num}",font=("",30),width=4,height=2)
    btn.bind("<1>",button_click)
    btn.grid(row=y,column=x)
    x += 1
    if i%3 == 0:
        y += 1
        x = 0

entry = tk.Entry(root, width=10, font=("",40),justify="right")
entry.grid(row=0,column=0,columnspan=3)
    
root.mainloop()