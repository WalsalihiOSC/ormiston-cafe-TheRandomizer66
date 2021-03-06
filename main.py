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
        GREEN = "#a6d3a0"
        DARK_MAGENTA = "#32161f"
        DARK_GRAY = "#595959"
        LIGHT_GRAY = "#eeeeee"
        RED = "#e32a2a"

        # The following are variables to set different values and create different lists for my code to access
        current_dir = Path(__file__).absolute().parent
        self.pages = []
        self.current_page = 0
        self.logo = ImageTk.PhotoImage(Image.open(current_dir / "OSC logo.png").resize((800//3, 800//3//4)))
        self.small_logo = ImageTk.PhotoImage(Image.open(current_dir / "OSC logo.png").resize((800 // 4, 800 // 4 // 4)))
        self.quantity_of_order = 0
        self.sandwich_chicken_num = 0
        self.sandwich_pork_num = 0
        self.sandwich_beef_num = 0
        self.sandwich_vege_num = 0
        self.salad_chicken_num = 0
        self.salad_beef_num = 0
        self.salad_potato_num = 0
        self.salad_vege_num = 0
        self.drink_water_num = 0
        self.drink_coke_num = 0
        self.drink_juice_num = 0
        self.drink_coffee_num = 0
        self.wrap_chicken_num = 0
        self.wrap_pork_num = 0
        self.wrap_beef_num = 0
        self.wrap_vege_num = 0

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
                            highlightbackground=DARK_GRAY,
                            highlightthickness=3)
        title_frame.grid(row=1, columnspan=4, column=0)
        title_frame.pack_propagate(False)
        Label(title_frame, text="OSC's Cafe Kiosk", font=("Verdana", 32), bg=BLUE).pack(pady=(20, 0))

        # This is my brown background with the "proceed" button
        proceed_frame = Frame(start_frame, bg=BROWN,
                              width=700,
                              height=150,
                              highlightbackground=DARK_GRAY,
                              highlightthickness=3)
        proceed_frame.grid(row=2, columnspan=4, column=0)
        proceed_frame.grid_propagate(False)
        Button(proceed_frame, text="Proceed", bg=GREEN, command=self.next_frame)\
            .grid(row=0, column=0, padx=310, pady=50)

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
                            highlightbackground=DARK_GRAY,
                            highlightthickness=3)
        title_frame.grid(row=1, column=0, columnspan=3)
        title_frame.pack_propagate(False)
        Label(title_frame,
              text="Menu",
              font=("Verdana", 32),
              background=BLUE).pack(pady=(6, 0))

        background_frame = Frame(menu_frame,
                                 background=BROWN,
                                 width=750,
                                 height=255,
                                 highlightbackground=DARK_GRAY,
                                 highlightthickness=3)
        background_frame.grid(row=2, column=0, columnspan=3, sticky=N)
        background_frame.pack_propagate(False)
        background_frame.grid_columnconfigure(0, minsize=730//2)
        background_frame.grid_columnconfigure(1, minsize=730//2)

        # This is my frame that will have all the content
        item_frame = Frame(background_frame, width=730, height=235, bg=LIGHT_GRAY)
        item_frame.pack(pady=10)
        item_frame.grid_propagate(False)
        item_frame.grid_rowconfigure(0, minsize=235//2)
        item_frame.grid_rowconfigure(1, minsize=235//2)
        item_frame.grid_columnconfigure(0, minsize=730//2)
        item_frame.grid_columnconfigure(1, minsize=730//2)

        self.order_categories = Frame(item_frame,
                                      background=DARK_MAGENTA,
                                      width=730,
                                      height=235//4)
        self.order_categories.grid(row=0, column=0, columnspan=2, sticky=N)
        for i in range(4):
            self.order_categories.grid_columnconfigure(i, minsize=730//4)
        self.order_categories.grid_rowconfigure(0, minsize=50)
        self.order_categories.grid_propagate(False)

        Button(self.order_categories, text="Sandwiches", command=lambda: self.change_menu(1)).grid(row=0, column=0)
        Button(self.order_categories, text="Salads", command=lambda: self.change_menu(2)).grid(row=0, column=1)
        Button(self.order_categories, text="Drinks", command=lambda: self.change_menu(3)).grid(row=0, column=2)
        Button(self.order_categories, text="Wraps", command=lambda: self.change_menu(4)).grid(row=0, column=3)

        # Sandwich Frame
        sandwich_frame = Frame(background_frame, width=730, height=235, bg=LIGHT_GRAY)
        sandwich_frame.grid_propagate(False)
        for i in range(4):
            sandwich_frame.grid_columnconfigure(i, minsize=730//4)

        self.order_categories = Frame(sandwich_frame,
                                      background=DARK_MAGENTA,
                                      width=730,
                                      height=235//4)
        self.order_categories.grid(row=0, column=0, columnspan=4, sticky=N)
        for i in range(4):
            self.order_categories.grid_columnconfigure(i, minsize=730//4)
        self.order_categories.grid_rowconfigure(0, minsize=50)
        self.order_categories.grid_propagate(False)

        Button(self.order_categories, text="Sandwiches", command=lambda: self.change_menu(1)).grid(row=0, column=0)
        Button(self.order_categories, text="Salads", command=lambda: self.change_menu(2)).grid(row=0, column=1)
        Button(self.order_categories, text="Drinks", command=lambda: self.change_menu(3)).grid(row=0, column=2)
        Button(self.order_categories, text="Wraps", command=lambda: self.change_menu(4)).grid(row=0, column=3)
        Label(sandwich_frame, text=f"Chicken\n{self.sandwich_chicken_num}\nPrice for 1: $3.00")\
            .grid(row=1, column=0, sticky=E)
        Button(sandwich_frame, text="+", command=self.sandwich_chicken_num)\
            .grid(row=1, column=1, sticky=W, padx=(30, 0))
        Button(sandwich_frame, text="-", command=self.reduce_order).grid(row=1, column=1, sticky=W)

        Label(sandwich_frame, text=f"Pork\n{self.sandwich_chicken_num}\nPrice for 1: $3.50") \
            .grid(row=2, column=0, sticky=E)
        Button(sandwich_frame, text="+", command=self.add_order).grid(row=2, column=1, sticky=W, padx=(30, 0))
        Button(sandwich_frame, text="-", command=self.reduce_order).grid(row=2, column=1, sticky=W)

        Label(sandwich_frame, text=f"Beef\n{self.sandwich_chicken_num}\nPrice for 1: $3.50") \
            .grid(row=1, column=2, sticky=E)
        Button(sandwich_frame, text="+", command=self.add_order).grid(row=1, column=3, sticky=W, padx=(30, 0))
        Button(sandwich_frame, text="-", command=self.reduce_order).grid(row=1, column=3, sticky=W)

        Label(sandwich_frame, text=f"Vegetarian\n{self.sandwich_chicken_num}\nPrice for 1: $3.00") \
            .grid(row=2, column=2, sticky=E)
        Button(sandwich_frame, text="+", command=self.add_order).grid(row=2, column=3, sticky=W, padx=(30, 0))
        Button(sandwich_frame, text="-", command=self.reduce_order).grid(row=2, column=3, sticky=W)

        # Salad Frame
        salads_frame = Frame(background_frame, width=730, height=235, bg=LIGHT_GRAY)
        salads_frame.grid_propagate(False)
        salads_frame.grid_columnconfigure(0, minsize=730 // 2)
        salads_frame.grid_columnconfigure(1, minsize=730 // 2)
        self.order_categories = Frame(salads_frame,
                                      background=DARK_MAGENTA,
                                      width=730,
                                      height=235 // 4)
        self.order_categories.grid(row=0, column=0, columnspan=2, sticky=N)
        for i in range(4):
            self.order_categories.grid_columnconfigure(i, minsize=730//4)
        self.order_categories.grid_rowconfigure(0, minsize=50)
        self.order_categories.grid_propagate(False)
        Button(self.order_categories, text="Sandwiches", command=lambda: self.change_menu(1)).grid(row=0, column=0)
        Button(self.order_categories, text="Salads", command=lambda: self.change_menu(2)).grid(row=0, column=1)
        Button(self.order_categories, text="Drinks", command=lambda: self.change_menu(3)).grid(row=0, column=2)
        Button(self.order_categories, text="Wraps", command=lambda: self.change_menu(4)).grid(row=0, column=3)
        Label(salads_frame, text="Hopefully", bg=RED).grid(row=1, column=0)

        # Drinks Frame
        drinks_frame = Frame(background_frame, width=730, height=235, bg=LIGHT_GRAY)
        drinks_frame.grid_propagate(False)
        drinks_frame.grid_columnconfigure(0, minsize=730 // 2)
        drinks_frame.grid_columnconfigure(1, minsize=730 // 2)
        self.order_categories = Frame(drinks_frame,
                                      background=DARK_MAGENTA,
                                      width=730,
                                      height=235 // 4)
        self.order_categories.grid(row=0, column=0, columnspan=2, sticky=N)
        for i in range(4):
            self.order_categories.grid_columnconfigure(i, minsize=730//4)
        self.order_categories.grid_rowconfigure(0, minsize=50)
        self.order_categories.grid_propagate(False)
        Button(self.order_categories, text="Sandwiches", command=lambda: self.change_menu(1)).grid(row=0, column=0)
        Button(self.order_categories, text="Salads", command=lambda: self.change_menu(2)).grid(row=0, column=1)
        Button(self.order_categories, text="Drinks", command=lambda: self.change_menu(3)).grid(row=0, column=2)
        Button(self.order_categories, text="Wraps", command=lambda: self.change_menu(4)).grid(row=0, column=3)
        Label(drinks_frame, text="Please", bg=RED).grid(row=1, column=0)

        # Wraps Frame
        wraps_frame = Frame(background_frame, width=730, height=235, bg=LIGHT_GRAY)
        wraps_frame.grid_propagate(False)
        wraps_frame.grid_columnconfigure(0, minsize=730 // 2)
        wraps_frame.grid_columnconfigure(1, minsize=730 // 2)
        self.order_categories = Frame(wraps_frame,
                                      background=DARK_MAGENTA,
                                      width=730,
                                      height=235 // 4)
        self.order_categories.grid(row=0, column=0, columnspan=2, sticky=N)
        for i in range(4):
            self.order_categories.grid_columnconfigure(i, minsize=730//4)
        self.order_categories.grid_rowconfigure(0, minsize=50)
        self.order_categories.grid_propagate(False)
        Button(self.order_categories, text="Sandwiches", command=lambda: self.change_menu(1)).grid(row=0, column=0)
        Button(self.order_categories, text="Salads", command=lambda: self.change_menu(2)).grid(row=0, column=1)
        Button(self.order_categories, text="Drinks", command=lambda: self.change_menu(3)).grid(row=0, column=2)
        Button(self.order_categories, text="Wraps", command=lambda: self.change_menu(4)).grid(row=0, column=3)
        Label(wraps_frame, text="I'm gonna cry", bg=RED).grid(row=1, column=0)

        self.menu_screens = [item_frame, sandwich_frame, salads_frame, drinks_frame, wraps_frame]

        Button(menu_frame, text="Confirm", bg=GREEN, command=self.next_frame).grid(row=4, column=2, sticky=SE)
        Button(menu_frame, text="Cancel", bg=RED, command=self.prev_frame).grid(row=4, column=0, sticky=SW)

        # The following is my order confirmation page

        # This is my order confirmation frame where the users will confirm their order and can edit what they want to
        order_confirmation_frame = Frame(window)
        self.pages.append(order_confirmation_frame)

        # This is the GUI title
        Label(order_confirmation_frame, text="OSC's Cafe Kiosk", font=("Verdana", 22)) \
            .grid(row=0, column=0, columnspan=2, pady=20)

        # This is my OSC Logo
        Label(order_confirmation_frame, image=self.small_logo).grid(row=0, column=1, columnspan=2, pady=20)

        # This is my page title
        title_frame = Frame(order_confirmation_frame,
                            background=BLUE,
                            width=750,
                            height=75,
                            highlightbackground=DARK_GRAY,
                            highlightthickness=3)
        title_frame.grid(row=1, column=0, columnspan=3)
        title_frame.pack_propagate(False)
        Label(title_frame,
              text=f"Order Confirmation | Amount of items: {self.quantity_of_order}",
              font=("Verdana", 20),
              background="#5bc5da").pack(pady=(12, 0))

        background_frame = Frame(order_confirmation_frame,
                                 background=BROWN,
                                 width=750,
                                 height=255,
                                 highlightbackground=DARK_GRAY,
                                 highlightthickness=3)
        background_frame.grid(row=2, column=0, columnspan=3, sticky=N)
        background_frame.pack_propagate(False)

        item_frame = Frame(background_frame, width=730, height=235)
        item_frame.pack(pady=10)
        item_frame.pack_propagate(False)
        item_frame.grid_propagate(False)

        item_no_one = Frame(item_frame,
                            background="black",
                            width=300,
                            height=100)
        item_no_one.grid(row=0, column=0, sticky=W)
        item_no_one.grid_propagate(False)

        item_no_two = Frame(item_frame,
                            background=LIGHT_GRAY,
                            width=300,
                            height=10)
        item_no_two.grid(row=0, column=1, sticky=E)

        Button(order_confirmation_frame, text="Confirm", bg=GREEN, command=self.next_frame)\
            .grid(row=4, column=2, sticky=SE)
        Button(order_confirmation_frame, text="Menu", bg=RED, command=self.prev_frame).grid(row=4, column=0, sticky=SW)

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

    def change_menu(self, menu_frame):
        for page in self.menu_screens:
            page.pack_forget()
        self.menu_screens[menu_frame].pack(pady=10)
        self.order_categories.grid(row=0, column=0, columnspan=2, sticky=N)

    def add_order(self, var_num):
        var_num += 1

    def reduce_order(self):
        self.quantity_of_order -= 1
        print(self.quantity_of_order)

    def remove_order(self):
        self.quantity_of_order = 0


root = Tk()
root.geometry("801x452")
cafe_kiosk = Interface(root)
root.mainloop()
