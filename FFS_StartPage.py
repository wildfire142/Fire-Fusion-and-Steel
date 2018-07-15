import tkinter as tk
from tkinter import ttk

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, text="Weapon Designers")
        label.grid(column=0, row=0, \
                                   sticky= "W", padx=5, pady=5)

        button1 = ttk.Button(self, text="Small Arms",
                            command=lambda: self.controller.show_frame("SmallArms"))
        button1.grid(column=0, row=1, \
                                   sticky= "W", padx=5, pady=5)
        
        button2 = ttk.Button(self, text="Gauss Weapons",
                            command=lambda: self.controller.show_frame("GaussWeapons"))

        button2.grid(column=0, row=2, \
                                   sticky= "W", padx=5, pady=5)


    def print_it(self):

        page_gauss = self.controller.get_page("GaussWeapons")
        value = page_gauss.TechLevel.get()



