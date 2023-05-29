# needed libraries
from tkinter import *
from PIL import Image, ImageTk
from utils import *


# window setup
window = Tk()
window.title('Minesweeper Game')
window.config(bg=WINDOW_BG)
window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
window.resizable(False, False)
window.config(cursor="hand2")


# window header setup
header = Frame(window, bg=WINDOW_BG, width=WINDOW_WIDTH, height=calculate_percentage('h', 15))
header.place(x=0, y=0)
# app logo
logo = Image.open("logo.png")
logo = logo.resize((70, 70))
logo = ImageTk.PhotoImage(logo)
# header title
header_title = Label(header, bg=WINDOW_BG, fg='#fff', text='Minesweeper Game', font=('Georgia', 20, 'bold'))
header_title.config(image=logo, compound='left')
header_title.place(relx=0.5, rely=0.5, anchor='center')


# window main setup
def start_game():
    startButton.config(state=DISABLED)
    endButton.config(state=NORMAL)
    # this part will be updated...
    print('Game started!')


def end_game():
    startButton.config(state=NORMAL)
    endButton.config(state=DISABLED)
    # this part will be updated...
    print('Game end!')


# window sidebar setup
sidebar = Frame(window, bg=WINDOW_BG, width=calculate_percentage('w', 25), height=calculate_percentage('h', 80))
sidebar.place(x=0, y=calculate_percentage('h', 20))
# start game btn
startButton = Button(sidebar, text='Start Game', bg='#539165', fg='#fff', width=17, height=1)
startButton.config(font=('Arial', 12, 'bold'), command=start_game)
startButton.grid(row=0, column=0, pady=5, padx=5)
# end game btn
endButton = Button(sidebar, text='End Game', bg='#F96666', fg='#fff', width=17, height=1)
endButton.config(font=('Arial', 12, 'bold'), command=end_game, state=DISABLED)
endButton.grid(row=1, column=0, pady=5, padx=5)


# project running...
window.mainloop()

