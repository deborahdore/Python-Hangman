import tkMessageBox
from Tkinter import *
from Tkinter import Button
from Tkinter import Canvas
from Tkinter import Label
from string import upper

from PIL import Image
from PIL import ImageTk

game_over = False
index_image = 0
chances = 6
right = False
window = Tk()
window.withdraw()
right_answer = ""
label1 = Label()
canv = Canvas()

# hangma's images
iconPath = ['./image/hang1.jpg',
            './image/hang2.jpg',
            './image/hang3.jpg',
            './image/hang4.jpg',
            './image/hang5.jpg',
            './image/hang6.jpg',
            './image/hang7.jpg']


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))


# try a character
def tries(alphabet):
    global chances
    global index_image
    global right
    global game_over
    global canv
    global img
    global label1

    right = False
    index_right_answer = get_right_index(alphabet)
    if chances > 0 and index_image < 6:
        for elem in index_right_answer:
            if elem == 0:
                btn01["text"] = alphabet
                right = True
            elif elem == 1:
                btn02["text"] = alphabet
                right = True
            elif elem == 2:
                btn03["text"] = alphabet
                right = True
            elif elem == 3:
                btn04["text"] = alphabet
                right = True
            elif elem == 4:
                btn05["text"] = alphabet
                right = True
            elif elem == 5:
                btn06["text"] = alphabet
                right = True

    if right == False:  # if the char guessed was wrong: loose a chance
        chances -= 1
        txt = "Chances remaining: " + str(chances)
        label1.configure(text=txt)

        index_image += 1
        if index_image < len(iconPath):
            img = ImageTk.PhotoImage(Image.open(iconPath[index_image]))  # PIL solution
            canv.create_image(50, 50, anchor=NW, image=img)

    if chances <= 0:
        tkMessageBox.showinfo("Sorry!", "You failed!")
        print("GAME OVER")
        game_over = True

    if btn01["text"] == right_answer[0] and btn02["text"] == right_answer[1] and btn03["text"] == right_answer[2] and \
            btn04["text"] == right_answer[3] and btn05["text"] == right_answer[4] and btn06["text"] == right_answer[5]:
        tkMessageBox.showinfo("Congratulations!", "You have won the game!")
        print("GAME OVER")
        game_over = True

    if game_over == True:
        quit_game()


# get the index of character tried (if char tried is correct)
def get_right_index(alphabet):
    res = [-1, -1, -1, -1, -1, -1]
    x = 0
    for y in right_answer:
        if y == alphabet:
            res[x] = x
        x += 1
    return res


# quit the game if won or lost
def quit_game():
    global window
    window.destroy()


btn01 = Button(window, text=" ", highlightbackground="aquamarine", foreground="Black", width=3, height=1,
               font=('Helvetica', '20'))
btn01.grid(column=3, row=2)
btn02 = Button(window, text=" ", highlightbackground="aquamarine", foreground="Black", width=3, height=1,
               font=('Helvetica', '20'))
btn02.grid(column=4, row=2)
btn03 = Button(window, text=" ", highlightbackground="aquamarine", foreground="Black", width=3, height=1,
               font=('Helvetica', '20'))
btn03.grid(column=5, row=2)
btn04 = Button(window, text=" ", highlightbackground="aquamarine", foreground="Black", width=3, height=1,
               font=('Helvetica', '20'))
btn04.grid(column=6, row=2)
btn05 = Button(window, text=" ", highlightbackground="aquamarine", foreground="Black", width=3, height=1,
               font=('Helvetica', '20'))
btn05.grid(column=7, row=2)
btn06 = Button(window, text=" ", highlightbackground="aquamarine", foreground="Black", width=3, height=1,
               font=('Helvetica', '20'))
btn06.grid(column=8, row=2)

btn1 = Button(window, text="Q", highlightbackground="skyBlue", foreground="Black", width=3, height=1,
              font=('Helvetica', '20'), command=lambda: tries("Q"))
btn1.grid(column=1, row=5)
btn2 = Button(window, text="W", highlightbackground="skyBlue", foreground="Black", width=3, height=1,
              font=('Helvetica', '20'), command=lambda: tries("W"))
btn2.grid(column=2, row=5)
btn3 = Button(window, text="E", highlightbackground="skyBlue", foreground="Black", width=3, height=1,
              font=('Helvetica', '20'), command=lambda: tries("E"))
btn3.grid(column=3, row=5)
btn4 = Button(window, text="R", highlightbackground="skyBlue", foreground="Black", width=3, height=1,
              font=('Helvetica', '20'), command=lambda: tries("R"))
btn4.grid(column=4, row=5)
btn5 = Button(window, text="T", highlightbackground="skyBlue", foreground="Black", width=3, height=1,
              font=('Helvetica', '20'), command=lambda: tries("T"))
btn5.grid(column=5, row=5)
btn6 = Button(window, text="Y", highlightbackground="skyBlue", foreground="Black", width=3, height=1,
              font=('Helvetica', '20'), command=lambda: tries("Y"))
