import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from FFS_Menu_Bar import MenuBar
from FFS_StartPage import StartPage
from Gauss_Frame import GaussWeapons
from Small_Arms_Frame import SmallArms



class FireFusionAndSteel(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self) 
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        menu_bar = MenuBar(parent=container, controller=self)
        self.config(menu=menu_bar)

        self.frames = {}
        self.frames["StartPage"] = StartPage(parent=container, controller=self)
        self.frames["SmallArms"] = SmallArms(parent=container, controller=self)
        self.frames["GaussWeapons"] = GaussWeapons(parent=container, controller=self)

        self.frames["StartPage"].grid(row=0, column=0, sticky="nsew")
        self.frames["SmallArms"].grid(row=0, column=0, sticky="nsew")
        self.frames["GaussWeapons"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

        self.currentpage = "StartPage"

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.event_generate("<<ShowFrame>>")
        frame.tkraise()

    def get_page(self, classname):
        '''Returns an instance of a page given it's class name as a string'''
        for page in self.frames.values():
            if str(page.__class__.__name__) == classname:
                return page
        return None


if __name__ == "__main__":
    root = FireFusionAndSteel()
    root.title("Fire Fusion and Steel")
    windowWidth = root.winfo_reqwidth()
    PositionRight = 270
    PositionDown = 0
    root.geometry("+{}+{}".format(PositionRight, PositionDown))
    root.mainloop()
