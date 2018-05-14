# contents of weapon frame

#======================
# imports
#======================

import tkinter as tk
from tkinter import ttk
from Gauss_Frame import *

#======================
# class that defines tabs
#======================

class Weapons (ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        GaussWeapons = Gauss_Weapons(self.notebook)
        self.notebook.add(GaussWeapons, text="Gauss Weapon Designer")
