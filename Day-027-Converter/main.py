from tkinter import *


def convert():
    converted_num = round(float(entry.get()) * 1.60934)
    answer.config(text=converted_num)


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

entry = Entry(width=10)
entry.insert(END, 0)
entry.grid(row=0, column=1)

miles = Label(text="Miles")
miles.grid(row=0, column=2)

equal = Label(text="is equal to")
equal.grid(row=1, column=0)

answer = Label(text=entry.get())
answer.grid(row=1, column=1)

km = Label(text="Km")
km.grid(row=1, column=2)

button = Button(text="Calculate", command=convert)
button.grid(row=2, column=1)

window.mainloop()
