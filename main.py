# needed libraries
from tkinter import *
from config import *

# window setup
window = Tk()
window.title('Minesweeper Game')
window.config(bg='#ECF2FF')
window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
window.resizable(False, False)


# project running...
window.mainloop()