btn6.grid(column=6, row=5)
btn7 = Button(window, text="U", highlightbackground="skyBlue", foreground="Black", width=3, height=1,
              font=('Helvetica', '20'), command=lambda: tries("U"))
btn7.grid(column=7, row=5)
btn8 = Button(window, text="I", highlightbackground="skyBlue", foreground="Black", width=3, height=1,
              font=('Helvetica', '20'), command=lambda: tries("I"))
btn8.grid(column=8, row=5)
btn9 = Button(window, text="O", highlightbackground="skyBlue", foreground="Black", width=3, height=1,
              font=('Helvetica', '20'), command=lambda: tries("O"))
btn9.grid(column=9, row=5)
btn10 = Button(window, text="P", highlightbackground="skyBlue", foreground="Black", width=3, height=1,
               font=('Helvetica', '20'), command=lambda: tries("P"))
btn10.grid(column=10, row=5)

btn11 = Button(window, text="A", highlightbackground="skyBlue", foreground="Black", width=3, height=1,
               font=('Helvetica', '20'), command=lambda: tries("A"))
btn11.grid(column=2, row=6)
btn12 = Button(window, text="S", highlightbackground="skyBlue", foreground="Black", width=3, height=1,
               font=('Helvetica', '20'), command=lambda: tries("S"))
btn12.grid(column=3, row=6)
btn13 = Button(window, text="D", highlightbackground="skyBlue", foreground="Black", width=3, height=1,
               font=('Helvetica', '20'), command=lambda: tries("D"))
btn13.grid(column=4, row=6)
btn14 = Button(window, text="F", highlightbackground="skyBlue", foreground="Black", width=3, height=1,
               font=('Helvetica', '20'), command=lambda: tries("F"))
btn14.grid(column=5, row=6)
btn15 = Button(window, text="G", highlightbackground="skyBlue", foreground="Black", width=3, height=1,
               font=('Helvetica', '20'), command=lambda: tries("G"))
btn15.grid(column=6, row=6)
btn16 = Button(window, text="H", highlightbackground="skyBlue", foreground="Black", width=3, height=1,
               font=('Helvetica', '20'), command=lambda: tries("H"))
btn16.grid(column=7, row=6)
btn17 = Button(window, text="J", highlightbackground="skyBlue", foreground="Black", width=3, height=1,
               font=('Helvetica', '20'), command=lambda: tries("J"))
btn17.grid(column=8, row=6)
btn18 = Button(window, text="K", highlightbackground="skyBlue", foreground="Black", width=3, height=1,
               font=('Helvetica', '20'), command=lambda: tries("K"))
btn18.grid(column=9, row=6)

btn19 = Button(window, text="L", highlightbackground="skyBlue", foreground="Black", width=3, height=1,
               font=('Helvetica', '20'), command=lambda: tries("L"))
btn19.grid(column=3, row=7)
btn20 = Button(window, text="Z", highlightbackground="skyBlue", foreground="Black", width=3, height=1,
               font=('Helvetica', '20'), command=lambda: tries("Z"))
btn20.grid(column=4, row=7)
btn21 = Button(window, text="X", highlightbackground="skyBlue", foreground="Black", width=3, height=1,
               font=('Helvetica', '20'), command=lambda: tries("X"))
btn21.grid(column=5, row=7)
btn22 = Button(window, text="C", highlightbackground="skyBlue", foreground="Black", width=3, height=1,
               font=('Helvetica', '20'), command=lambda: tries("C"))
btn22.grid(column=6, row=7)
btn23 = Button(window, text="V", highlightbackground="skyBlue", foreground="Black", width=3, height=1,
               font=('Helvetica', '20'), command=lambda: tries("V"))
btn23.grid(column=7, row=7)
btn24 = Button(window, text="B", highlightbackground="skyBlue", foreground="Black", width=3, height=1,
               font=('Helvetica', '20'), command=lambda: tries("B"))
btn24.grid(column=8, row=7)

btn25 = Button(window, text="N", highlightbackground="skyBlue", foreground="Black", width=3, height=1,
               font=('Helvetica', '20'), command=lambda: tries("N"))
btn25.grid(column=5, row=8)
btn26 = Button(window, text="M", highlightbackground="skyBlue", foreground="Black", width=3, height=1,
               font=('Helvetica', '20'), command=lambda: tries("M"))
btn26.grid(column=6, row=8)


def play(word):
    global right_answer
    global label1
    global canv
    global window

    right_answer = upper(word)
    window.deiconify()

    # create the window
    window.title("Ready to play Hangman?")
    window.geometry("900x700")
    center(window)

    label1 = Label(window, text="Total Chances are : 6")
    label1.grid(column=0, row=20)

    canv = Canvas(window, width=250, height=250, highlightbackground='white')
    canv.grid(row=0, column=0)

    img = ImageTk.PhotoImage(Image.open(iconPath[0]))  # PIL solution
    canv.create_image(50, 50, anchor=NW, image=img)
    window.mainloop()
