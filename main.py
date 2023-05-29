# needed libraries
from tkinter import *
from PIL import Image, ImageTk
from config import *
import utils


# window setup
window = Tk()
window.title('Minesweeper Game')
window.config(bg=WINDOW_BG)
window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
window.resizable(False, False)


# window header setup
header = Frame(window, bg=WINDOW_BG, width=WINDOW_WIDTH, height=utils.calculate_percentage('h', 15))
header.place(x=0, y=0)
# app logo
logo = Image.open("logo.png")
logo = logo.resize((70, 70))
logo = ImageTk.PhotoImage(logo)
# header title
header_title = Label(header, bg=WINDOW_BG, fg='#fff', text='Minesweeper Game', font=('Georgia', 20, 'bold'))
header_title.config(image=logo, compound='left')
header_title.place(relx=0.5, rely=0.5, anchor='center')


# window sidebar setup


# project running...
window.mainloop()

