from tkinter import Label, Canvas, Tk, PhotoImage, Button
import pandas as pd
import assets

# FUNCTIONS
def get_unused_words():
    """
    Creates and returns unused words.
    Returns: Pandas DataFrame
    """
    unused_words = pd.read_csv(assets.ES_UNUSED_FILE, index_col=0)

    used_words, saved_file_columns = get_used_words()

    unused_words = unused_words[~unused_words.isin(used_words)]
    unused_words = unused_words[unused_words["es"].notna()]
    unused_words = unused_words.drop("fr", axis=1)
    return unused_words, saved_file_columns

def get_used_words():
    used_words = pd.read_csv(assets.ES_USED_FILE, index_col=0)
    saved_file_columns = used_words.columns.values
    return used_words, saved_file_columns

def get_active_word():
    global front_active_word
    global back_active_word
    global active_word

    active_word = unused_words.sample(1)
    front_active_word = active_word["es"].item()
    back_active_word = active_word["en"].item()

def card_front():
    back_canvas.grid_forget()
    get_active_word()
    front_canvas.grid(column=0, row=0, columnspan=2)
    front_title()
    front_word()
    window.after(3000, card_back)

def card_back():
    wrong_canvas.grid(column=0, row=1)
    right_canvas.grid(column=1, row=1)
    front_canvas.grid_forget()
    back_canvas.grid(column=0, row=0, columnspan=2)
    back_title()
    back_word()

def front_title():
    global lang_label

    lang_label.grid_forget()
    lang_label = Label(
        text=front_lang,
        font=assets.TITLE_FONT,
        bg="white",
        highlightthickness=0
        )
    lang_label.grid(sticky="n", pady=100, column=0, row=0, columnspan=2)

def front_word():
    global word_label

    word_label.grid_forget()
    word_label = Label(
        text=front_active_word,
        font=assets.WORD_FONT,
        bg="white",
        highlightthickness=0
        )
    word_label.grid(column=0, row=0, columnspan=2)

def back_title():
    global lang_label

    lang_label.grid_forget()
    lang_label = Label(
        text=back_lang,
        font=assets.TITLE_FONT,
        fg="white",
        bg=assets.CARD_BACK_COLOR
        )
    lang_label.grid(sticky="n", pady=100, column=0, row=0, columnspan=2)

def back_word():
    global word_label

    word_label.grid_forget()
    word_label = Label(
        text=back_active_word,
        font=assets.WORD_FONT,
        fg="white",
        bg=assets.CARD_BACK_COLOR
        )
    word_label.grid(column=0, row=0, columnspan=2)

def right():
    save_word()
    get_active_word()
    reset()

def wrong():
    get_active_word()
    reset()

def reset():
    wrong_canvas.grid_forget()
    right_canvas.grid_forget()
    card_front()

def save_word():
    global unused_words
    global active_word

    unused_words.drop(active_word.first_valid_index(), axis=0, inplace=True)
    word = pd.DataFrame(active_word, columns=saved_file_columns)
    word.to_csv(assets.ES_USED_FILE, mode="a", header=None)

def clear_saved():
    """
    Clears save file, then destroys window.
    """
    empty_df = pd.DataFrame(columns=saved_file_columns)
    empty_df.to_csv(assets.ES_USED_FILE)
    window.destroy()


# INITS
unused_words = None
front_lang = "Spanish"
back_lang = "English"
active_word = None
front_active_word = None
back_active_word = None
saved_file_columns = []


# WINDOW
window = Tk()
window.title("Flash Cards")
window.config(bg=assets.BG_COLOR, padx=50, pady=50)

place_holder = Canvas(
    width=100,
    height=100,
    bg=assets.BG_COLOR,
    highlightthickness=0
    )
place_holder.grid(column=0, row=1, columnspan=2)


# CARD
front_canvas = Canvas(
    width=800,
    height=526,
    bg=assets.BG_COLOR,
    highlightthickness=0
    )
front_png = PhotoImage(file=assets.CARD_FRONT_FILE)
front_canvas.create_image(400, 263, image= front_png)
front_canvas.grid(column=0, row=0, columnspan=2)

back_canvas = Canvas(
    width=800,
    height=526,
    bg=assets.BG_COLOR,
    highlightthickness=0
    )
back_png = PhotoImage(file=assets.CARD_BACK_FILE)
back_canvas.create_image(400, 263, image= back_png)


# BUTTONS
wrong_canvas = Canvas(
    width=100,
    height=100,
    bg=assets.BG_COLOR,
    highlightthickness=0,
    )
wrong_png = PhotoImage(file=assets.WRONG_BUTTON_FILE)
wrong_canvas.create_image(50, 50, image=wrong_png)
wrong_canvas.bind("<Button-1>", lambda x: wrong())

clear_button = Button(text="Clear Saved File")
clear_button.bind("<Button-1>", lambda x: clear_saved())
clear_button.grid(column=0, row=1, columnspan=2)

right_canvas = Canvas(
    width=100,
    height=100,
    bg=assets.BG_COLOR,
    highlightthickness=0
    )
right_png = PhotoImage(file=assets.RIGHT_BUTTON_FILE)
right_canvas.create_image(50, 50, image=right_png)
right_canvas.bind("<Button-1>", lambda x: right())


# LABELS
lang_label = Label(text="Language", font=assets.TITLE_FONT, bg="white")

word_label = Label(text="Word", font=assets.WORD_FONT, bg="white")

unused_words, saved_file_columns = get_unused_words()
card_front()


window.mainloop()