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

        # This is to make a frame for the title/introduction and to add this frame to my list of pages
        start_frame = Frame(window, highlightbackground="black", highlightthickness=4,
                            height=450,
                            width=800)
        start_frame.pack()
        self.pages.append(start_frame)

        # This is my OSC Logo
        Label(start_frame, image=self.logo).grid(row=0, column=0, columnspan=2, padx=30, sticky=W)

        # This is my turquoise background with the Interface title
        Frame(start_frame, background="#5bc5da",
              width=800*0.837056505,
              height=450*0.25,
              highlightbackground="#595959",
              highlightthickness=3).grid(row=1, columnspan=4, column=0)
        Label(start_frame, text="OSC's Cafe Kiosk", font=("Verdana", 32), background="#5bc5da")\
            .grid(row=1, column=0, columnspan=4)

        # This is my brown background with the "proceed" button
        Frame(start_frame, background="#775b59",
              width=800*0.837056505,
              height=450*0.344262295,
              highlightbackground="#595959",
              highlightthickness=3).grid(row=2, columnspan=4, column=0)
        Button(start_frame, text="Proceed", command=self.next_frame).grid(row=2, column=1)

        # The following will be my menu page

        # This is my menu frame where the users can pick their orders
        menu_frame = Frame(window, highlightbackground="black", highlightthickness=4)
        self.pages.append(menu_frame)
        self.small_logo = ImageTk.PhotoImage(Image.open(current_dir / "OSC logo.png").resize((800 // 4, 800 // 4 // 4)))

        # This is my OSC Logo
        Label(menu_frame, image=self.small_logo).grid(row=0, column=1, columnspan=2)

        # This is the GUI title
        Label(menu_frame, text="OSC's Cafe Kiosk", font=("Verdana", 22))\
            .grid(row=0, column=0, columnspan=2)

        # This is my page title
        title_frame = Frame(menu_frame,
                            background="#5bc5da",
                            width=800*0.958,
                            height=450*0.25,
                            highlightbackground="#595959",
                            highlightthickness=3)
        title_frame.grid(row=1, column=0, columnspan=3)
        Label(menu_frame,
              text="Menu",
              font=("Verdana", 32),
              background="#5bc5da").grid(row=1, column=0, columnspan=3)

        background_frame = Frame(menu_frame,
                                 background="#775b59",
                                 width=800 * 0.958,
                                 height=450 * 0.4,
                                 highlightbackground="#595959",
                                 highlightthickness=3)
        background_frame.grid(row=2, rowspan=2, column=0, columnspan=3, sticky=N)
        background_frame.grid_propagate(False)
        background_frame.pack_propagate(False)
        Frame(background_frame,
              background="#eeeeee",
              width=50,
              height=50).grid(row=0, column=0)

        Button(background_frame, text="Confirm", command=self.next_frame).grid(row=4, column=1, sticky=SE)
        Button(background_frame, text="Cancel", command=self.prev_frame).grid(row=4, column=0, sticky=SW)

        # The following is my order confirmation page

        order_confirmation_frame = Frame(window, highlightbackground="black", highlightthickness=4)
        self.pages.append(order_confirmation_frame)
        self.small_logo = ImageTk.PhotoImage(Image.open(current_dir / "OSC logo.png")
                                             .resize((800 // 4, 800 // 4 // 4)))

        # This is my OSC Logo
        Label(order_confirmation_frame, image=self.small_logo).grid(row=0, column=1, columnspan=2)

        # This is the GUI title
        Label(order_confirmation_frame, text="OSC's Cafe Kiosk", font=("Verdana", 22)) \
            .grid(row=0, column=0, columnspan=2)

        # This is my page title
        title_frame = Frame(order_confirmation_frame,
                            background="#5bc5da",
                            width=800 * 0.958,
                            height=450 * 0.25,
                            highlightbackground="#595959",
                            highlightthickness=3)
        title_frame.grid(row=1, column=0, columnspan=3)
        Label(order_confirmation_frame,
              text="Order Confirmation | Amount of items: 5",
              font=("Verdana", 20),
              background="#5bc5da").grid(row=1, column=0, columnspan=3)

        # This is my brown background
        background_frame = Frame(order_confirmation_frame,
                                 background="#775b59",
                                 width=800 * 0.958,
                                 height=450 * 0.4,
                                 highlightbackground="#595959",
                                 highlightthickness=3)
        background_frame.grid(row=2, rowspan=2, column=0, columnspan=3, sticky=N)
        background_frame.grid_propagate(False)
        background_frame.pack_propagate(False)

        # This is the frame which will contain all the extra details
        Frame(background_frame,
              background="#eeeeee").grid(row=0, column=0)

        # Don't go past this bad boi
        for i in range(3):
            start_frame.grid_columnconfigure(i, minsize=800//3)
            menu_frame.grid_columnconfigure(i, minsize=800//3)
            order_confirmation_frame.grid_columnconfigure(i, minsize=800//3)
            background_frame.grid_columnconfigure(i, minsize=800 * 0.958 * 0.25)

        for i in range(4):
            start_frame.grid_rowconfigure(i, minsize=450//4)
            menu_frame.grid_rowconfigure(i, minsize=450//4)
            order_confirmation_frame.grid_rowconfigure(i, minsize=450//4)
            background_frame.grid_rowconfigure(i, minsize=450 * 0.958 * 0.25)

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
