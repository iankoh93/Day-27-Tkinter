from tkinter import *


def button_clicked():
    output_km["text"] = float(my_input.get()) * 1.60934


FONT = ("Comic Sans", 16, "normal")
window = Tk()
window.title("My first GUI program")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)


is_equal_to = Label(text="is equal to", font=FONT)
is_equal_to.grid(column=0, row=1)


button = Button()
button.config(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

km = Label(text="Km", font=FONT)
km.grid(column=2, row=1)

miles = Label(text="Miles", font=FONT)
miles.grid(column=2, row=0)

output_km = Label(text="0", font=FONT, padx=20)
output_km.grid(column=1, row=1)

my_input = Entry(width=10)
my_input.grid(column=1, row=0)
# my_input.pack()


window.mainloop()
