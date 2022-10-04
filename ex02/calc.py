import random
import tkinter as tk
from tkinter import messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    if txt == "=":#=ボタン
        a = entry.get()
        entry.delete(0,tk.END)
        ans = eval(a)
        entry.insert(tk.END, ans)
    elif "AC" in txt:#ACボタン
        entry.delete(0,tk.END)
    elif "Rnd"in txt:#乱数Rnd用ボタン
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
for i, j in [(".",1),("00",2)]:
    btn= tk.Button(root, text=i,font=("",30),width=4,height=2)
    btn.bind("<1>",button_click)
    btn.grid(row=4,column=j)

#追加ボタン
#("ボタン",width,height,row,colmun)
btnlst = [
("+",4,1,5,0),("-",4,1,5,1),
("*",4,1,5,2),("/",3,1,5,3),
("=",3,2,3,3),("AC",3,2,1,3),
("Rnd",3,2,2,3),("%",3,2,4,3)]

for a, b, c, d, e in btnlst:
    pls = tk.Button(root, text=a,font=("",30),width=b,height=c,bg="Orange")
    pls.bind("<1>",button_click)
    pls.grid(row=d,column=e)

##入力欄
entry = tk.Entry(root, width=14, font=("",40),justify="right")
entry.grid(row=0,column=0,columnspan=5)
root.mainloop()