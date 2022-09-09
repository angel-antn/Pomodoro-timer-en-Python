import tkinter as tk
from timer import Timer
from playsound import playsound

PINK = "#e2979c"
GREEN = "#7ad087"
YELLOW = "#f7f5dd"
GRAY = "#6d6d6d"
FONT_TITLE = ('Arial black', 28, 'bold')
FONT = ('Arial black', 12, 'bold')
FONT_CHECKS = ('Arial black', 16, 'bold')

timer = Timer()


def start_timer():

    start_button.config(state=tk.DISABLED)

    if timer.is_on:

        checkmarks = ''
        for i in range(0, timer.reps, 2):
            if len(checkmarks) < 3:
                checkmarks += '✔'
            else:
                checkmarks = 'Well Done! Now Rest'
        check_mark_label.config(text=checkmarks)

        if timer.reps % 2 == 0:
            playsound('sounds/start.mp3', False)
            title_label.config(text='Pomodoro Start!', padx=3, fg=GREEN)
            window.config(padx=60)
        elif timer.reps != 7:
            playsound('sounds/break.mp3', False)
            title_label.config(text='Pomodoro Break', padx=0, fg=PINK)
            window.config(padx=59)
        else:
            playsound('sounds/finish.mp3', False)
            title_label.config(text='Pomodoro Finish', padx=0, fg=PINK)
            window.config(padx=58)

        count_down()

    else:

        timer.reset()
        title_label.config(text='Pomodoro Timer', padx=0, fg=GREEN)
        window.config(padx=60)
        canvas.itemconfig(canvas_text, text='START!')
        check_mark_label.config(text='')
        start_button.config(state=tk.NORMAL)


def count_down():

    if timer.is_on:
        canvas.itemconfig(canvas_text, text=f'{timer.get_minutes()}:{timer.get_seconds()}')
        if timer.cicle > 0:
            timer.decrease_sec()
            window.after(1000, count_down)
        elif timer.reps <= 7:
            timer.change()
            start_timer()
    else:
        start_timer()


window = tk.Tk()
window.title('Pomodoro Timer')
window.config(pady=30, padx=60, bg=YELLOW)

title_label = tk.Label(text='Pomodoro Timer', fg=GREEN, font=FONT_TITLE, bg=YELLOW)
title_label.grid(row=0, column=0, pady=(0, 10), columnspan=2)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(100, 130, text='START!', font=FONT_TITLE, fill='white')
canvas.grid(row=1, column=0, columnspan=2, pady=(0, 12))

start_button = tk.Button(text='Start', relief=tk.FLAT, fg='white', font=FONT, bg=GREEN,
                         width=5, padx=2, pady=1, cursor='hand2', activebackground=GREEN, activeforeground='white',
                         borderwidth=0, highlightthickness=0, command=start_timer, disabledforeground=GRAY)
start_button.grid(row=2, column=0)

reset_button = tk.Button(text='Reset', relief=tk.FLAT, fg='white', font=FONT, bg=GREEN,
                         width=5, padx=2, pady=1, cursor='hand2', activebackground=GREEN, activeforeground='white',
                         borderwidth=0, highlightthickness=0, command=timer.stop)
reset_button.grid(row=2, column=1)

check_mark_label = tk.Label(text='', font=FONT_CHECKS, fg=GREEN, bg=YELLOW)
check_mark_label.grid(row=3, column=0, columnspan=2, pady=(12, 0))

window.mainloop()
