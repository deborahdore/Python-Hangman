import random
from Tkinter import *
from Tkinter import Button
from Tkinter import Canvas
from Tkinter import Label

from src.hangman_play import play, center

entry = Entry()
window_choose = Tk()
window_word = Tk()
window_word.withdraw()




# Choose a random word
def get_random_word():
    with open('./word_list.csv', 'r') as text:  # open the file in reading mode
        rand_num = random.randrange(0, 99)
        data = text.readlines()
        word = data[rand_num]
        return word


def destr(win):
    win.destroy()


def single_mode_funct():
    global window_choose
    random_answer = get_random_word()
    destr(window_choose)
    play(random_answer)


def get_entry():
    global entry
    global window_word
    result = entry.get()
    if len(result) == 6:
        window_word.destroy()
        play(str(result))


def multiplayer_funct():
    global window_choose
    global entry
    global window_word
    destr(window_choose)
    window_word.deiconify()
    window_word.title("Choose a word")
    center(window_word)

    canvas_word = Canvas(window_word, height=600, width=600, highlightbackground='green')
    canvas_word.pack(fill=BOTH, expand=YES)

    Label(canvas_word, text="Insert a word of 6 letters").grid(row=1, column=0)

    entry = Entry(canvas_word)
    entry.grid(row=2, column=0)

    btn_word = Button(canvas_word, text="Submit", command=get_entry)
    btn_word.grid(row=3, column=0)

    window_word.mainloop()


if __name__ == '__main__':
    window_choose.title("Ready to play hangman? Choose a modality!")

    window_choose.geometry("512x255")
    center(window_choose)
    canv_s = Canvas(window_choose, width=250, height=250, highlightbackground='blue')
    canv_s.grid(row=0, column=0)

    canv_m = Canvas(window_choose, width=250, height=250, highlightbackground='red')
    canv_m.grid(row=0, column=1)

    single_mode = Button(window_choose, text='single mode against computer', activebackground='yellow',
                         command=single_mode_funct)
    single_mode.grid(row=0, column=0)

    multiplayer = Button(window_choose, text='multiplayer', activebackground='yellow', command=multiplayer_funct)
    multiplayer.grid(row=0, column=1)
    window_choose.mainloop()
