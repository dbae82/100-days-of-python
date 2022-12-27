from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=flashcard_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=flashcard_back)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

title = Label(text="French", fg="Black")
title.config(font=(FONT_NAME, 40, "italic"))
title.place(relx=400, rely=150)

canvas = Canvas(width=800, height=526)
flashcard_front = PhotoImage(file="images/card_front.png")
flashcard_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=flashcard_front)
card_title = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="images/wrong.png")
unknown_btn = Button(image=cross_img, highlightbackground=BACKGROUND_COLOR, command=next_card)
unknown_btn.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
known_btn = Button(image=check_img, highlightbackground=BACKGROUND_COLOR, command=is_known)
known_btn.grid(row=1, column=1)

next_card()

window.mainloop()
