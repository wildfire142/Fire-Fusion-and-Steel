# contents of weapon frame

#======================
# imports
#======================

import tkinter as tk
from tkinter import ttk
from Gauss_Frame import *
from Small_Arms_Frame import *


#======================
# class that defines tabs
#======================

class Weapons (ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        GaussWeapons = Gauss_Weapons(self.notebook)
        SmallArms = Small_Arms(self.notebook)
        self.notebook.add(SmallArms, text="Small Arms Designer")
        self.notebook.add(GaussWeapons, text="Gauss Weapon Designer")
