from tkinter import *
from pathlib import Path
from PIL import Image, ImageTk


# This program will help café managers track students orders in an interface that allows students and staff of OSC to
# order in

# The following class is going to be the actual interface that the users will see


class Interface:
    def __init__(self, window):
        self.pages = []
        self.current_page = 0

        current_dir = Path(__file__).absolute().parent
        self.logo = ImageTk.PhotoImage(Image.open(current_dir / "OSC logo.png").resize((800//3, 800//3//4)))

        start_frame = Frame(window)
        start_frame.pack()
        self.pages.append(start_frame)

        Frame(start_frame, background="#5bc5da", width=800*0.837056505, height=450*0.25)\
            .grid(row=1, columnspan=4, column=0)
        Label(start_frame, text="OSC's Cafe Kiosk", font=("Verdana", 32), background="#5bc5da")\
            .grid(row=1, column=0, columnspan=4)

        Frame(start_frame, background="#775b59", width=800*0.837056505, height=450*0.344262295)\
            .grid(row=2, columnspan=4, column=0)
        menu_next = Button(start_frame, text="Proceed", command=self.next_frame)
        menu_next.grid(row=2, column=1)

        Label(start_frame, image=self.logo).grid(row=0, column=0)

        menu_frame = Frame(window)
        self.pages.append(menu_frame)

        for i in range(3):
            menu_frame.grid_columnconfigure(i, minsize=800/3)

        for i in range(4):
            menu_frame.grid_rowconfigure(i, minsize=450/4)

        Label(menu_frame, text="OSC's Cafe Kiosk", font=("Verdana", 32), pady=45).grid(row=0, column=0)

        Label(menu_frame, image=self.logo).grid(row=0, column=2, sticky=W)

        # Don't go past this bad boi
        for i in range(3):
            start_frame.grid_columnconfigure(i, minsize=800/3)
            menu_frame.grid_columnconfigure(i, minsize=800/3)

        for i in range(4):
            start_frame.grid_rowconfigure(i, minsize=450/4)
            menu_frame.grid_rowconfigure(i, minsize=450/4)


    def update_current_page(self):
        for page in self.pages:
            page.pack_forget()
        self.pages[self.current_page].pack()

    def next_frame(self):
        self.current_page += 1
        self.update_current_page()

    def prev_frame(self):
        self.current_page -= 1
        self.update_current_page()


root = Tk()
root.geometry("800x450")
cafe_kiosk = Interface(root)
root.mainloop()
