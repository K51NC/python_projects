RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "✔"
WORK_MIN = 25 * 60 # minutes * 60
SHORT_BREAK_MIN = 5 * 60 # minutes * 60
LONG_BREAK_MIN = 20 * 60 # minutes * 60
WATER_TIMER = 15 * 60 # minutes * 60
# change this to your specific setup
TOMATO_FILE = "./input/tomato.png"
WATER_FILE = "./input/water_drop.png"

from tkinter import Tk, Button, Label, Canvas, PhotoImage, messagebox
import math
import os


def pomo_start():
    global step
    global checkmarks_qty
    reset_button.grid(column=2, row=2)
    start_button.grid_forget()

    step += 1
    
    checkmark_label.config(text=CHECK_MARK * checkmarks_qty)

    if step == 8:
        main_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN, "long_break")
        checkmarks_qty = 0
    elif step == 9:
        pomo_reset()
    elif step % 2 == 0:
        main_label.config(text="Break", fg=RED)
        count_down(SHORT_BREAK_MIN, "short_break")
    else:
        main_label.config(text="Work", fg=GREEN)
        checkmarks_qty += 1
        count_down(WORK_MIN, "work")

def pomo_reset():
    global step
    global checkmarks_qty
    step = 0
    checkmarks_qty = 0
    main_label.config(text="Timer", fg=GREEN)
    window.after_cancel(timer)
    checkmark_label.config(text="")
    tomato_canvas.itemconfig(timer_text, text="00:00")
    start_button.grid(column=0, row=2)
    reset_button.grid_forget()


def count_down(count, type):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    tomato_canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1, type)
    else:
        if type == "short_break":
            messagebox.showinfo(title="Break is Over", message="Start next pomodoro?")
        elif type == "long_break":
            messagebox.showinfo(title="Break is Over", message="Long break "
                                "is over. Choose 'Start' to begin a new pomodoro cycle.")
        elif type == "work":
            messagebox.showinfo(title="Break Time", message="Begin break?")
        pomo_start()
    
def water_reset(event):
    if event:
        water_canvas.grid_forget()
        water_counter(WATER_TIMER)
    else:
        water_canvas.grid(column=0, row=0)
        water_canvas.bind("<Button-1>", water_reset)

def water_counter(count):
    # remove these two lines below if you don't want
    # your 'cmd' or 'powershell' window showing a water timer
    os.system("cls")
    print(f"Water count remaining (seconds): {count}")

    if count > 0:
        water_canvas.after(1000, water_counter, count - 1)
    else:
        water_reset(0)


checkmarks_qty = 0
step = 0
timer = None


# WINDOW SETUP
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

tomato_canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file=TOMATO_FILE)
tomato_canvas.create_image(100, 112, image=tomato_png)
timer_text = tomato_canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
tomato_canvas.grid(pady=5, column=1, row=1)

water_canvas = Canvas(width=50, height=50, background=YELLOW, highlightthickness=0)
water_png = PhotoImage(file=WATER_FILE)
water_canvas.create_image(25, 25, image=water_png)
water_canvas.grid(column=0, row=0)
water_reset(0)

invis_canvas_one = Canvas(width=100, height=50, background=YELLOW, highlightthickness=0)
invis_canvas_one.grid(column=0, row=1)

invis_canvas_two = Canvas(width=100, height=50, background=YELLOW, highlightthickness=0)
invis_canvas_two.grid(column=2, row=1)


# LABELS
main_label = Label(text="Timer", font=(FONT_NAME, 40), background=YELLOW, fg=GREEN)
main_label.grid(column=1, row=0)

checkmark_label = Label()
checkmark_label.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
checkmark_label.grid(column=1, row=3)


# BUTTONS
start_button = Button(text="Start", font=(FONT_NAME, 12), command=pomo_start)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 12), command=pomo_reset)


window.mainloop()
