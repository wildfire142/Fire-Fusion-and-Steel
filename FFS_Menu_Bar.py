import tkinter as tk
from tkinter import ttk
from tkinter import Menu

class MenuBar(tk.Menu):
    
    def __init__(self, parent, controller):
        tk.Menu.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.MenuBar_Setup()

    def MenuBar_Setup(self): 
        file_menu = Menu(self, tearoff=0) # create file menu
        # add file menu to menu bar
        self.add_cascade(label="File", menu=file_menu)
        #add save item
        file_menu.add_command(label="Save", \
                              command = self._save) 
        #add load item
        file_menu.add_command(label="Load", command = self._load )
        file_menu.add_separator() #add separator
        # add exit item
        file_menu.add_command(label="Exit", command = self._quit)

        # create weapon designers menu
        weapon_menu = Menu(self, tearoff=0)
        #add weapons designer menu to menu bar
        self.add_cascade(label="Weapon Designers", menu=weapon_menu)
        #add small arms
        weapon_menu.add_command(label="Small Arms", \
                              command=lambda: self.controller.show_frame("SmallArms") )
        #add gauss weapons
        weapon_menu.add_command(label="Gauss Weapons", \
                                command=lambda: self.controller.show_frame("GaussWeapons"))
        weapon_menu.add_separator() #add separator
        

    #quits program
    def _quit(self):
        self.controller.quit()
        self.controller.destroy()
        exit()

    #calls save function
    def _save(self):
        page = self.controller.get_page(self.controller.currentpage)
        page.Save_Data()


    #calls load function on first layer notebook
    def _load(self):
        page = self.controller.get_page(self.controller.currentpage)
        page.Load_Data()
        

