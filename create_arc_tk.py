from tkinter import *


tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
canvas.create_arc(10, 10, 200, 100, extent=270, style=ARC)
tk.mainloop()