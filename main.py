from tkinter import *
from PIL import Image
from PIL import ImageTk

# This program will help cafe managers track students orders in an interface that allows students and staff of OSC to
# order in

# The following class is going to be the actual interface that the users will see


class Interface:
    def __init__(self, window):
        start_frame = Frame(window)
        canvas = Canvas(start_frame, width=400, height=200)
        canvas.pack()
        img = ImageTk.PhotoImage(Image.open('OSC logo.png'))
        canvas.create_image(10, 10, anchor=NW, image=img)

        menu_frame = Frame(window)
        

root = Tk()
root.geometry("800x450")
cafe_kiosk = Interface(root)
root.mainloop()
