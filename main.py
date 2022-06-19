from tkinter import *
from pathlib import Path
from PIL import Image, ImageTk


# This program will help café managers track students orders in an interface that allows students and staff of OSC to
# order in

# The following class is going to be the actual interface that the users will see


class Interface:
    def __init__(self, window):

        # My colour constants
        BLUE = "#5bc5da"
        BROWN = "#775b59"
        GREEN = "#a6d3a0ff"
        DARK_MAGENTA = "#595959"
        LIGHT_GRAY = "#eeeeee"

        # The following are variables to set different values and create different lists for my code to access
        current_dir = Path(__file__).absolute().parent
        self.pages = []
        self.current_page = 0
        self.logo = ImageTk.PhotoImage(Image.open(current_dir / "OSC logo.png").resize((800//3, 800//3//4)))
        self.small_logo = ImageTk.PhotoImage(Image.open(current_dir / "OSC logo.png").resize((800 // 4, 800 // 4 // 4)))
        self.quantity_of_order = 0

        # This is to make a frame for the title/introduction and to add this frame to my list of pages
        start_frame = Frame(window)
        start_frame.pack()
        self.pages.append(start_frame)

        # This is my OSC Logo
        Label(start_frame, image=self.logo).grid(row=0, column=0, pady=(30, 20))

        # This is my turquoise background with the Interface title
        title_frame = Frame(start_frame, bg=BLUE,
                            width=700,
                            height=100,
                            highlightbackground=DARK_MAGENTA,
                            highlightthickness=3)
        title_frame.grid(row=1, columnspan=4, column=0)
        title_frame.pack_propagate(False)
        Label(title_frame, text="OSC's Cafe Kiosk", font=("Verdana", 32), bg=BLUE).pack(pady=(20, 0))

        # This is my brown background with the "proceed" button
        proceed_frame = Frame(start_frame, bg=BROWN,
                              width=700,
                              height=150,
                              highlightbackground=DARK_MAGENTA,
                              highlightthickness=3)
        proceed_frame.grid(row=2, columnspan=4, column=0)
        proceed_frame.grid_propagate(False)
        Button(proceed_frame, text="Proceed", command=self.next_frame).grid(row=0, column=0)

        # The following will be my menu page

        # This is my menu frame where the users can pick their orders
        menu_frame = Frame(window)
        self.pages.append(menu_frame)

        # This is the GUI title
        Label(menu_frame, text="OSC's Cafe Kiosk", font=("Verdana", 22))\
            .grid(row=0, column=0, columnspan=2, pady=20)

        # This is my OSC Logo
        Label(menu_frame, image=self.small_logo).grid(row=0, column=1, columnspan=2, pady=20)

        # This is my page title
        title_frame = Frame(menu_frame,
                            background="#5bc5da",
                            width=750,
                            height=75,
                            highlightbackground="#595959",
                            highlightthickness=3)
        title_frame.grid(row=1, column=0, columnspan=3)
        title_frame.pack_propagate(False)
        Label(title_frame,
              text="Menu",
              font=("Verdana", 32),
              background="#5bc5da").pack(pady=(6, 0))

        background_frame = Frame(menu_frame,
                                 background="#775b59",
                                 width=750,
                                 height=255,
                                 highlightbackground="#595959",
                                 highlightthickness=3)
        background_frame.grid(row=2, column=0, columnspan=3, sticky=N)
        background_frame.pack_propagate(False)

        item_frame = Frame(background_frame, width=730, height=235)
        item_frame.pack(pady=10)
        item_frame.pack_propagate(False)

        item_no_one = Frame(item_frame,
                            background=LIGHT_GRAY,
                            width=100,
                            height=100)
        item_no_one.grid(row=0, column=0, sticky=W)
        item_no_one.pack_propagate(False)
        Label(item_no_one, text="Hello").pack()

        Label(item_frame, text="Hllo").grid(row=0, column=1)

        item_no_two = Frame(item_frame,
                            background=LIGHT_GRAY,
                            width=100,
                            height=10)
        item_no_two.grid(row=0, column=2, sticky=E)
        item_no_two.pack_propagate(False)
        Label(item_no_two, text="Other Hello").pack()

        Button(menu_frame, text="Confirm", command=self.next_frame).grid(row=4, column=2, sticky=SE)
        Button(menu_frame, text="Cancel", command=self.prev_frame).grid(row=4, column=0, sticky=SW)

        # The following is my order confirmation page

        # This is my order confirmation frame where the users will confirm their order and can edit what they want to
        menu_frame = Frame(window)
        self.pages.append(menu_frame)

        # This is the GUI title
        Label(menu_frame, text="OSC's Cafe Kiosk", font=("Verdana", 22)) \
            .grid(row=0, column=0, columnspan=2, pady=20)

        # This is my OSC Logo
        Label(menu_frame, image=self.small_logo).grid(row=0, column=1, columnspan=2, pady=20)

        # This is my page title
        title_frame = Frame(menu_frame,
                            background="#5bc5da",
                            width=750,
                            height=75,
                            highlightbackground="#595959",
                            highlightthickness=3)
        title_frame.grid(row=1, column=0, columnspan=3)
        title_frame.pack_propagate(False)
        Label(title_frame,
              text=f"Order Confirmation | Amount of items: {self.quantity_of_order}",
              font=("Verdana", 32),
              background="#5bc5da").pack(pady=(6, 0))

        background_frame = Frame(menu_frame,
                                 background="#775b59",
                                 width=750,
                                 height=255,
                                 highlightbackground="#595959",
                                 highlightthickness=3)
        background_frame.grid(row=2, column=0, columnspan=3, sticky=N)
        background_frame.pack_propagate(False)

        item_frame = Frame(background_frame, width=730, height=235)
        item_frame.pack(pady=10)
        item_frame.pack_propagate(False)

        item_no_one = Frame(item_frame,
                            background=LIGHT_GRAY,
                            width=300,
                            height=100)
        item_no_one.grid(row=0, column=0, sticky=W)
        Label(item_no_one, text="Hello")

        item_no_two = Frame(item_frame,
                            background=LIGHT_GRAY,
                            width=300,
                            height=10)
        item_no_two.grid(row=0, column=1, sticky=E)

        Button(menu_frame, text="Confirm", command=self.next_frame).grid(row=4, column=2, sticky=SE)
        Button(menu_frame, text="Menu", command=self.prev_frame).grid(row=4, column=0, sticky=SW)

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

    def add_order(self):
        self.quantity_of_order += 1

    def remove_order(self):
        self.quantity_of_order = 0


root = Tk()
root.geometry("801x452")
cafe_kiosk = Interface(root)
root.mainloop()
