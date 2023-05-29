from config import *
import tkinter


# a utility function to calculate the percentage
# d_name: dimension name-> w=>width, h=>height
def calculate_percentage(d_name, percentage):
    return (WINDOW_WIDTH / 100) * percentage if d_name == 'w' else (WINDOW_HEIGHT / 100) * percentage

