from tkinter import *
import pyglet
import math


pyglet.font.add_file('Sile.ttf')
TIMER = None
BACKGROUND_COLOR = '#FFAE23'
SOFT = 5
MEDIUM = 7
HARD = 10


def start_timer():
    if select.get() == 'Soft Boiled':
        soft = SOFT * 60
        timer(soft)
    elif select.get() == 'Medium Boiled':
        medium = MEDIUM * 60
        timer(medium)
    elif select.get() == 'Hard Boiled':
        hard = HARD * 60
        timer(hard)
    else:
        pass

def timer(count):
    minutes = math.floor(count/60)
    seconds = count % 60
    if seconds < 10:
        seconds = f'0{seconds}'

    canvas.itemconfig(timer_txt, text=f'{minutes}:{seconds}')

    if count > 0:
        global TIMER
        TIMER = window.after(1000, timer, count - 1)

def reset():
    window.after_cancel(TIMER)

    canvas.itemconfig(timer_txt, text='00:00')


window = Tk()
window.title('Eggie Timer')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

egg_txt = Label(text='Pick Your Egg', bg=BACKGROUND_COLOR, fg='white', font=('Sile', 35))
egg_txt.grid(column=1, row=0, columnspan=2)

select = StringVar(window)
select.set('Select an Option')
options = OptionMenu(window, select, "Soft Boiled", "Medium Boiled", "Hard Boiled")
options.config(width=30)
options.grid(column=1, row=1, columnspan=2)

canvas = Canvas(width=400, height=400, bg=BACKGROUND_COLOR, highlightthickness=0)
gudetama = PhotoImage(file='gudetama.png')
canvas.create_image(200, 250, image=gudetama)
timer_txt = canvas.create_text(320, 100, text='00:00', fill='white', font=('Sile', 45))
time_left_txt = canvas.create_text(150, 100, text='Time Left: ', fill='white', font=('Sile', 45))
canvas.grid(column=1, row=2, columnspan=2)

start_button = Button(text='Start', width=20, height=5, highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text='Reset', width=20, height=5, highlightthickness=0, command=reset)
reset_button.grid(column=2, row=3)


window.mainloop()