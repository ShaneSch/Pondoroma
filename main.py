from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK = "✔ "
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset():
    global reps
    window.after_cancel(timer)
    cava.itemconfig(timertext, text="00:00")
    titlelabel.config(text="Timer")
    checks.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def starttimer():
    global reps
    reps += 1
    longbreaksec = LONG_BREAK_MIN * 60
    shortbreaksec = SHORT_BREAK_MIN * 60
    worksecs = WORK_MIN * 60
    if reps % 8 == 0:
        countdown(longbreaksec)
        titlelabel.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(shortbreaksec)
        titlelabel.config(text="Break", fg=PINK)
    else:
        countdown(worksecs)
        titlelabel.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    countmin = math.floor(count / 60)
    countsec = count % 60
    if countsec == 0:
        countsec = "00"
    elif countsec < 10:
        countsec = f"0{countsec}"
    cava.itemconfig(timertext, text=f"{countmin}:{countsec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        starttimer()
        marks = ""
        worksessions = math.floor(reps/2)
        for _ in range(worksessions):
            marks += CHECK
        checks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

cava = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
cava.create_image(100, 112, image=tomato)
timertext = cava.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
cava.grid(column=1, row=1)

titlelabel = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "normal"), highlightthickness=0)
titlelabel.grid(column=1, row=0)

startbutton = Button(text="Start", highlightthickness=0, command=starttimer)
startbutton.grid(column=0, row=2)

resetbutton = Button(text="Reset", highlightthickness=0, command=reset)
resetbutton.grid(column=2, row=2)

checks = Label(fg=GREEN, bg=YELLOW)
checks.grid(column=1, row=3)
window.mainloop()
