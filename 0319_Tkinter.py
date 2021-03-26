import tkinter as tk
import tkinter.messagebox

def clickme():
    tkinter.messagebox.showinfo(title='提示',message='不要碰')

window = tk.Tk()

window.title('俊嘉的第一個GUI程式')

window.geometry('300x300')

label = tk.Label(window,text='俊嘉的GUL',bg='#000',fg="#FFF")
label.pack()

entry = tk.Entry(window,width = 20)
entry.pack()

button = tk.Button(window,text = "點我點我!",command = clickme)
button.pack()


window.mainloop()
