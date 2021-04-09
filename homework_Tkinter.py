import tkinter as tk
window = tk.Tk()
window.title("Menu")
window.geometry("300x300")

menubar = tk.Menu(window)

filemenu = tk.Menu(menubar,tearoff = False)
filemenu.add_command(label="開新遊戲")
filemenu.add_command(label="作弊指令")
filemenu.add_separator()
filemenu.add_command(label = "EXIT")

menubar.add_cascade(label="檔案",menu = filemenu)

filemenu2 = tk.Menu(menubar,tearoff=False)
filemenu2.add_command(label="遊戲設定")
filemenu2.add_command(label="畫面設定")
menubar.add_cascade(label="設定",menu=filemenu2)

submenu = tk.Menu(menubar,tearoff=False)
submenu.add_command(label="遊戲優化")
submenu.add_command(label="攻擊敵人")

filemenu2.add_cascade(label="進階設定",menu=submenu)

window.config(menu=menubar)

window.mainloop()
