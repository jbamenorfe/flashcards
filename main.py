BACKGROUND_COLOR = "#B1DDC6"
TITLE_TEXT_FONT = "Arial", 40, "italic"
WORD_TEXT_FONT = "Arial", 60, "bold"

from tkinter import *
import pandas
import random

# Read the french_words.csv file
original_words_to_learn_csv = pandas.read_csv("data/french_words.csv")
# Convert words_csv to dictionary
original_words_to_learn_dict = original_words_to_learn_csv.to_dict(orient="records")

def generate_next_card():
    current_word_group = random.choice(original_words_to_learn_dict)
    french_word = current_word_group["French"]
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=french_word)

# Create a Tkinter object called "window".
window = Tk()       # Create teh window object
window.title("Flashy")      # Set the window's title
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)     # Set the window's x and y padding, and background color

# Create a canvas object
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)       # Create the canvas object, and give it width and height. Set its border to invisible.
front_image = PhotoImage(file="images/card_front.png")  # Upload the card_front.png image and assign it to front_image variable
canvas.create_image(400, 263, image=front_image)
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
check_button = Button(image=right_image, highlightthickness=0, command=generate_next_card)
check_button.grid(row=1, column=1)

generate_next_card()






window.mainloop()




