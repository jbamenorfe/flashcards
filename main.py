BACKGROUND_COLOR = "#B1DDC6"
TITLE_TEXT_FONT = "Arial", 40, "italic"
WORD_TEXT_FONT = "Arial", 60, "bold"

from tkinter import *
import pandas
import random
current_card = {}
words_to_learn = {}

try:
    # Read the french_words.csv file
    words_to_learn_csv = pandas.read_csv("data/updated_words_to_learn.csv")
except FileNotFoundError:
    original_words_to_learn_csv = pandas.read_csv("data/french_words.csv")
    words_to_learn = original_words_to_learn_csv.to_dict(orient="records")
else:
    # Convert words_csv to dictionary
    words_to_learn = words_to_learn_csv.to_dict(orient="records")


def generate_next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    french_word = current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    canvas.itemconfig(card_background_image, image=card_front_image)
    flip_timer= window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    english_word = current_card["English"]
    canvas.itemconfig(card_word, text=english_word, fill="white")
    canvas.itemconfig(card_background_image, image=card_back_image)

def word_is_known():
    words_to_learn.remove(current_card)
    updated_words_learn = pandas.DataFrame(words_to_learn)
    updated_words_learn.to_csv("data/updated_words_to_learn.csv")
    generate_next_card()

# Create a Tkinter object called "window".
window = Tk()       # Create teh window object
window.title("Flashy")      # Set the window's title
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)     # Set the window's x and y padding, and background color

flip_timer = window.after(3000, func=flip_card)

# Create a canvas object
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)       # Create the canvas object, and give it width and height. Set its border to invisible.
card_front_image = PhotoImage(file="images/card_front.png")  # Upload the card_front.png image and assign it to front_image variable
card_back_image = PhotoImage(file="images/card_back.png")
card_background_image = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=TITLE_TEXT_FONT)
card_word = canvas.create_text(400, 253, text="", font=WORD_TEXT_FONT)

# Create Buttons
####    Create wrong/cross button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=generate_next_card)
wrong_button.grid(row=1, column=0)

####    Create right/check button
right_image = PhotoImage(file="images/right.png")
check_button = Button(image=right_image, highlightthickness=0, command=word_is_known)
check_button.grid(row=1, column=1)

generate_next_card()

window.mainloop()




