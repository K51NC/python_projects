FONT = ("Arial", 12, "normal")

from tkinter import Tk, Label, Entry, Button, Text


def convert():
    km = int(input.get()) * 1.60934
    output_label_two.config(text=round(km, 2))


window = Tk()
window.minsize()
window.title("Miles to KM Converter")
window.config(padx=50, pady=50)

input = Entry(font=FONT)
input.grid(column=1, row=0)

input_label = Label()
input_label.config(text="Miles", padx=10, pady=10, font=FONT)
input_label.grid(column=2, row=0)

output_label_one = Label()
output_label_one.config(text="is equal to", padx=10, pady=10, font=FONT)
output_label_one.grid(column=0, row=1)

output_label_two = Label()
output_label_two.config(text=0, padx=10, pady=10, font=FONT)
output_label_two.grid(column=1, row=1)

output_label_three = Label()
output_label_three.config(text="Km", padx=10, pady=10, font=FONT)
output_label_three.grid(column=2, row=1)

convert_button = Button()
convert_button.config(text="Convert", command=convert, padx=10, pady=10, font=FONT)
convert_button.grid(column=1, row=2)

window.mainloop()