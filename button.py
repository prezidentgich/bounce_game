from tkinter import *


class Button:
    a = Button(text="Center Button")
    b = Button(text="Top Left Button")
    c = Button(text="Bottom Right Button")

    a.place(relx=0.5, rely=0.5, anchor=CENTER)
    b.place(relx=0.0, rely=0.0, anchor=NW)
    c.place(relx=1.0, rely=1.0, anchor=SE)


btn1 = Button()
mainloop()