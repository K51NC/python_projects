RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "✔"
WORK_MIN = 25 * 60 # minutes * 60
SHORT_BREAK_MIN = 5 * 60 # minutes * 60
LONG_BREAK_MIN = 20 * 60 # minutes * 60
# change this to you specific setup
TOMATO_FILE = "./018_POMODORO/input/tomato.png"


from tkinter import Tk, Button, Label, Canvas, PhotoImage
import math


def pomo_start():
    global step
    global checkmarks_qty
    step += 1
    
    checkmark_label.config(text=CHECK_MARK * checkmarks_qty)

    if step == 8:
        step = 0
        main_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN)
        checkmarks_qty = 0
    elif step % 2 == 0:
        main_label.config(text="Break", fg=RED)
        count_down(SHORT_BREAK_MIN)
    else:
        main_label.config(text="Work", fg=GREEN)
        checkmarks_qty += 1
        count_down(WORK_MIN)

def pomo_reset():
    global step
    global checkmarks_qty
    step = 0
    checkmarks_qty = 0
    main_label.config(text="Timer", fg=GREEN)
    window.after_cancel(timer)
    checkmark_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")

def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        pomo_start()


checkmarks_qty = 0
step = 0
timer = None


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file=TOMATO_FILE)
canvas.create_image(100, 112, image=tomato_png)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

main_label = Label(text="Timer", font=(FONT_NAME, 40), background=YELLOW, fg=GREEN)
main_label.grid(column=1, row=0)

start_button = Button(text="Start", font=(FONT_NAME, 12), command=pomo_start)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 12), command=pomo_reset)
reset_button.grid(column=2, row=2)

checkmark_label = Label()
checkmark_label.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
checkmark_label.grid(column=1, row=3)


window.mainloop()
