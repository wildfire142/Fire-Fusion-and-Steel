import tkinter as tk
from tkinter import ttk

class Load_Window (ttk.Frame):

    Load_Choice = str()
    
    def __init__(self, rows):
        tk.Frame.__init__(self)

        load_window = tk.Toplevel()
        load_window.title("Load Design")
        load_window.grab_set()
        load_window.focus()

        PositionRight = int(load_window.winfo_screenwidth()/2)
        PositionDown = int(load_window.winfo_screenheight()/2)
        load_window.geometry("+{}+{}".format(PositionRight, PositionDown))


        LoadList = tk.StringVar(value =rows)
        self.load_listbox = tk.Listbox(master=load_window, \
                                       listvariable=LoadList, \
                                       selectmode= "SINGLE")
        self.load_listbox.pack(fill="both", expand=True)
        self.load_listbox.bind ("<<ListboxSelect>>" , lambda event: Selection_Made())


        def Selection_Made():
            load_choice = self.load_listbox.get(self.load_listbox.curselection())
            Load_Window.Load_Choice = load_choice
            load_window.quit()
            load_window.destroy()
        
        load_window.mainloop()
