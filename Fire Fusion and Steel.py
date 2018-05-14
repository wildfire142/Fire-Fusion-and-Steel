#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
from Weapons_Frame import Weapons

#======================
# tab defintitions
#======================

class FireFusionSteel(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        #Spacecraft_Frame = Spacecraft(self.notebook)
        Weapons_Frame = Weapons(self.notebook)
        #self.notebook.add(GaussWeapons, text="Spacecraft Designer")
        self.notebook.add(Weapons_Frame, text="Weapons Designers")

#======================
# runs GUI
#======================

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Fire Fusion and Steel")
    FireFusionSteel(root).pack(fill="both", expand=True)
    root.mainloop()


