import tkinter
# Import every single class from tkinter without having to call the module
from tkinter import *


def button_clicked():
    my_label["text"] = my_input.get()


window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=700, height=500)

# Label
my_label = tkinter.Label(text="I am a label", font=("Comic Sans", 16, "normal"))
my_label.pack()

# Button
button = Button()
button.config(text="Click me", command=button_clicked)
button.pack()

# Entry
my_input = Entry(width=10)
my_input.pack()


window.mainloop()
