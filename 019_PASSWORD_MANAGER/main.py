# change this according to your setup
LOGO_FILE = "./019_PASSWORD_MANAGER/input/logo.png"
DATA_FILE = "./019_PASSWORD_MANAGER/output/data.txt"
LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
SYMBOLS = ["#", "@", "$", "%", "^", "&", "(", ")"]


from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# FUNCTIONS
def save():
    website = get_entry(website_entry)
    email = get_entry(email_entry)
    pw = get_entry(pw_entry)

    if len(website) == 0 or len(email) == 0 or len(pw) == 0:
        messagebox.showwarning(title="Empty Fields", message="Please do not leave any fields empty.")
    else:
        save_ok = messagebox.askokcancel(title=website, message=f"Email: {email}\nPassword: {pw}\n\nIs it okay to save?")

        if save_ok:
            save_info = f"{website}  |  {email}  |  {pw}\n"

            with open(DATA_FILE, "a") as file:
                file.write(save_info)
            
            website_entry.delete(0, END)
            pw_entry.delete(0, END)
            save_info = ""

def generate_pw():
    pw_entry.delete(0, END)
    pw_chars = []
    pw_chars += [choice(LETTERS).upper() for _ in range(randint(2, 4))]
    pw_chars += [choice(LETTERS).lower() for _ in range(randint(2, 4))]
    pw_chars += [choice(SYMBOLS) for _ in range(randint(2, 4))]
    pw_chars += [str(randint(0, 9)) for _ in range(randint(2, 4))]

    shuffle(pw_chars)
    generated_pw = "".join(pw_chars)
    pw_entry.insert(0, generated_pw)
    pyperclip.copy(generated_pw)
    pw_chars = []
    generated_pw = ""

def get_entry(entry):
    return entry.get()


# WINDOW SETUP
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_png = PhotoImage(file=LOGO_FILE)
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)


# LABELS
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

pw_label = Label(text="Password:")
pw_label.grid(column=0, row=3)


# ENTRIES
website_entry = Entry()
website_entry.grid(sticky="ew", column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry()
email_entry.grid(sticky="ew", column=1, row=2, columnspan=2)
email_entry.insert(0, "ksinc@example.com")

pw_entry = Entry()
pw_entry.grid(sticky="ew", column=1, row=3)


# BUTTONS
generate_button = Button(text="Generate Password", command=generate_pw)
generate_button.grid(sticky="ew", column=2, row=3)

save_button = Button(text="Save", width=36, command=save)
save_button.grid(sticky="ew", column=1, row=4, columnspan=2)


























window.mainloop()