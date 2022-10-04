import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showwarning("警告",f"ボタンが押されました")

root = tk.Tk()
root.title("おためし")
root.geometry("500x200")

label= tk.Label(root,
text="らべる",
font=(" ", 30),)
label.pack()

button = tk.Button(root, 
text="おすな",
bg = "Gray", 
font=("",30))
button.bind("<1>",button_click)
button.pack()

entry = tk.Entry(root, width=30, font=("",10))
entry.insert(tk.END, "ここに入力してください")
entry.pack()


root.mainloop()