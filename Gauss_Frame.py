# contents of Gauss weapon frame
import tkinter as tk
from tkinter import ttk
import sqlite3
from FFS_Load_Window import Load_Window
from Gauss_Weapons_Calcs import GaussWeaponsCalcs

class GaussWeapons(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)


        
#======================
# Common data Frame
#======================

        self.CommonInfo = ttk.LabelFrame(self, text="Common Data")
        self.CommonInfo.grid(column=0, row=0, sticky= "NWES", padx=5, pady=5)

        #======================
        # Labels
        #======================

        # Weapon name widget label
        self.WeaponName_label = ttk.Label(self, text="Weapon Designation")
        self.WeaponName_label.grid(in_=self.CommonInfo, column=0, row=1, \
                                   sticky= "W", padx=5, pady=5)

        # tech Level widget label
        self.TechLevel_label = ttk.Label(self, text="Tech Level")
        self.TechLevel_label.grid(in_=self.CommonInfo, column=0, row=2, \
                                  sticky= "W", padx=5, pady=5)

        #======================
        # widgets
        #======================

        # Adding a Textbox Entry widget for WeaponName
        self.WeaponName = tk.StringVar()
        self.WeaponNameBox = ttk.Entry(self, textvariable=self.WeaponName)
        self.WeaponNameBox.grid(in_=self.CommonInfo, column=1, \
                                row=1, padx=5, pady=5, sticky= "WE")
        self.WeaponNameBox.bind ('<KeyRelease>', \
                                 lambda event: self.Check_Is_Not_Empty("WeaponName") ) 

        # Adding a Combo box widget for Tech Level
        self.TechLevel = tk.IntVar()
        self.TechLevelBox = ttk.Combobox(self, width=12, textvariable=self.TechLevel,\
                                         state='readonly')
        self.TechLevelBox['values'] = (10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21)
        self.TechLevelBox.grid(in_=self.CommonInfo, column=1, row=2, padx=5, pady=5)
        self.TechLevelBox.current(0)
        self.TechLevelBox.bind ('<<ComboboxSelected>>', lambda event: self.Calc_Values() )

         # Weapon type raido button
        self.WeaponTypeVar = tk.StringVar(value="1")

        self.radWeaponType1 = tk.Radiobutton(self, text="Pistol", \
                                           variable=self.WeaponTypeVar, value="Pistol", \
                                           command= lambda : self.Calc_Values())
        self.radWeaponType1.grid(in_=self.CommonInfo, column=0, row=3, sticky=tk.W, \
                               padx=5, pady=5)
        
        self.radWeaponType2 = tk.Radiobutton(self, text="Longarm - needs two hands", \
                                           variable=self.WeaponTypeVar, value="Longarm", \
                                           command= lambda: self.Calc_Values())
        self.radWeaponType2.grid(in_=self.CommonInfo, column=1, row=3, sticky=tk.W, \
                               padx=5, pady=5)

#======================
# ammo data Frame
#======================
        

        self.AmmoInfo = ttk.LabelFrame(self, text="Ammunition Data")
        self.AmmoInfo.grid(column=0, row=1, sticky= "NWES", padx=5, pady=5)

        
        #======================
        # Labels
        #======================

        # Ammo diameter widget label
        self.GaussAmmoDiameter_label = ttk.Label(self, \
                                                 text="Gauss Ammo Diameter (mm)")
        self.GaussAmmoDiameter_label.grid(in_=self.AmmoInfo, column=0, row=1, \
                                          sticky= "W", padx=5, pady=5)

        # Ammo type radiobutton widget label
        self.GaussAmmoType_label = ttk.Label(self, text="Ammo Production Type")
        self.GaussAmmoType_label.grid(in_=self.AmmoInfo, column=0, row=2, \
                                          sticky= "W", padx=5, pady=5)

        #======================
        # widgets
        #======================

        # Adding a Textbox Entry widget for Ammo diameter
        self.AmmoDiameter = tk.StringVar(self, value="4")
        self.GaussAmmoDiameter = ttk.Entry(self, width=15, textvariable=self.AmmoDiameter)
        self.GaussAmmoDiameter.grid(in_=self.AmmoInfo, column=1, row=1, padx=5, pady=5)
        self.GaussAmmoDiameter.bind ('<KeyRelease>', \
                                 lambda event: self.Check_Is_Not_Empty("AmmoDiameter") ) 

        # Ammo type military or Commercial
        self.AmmoTypeVar = tk.DoubleVar()

        self.radAmmoType1 = tk.Radiobutton(self, text="Military - mass produced", \
                                           variable=self.AmmoTypeVar, value=0.02, \
                                           command= lambda : self.Calc_Values())
        self.radAmmoType1.grid(in_=self.AmmoInfo, column=1, row=3, sticky=tk.W, \
                               padx=5, pady=5)
        self.radAmmoType1.select()

        self.radAmmoType2 = tk.Radiobutton(self, text="Commerical rounds", \
                                           variable=self.AmmoTypeVar, value=0.04, \
                                           command= lambda: self.Calc_Values())
        self.radAmmoType2.grid(in_=self.AmmoInfo, column=0, row=3, sticky=tk.W, \
                               padx=5, pady=5)

#======================
# Weapon data Frame
#======================


        self.WeaponInfo = ttk.LabelFrame(self, text="Weapon Data")
        self.WeaponInfo.grid(column=1, row=0, sticky= "NWES", \
                             padx=5, pady=5)


        #======================
        # Labels
        #======================

        # muzzle velocity widget label
        self.MuzzleVelocity_label = ttk.Label(self, text="Muzzle Velocity (m\s)")
        self.MuzzleVelocity_label.grid(in_=self.WeaponInfo, column=0, row=1, \
                                       sticky= "W", padx=5, pady=5)

        # Rate of Fire widget label
        self.RateofFire_label = ttk.Label(self, text="Rate of Fire")
        self.RateofFire_label.grid(in_=self.WeaponInfo, column=0, row=2, \
                                   sticky= "W", padx=5, pady=5)

        # magazine size widget label
        self.MagazineCap_label = ttk.Label(self, text="Magazine Capacity")
        self.MagazineCap_label.grid(in_=self.WeaponInfo, column=0, row=3, \
                                    sticky= "W", padx=5, pady=5)

        # magazine type widget label
        self.MagazineCap_label = ttk.Label(self, text="Magazine Type")
        self.MagazineCap_label.grid(in_=self.WeaponInfo, column=0, row=4, \
                                    sticky= "W", padx=5, pady=5)

        # stock widget label
        self.Stock_label = ttk.Label(self, text="Stock")
        self.Stock_label.grid(in_=self.WeaponInfo, column=0, row=5, \
                                    sticky= "W", padx=5, pady=5)

        # sight widget label
        self.Sight_label = ttk.Label(self, text="Sights")
        self.Sight_label.grid(in_=self.WeaponInfo, column=0, row=6, \
                                    sticky= "W", padx=5, pady=5)
        # Shock Absorber widget label
        self.RecoilAbsorb_label = ttk.Label(self, text="Recoil Reduction - Shock Absorber")
        self.RecoilAbsorb_label.grid(in_=self.WeaponInfo, column=0, row=10, \
                                    sticky= "W", padx=5, pady=5)

        # Compensator widget label
        self.RecoilComp_label = ttk.Label(self, text="Recoil Reduction - Compensator")
        self.RecoilComp_label.grid(in_=self.WeaponInfo, column=0, row=11, \
                                    sticky= "W", padx=5, pady=5)

        #======================
        # widgets
        #======================

        # Adding a Textbox Entry widget for Muzzle Velocity
        self.MuzzleVelocity = tk.StringVar(self, value="1500")
        self.GaussMuzzleVelocity = ttk.Entry(self, width=15, textvariable=self.MuzzleVelocity)
        self.GaussMuzzleVelocity.grid(in_=self.WeaponInfo, column=1, row=1, padx=5, pady=5)
        self.GaussMuzzleVelocity.bind ('<KeyRelease>', \
                                 lambda event: self.Check_Is_Not_Empty("MuzzleVelocity") )

        # Adding a Combo box widget for Rate of Fire
        self.RateofFire = tk.StringVar()
        self.RateofFireBox = ttk.Combobox(self, width=12, textvariable=self.RateofFire,\
                                          state='readonly')
        self.RateofFireBox['values'] = ('SA', '5', '10', '5/10', '50')
        self.RateofFireBox.grid(in_=self.WeaponInfo, column=1, row=2, padx=5, pady=5)
        self.RateofFireBox.current(0)
        self.RateofFireBox.bind ('<<ComboboxSelected>>', lambda event: self.Calc_Values() )

        # Adding a Textbox Entry widget for Magazine Capacity
        self.MagazineCap = tk.StringVar(self, value="10")
        self.MagazineCapacity = ttk.Entry(self, width=15, textvariable=self.MagazineCap)
        self.MagazineCapacity.grid(in_=self.WeaponInfo, column=1, row=3, padx=5, pady=5)
        self.MagazineCapacity.bind ('<KeyRelease>', \
                                 lambda event: self.Check_Is_Not_Empty ("MagazineCap") ) 

        # Adding a Combo box widget for magazine type
        self.MagazineType = tk.StringVar()
        self.MagazineTypeBox = ttk.Combobox(self, textvariable=self.MagazineType\
                                            , state='readonly')
        self.MagazineTypeBox['values'] = ('Grip Magazine', 'Box Magazine', 'Cassette')
        self.MagazineTypeBox.grid(in_=self.WeaponInfo, column=1, row=4, padx=5, pady=5)
        self.MagazineTypeBox.current(0)
        self.MagazineTypeBox.bind ('<<ComboboxSelected>>', lambda event: self.Calc_Values() )

        # Adding a Combo box widget for Stock type
        self.StockType = tk.StringVar()
        self.StockTypeBox = ttk.Combobox(self, textvariable=self.StockType,\
                                         state='readonly')
        self.StockTypeBox['values'] = ('Pistol grip', 'Hollow pistol grip', 'Rifle stock',\
                                       'Bullpup rifle stock')
        self.StockTypeBox.grid(in_=self.WeaponInfo, column=1, row=5, padx=5, pady=5)
        self.StockTypeBox.current(0)
        self.StockTypeBox.bind ('<<ComboboxSelected>>', lambda event: self.Calc_Values() )

        # Adding a Combo box widget for Sights
        self.SightType = tk.StringVar()
        self.SightTypeBox = ttk.Combobox(self, textvariable=self.SightType\
                                         ,state='readonly')
        self.SightTypeBox['values'] = ('Iron sights', 'Optic sights', 'Telescopic sights',\
                                       'Electronic sights')
        self.SightTypeBox.grid(in_=self.WeaponInfo, column=1, row=6, padx=5, pady=5)
        self.SightTypeBox.current(0)
        self.SightTypeBox.bind ('<<ComboboxSelected>>', lambda event: self.Calc_Values() )

        # lasersights option option

        self.LaserSight = tk.IntVar()
        self.LaserSightCheck = tk.Checkbutton(self, text="Laser Sight", \
                                           variable=self.LaserSight, \
                                           command= lambda: self.Set_Outputs())
        self.LaserSightCheck.grid(in_=self.WeaponInfo, column=1, row=9, sticky=tk.W, \
                               padx=5, pady=5)
        self.LaserSightCheck.deselect()

        # Adding a Combo box widget for Recoil shock abosorber
        self.RecoilAbsorb = tk.StringVar()
        self.RecoilAbsorbBox = ttk.Combobox(self, textvariable=self.RecoilAbsorb)
        self.RecoilAbsorbBox['values'] = ('None', 'Folding SA stock', 'SA stock')
        self.RecoilAbsorbBox.grid(in_=self.WeaponInfo, column=1, row=10, padx=5, pady=5)
        self.RecoilAbsorbBox.current(0)
        self.RecoilAbsorbBox.bind ('<<ComboboxSelected>>', lambda event: self.Calc_Values() )

        # Adding a Combo box widget for Recoil Compenators
        self.RecoilComp = tk.StringVar()
        self.RecoilCompBox = ttk.Combobox(self, width=24, textvariable=self.RecoilComp,\
                                          state='readonly')
        self.RecoilCompBox['values'] = ('None', 'Gyroscopic Compensator',\
                                        'Inertial Compensator')
        self.RecoilCompBox.grid(in_=self.WeaponInfo, column=1, row=11, padx=5, pady=5)
        self.RecoilCompBox.current(0)
        self.RecoilCompBox.bind ('<<ComboboxSelected>>', lambda event: self.Calc_Values() )



#======================
# Weapon Options Frame
#======================


        self.OptionsInfo = ttk.LabelFrame(self, text="Weapon Options")
        self.OptionsInfo.grid(column=1, row=1, \
                              sticky= "NWES", padx=5, pady=5)


        #======================
        # Labels
        #======================



        # Mount type widget label
        self.MountType_label = ttk.Label(self, text="Mount Options")
        self.MountType_label.grid(in_=self.OptionsInfo, column=0, row=0, \
                                    sticky= "W", padx=5, pady=5)

        # Weapon options widget label
        self.WeaponAddOns_label = ttk.Label(self, text="Weapon Additional Options")
        self.WeaponAddOns_label.grid(in_=self.OptionsInfo, column=0, row=4, \
                                    sticky= "W", padx=5, pady=5)

        #======================
        # widgets
        #======================


        # Mount Options
        self.MountType = tk.StringVar()

        self.radMountType1 = tk.Radiobutton(self, text="No Mounting", \
                                           variable=self.MountType, value='None', \
                                           command= lambda : self.Calc_Values())
        self.radMountType1.grid(in_=self.OptionsInfo, column=1, row=0, sticky=tk.W, \
                               padx=5, pady=5)
        self.radMountType1.select()

        self.radMountType2 = tk.Radiobutton(self, text="Bipod", \
                                           variable=self.MountType, value='Bipod', \
                                           command= lambda: self.Calc_Values())
        self.radMountType2.grid(in_=self.OptionsInfo, column=1, row=1, sticky=tk.W, \
                               padx=5, pady=5)

        self.radMountType3 = tk.Radiobutton(self, text="Tripod", \
                                           variable=self.MountType, value='Tripod', \
                                           command= lambda: self.Calc_Values())
        self.radMountType3.grid(in_=self.OptionsInfo, column=1, row=2, sticky=tk.W, \
                               padx=5, pady=5)

        self.radMountType4 = tk.Radiobutton(self, text="Vehicle Mounted", \
                                           variable=self.MountType, value='Vehicle', \
                                           command= lambda: self.Calc_Values())
        self.radMountType4.grid(in_=self.OptionsInfo, column=1, row=3, sticky=tk.W, \
                               padx=5, pady=5)

        # bayonet lug option
        self.BayonetLug = tk.StringVar()
        self.BayonetLugCheck = tk.Checkbutton(self, text="Bayonet Lug", \
                                           variable=self.BayonetLug, \
                                           command= lambda: self.Calc_Values())
        self.BayonetLugCheck.grid(in_=self.OptionsInfo, column=1, row=4, sticky=tk.W, \
                               padx=5, pady=5)
        self.BayonetLugCheck.deselect()

        # grenade adapator option

        self.Grenade = tk.StringVar()
        self.GrenadeCheck = tk.Checkbutton(self, text="Grenade Adapator", \
                                           variable=self.Grenade, \
                                           command= lambda: self.Calc_Values())
        self.GrenadeCheck.grid(in_=self.OptionsInfo, column=1, row=5, sticky=tk.W, \
                               padx=5, pady=5)
        self.GrenadeCheck.deselect()
        
        # silenced option

        self.Silenced = tk.StringVar()
        self.SilencedCheck = tk.Checkbutton(self, text="Silenced Weapon", \
                                           variable=self.Silenced, \
                                           command= lambda: self.Calc_Values())
        self.SilencedCheck.grid(in_=self.OptionsInfo, column=1, row=6, sticky=tk.W, \
                               padx=5, pady=5)
        self.SilencedCheck.deselect()

#======================
# Design output Frame
#======================


        self.DesignInfo = ttk.LabelFrame(self, text="Design Statistics")
        self.DesignInfo.grid(column=2, row=0, sticky= "NWES",\
                             padx=5, pady=5, rowspan =2)



        #======================
        # widgets
        #======================


        # Adding a Textbox widget for Final Design
        self.FinalDesignBox = tk.Text(self, width=108, height=32)
        self.FinalDesignBox.grid(in_=self.DesignInfo, column=0, row=1, \
                                 sticky= "NWES", padx=5, pady=5)


#======================
# Errors Frame
#======================


        self.ErrorsInfo = ttk.LabelFrame(self, text="Design Errors")
        self.ErrorsInfo.grid(column=2, row=2, \
                              sticky= "NWES", padx=5, pady=5)


        #======================
        # Labels
        #======================



        # MuzzleVelocity warning label
        self.MuzzleVelocityError_label = ttk.Label\
                               (self, text="Muzzle Velocity must be no greater than 6000 m/s")

        # Grip magazine size warning label
        self.GripMagMaxRoundsError_label = ttk.Label\
                               (self)

        # Grip magazine Length warning label
        self.GripMagLengthError_label = ttk.Label\
                               (self,text="Rounds too long for grip magazine use box magazine instead" )


        # Max Ammo diameter warning label
        self.MaxAmmoDiameterError_label = ttk.Label\
                               (self,text="Maximum ammo diameter 20mm" )
        
        # Box magazine size warning label
        self.BoxMagCapError_label = ttk.Label\
                               (self)

        # MuzzleVelocity warning label
        self.SightTypeError_label = ttk.Label\
                               (self, text="Can not fit that type of sight to a one handed weapon")

        # Box mag max Length warning label
        self.BoxMagLengthError_label = ttk.Label\
                               (self,text="Receiver Length too short for a box magazine" )



        #======================
        # widgets
        #======================

    def on_show_frame(self, event):
        self.controller.currentpage = "GaussWeapons"

    def Design_Error_Checks(self):

        #disables recoil comps for pistol weapons

        if self.WeaponTypeVar == "Pistol":
            self.RecoilCompBox.configure(state='disabled')
            self.RecoilAbsorbBox.configure(state='disabled')
        else:
            self.RecoilCompBox.configure(state='readonly')
            self.RecoilAbsorbBox.configure(state='readonly')

        #excess muzzle velocity warning

        if GaussWeaponsCalcs.MuzzleVelocity > 6000:
            self.MuzzleVelocityError_label.grid(in_=self.ErrorsInfo, column=0, \
                                    sticky= "W", padx=5, pady=5)
        else:
            self.MuzzleVelocityError_label.grid_forget()

        # max ammo diameter   

        if  GaussWeaponsCalcs.AmmoDiameter > 20.0:
            self.MaxAmmoDiameterError_label.grid(in_=self.ErrorsInfo, column=0, \
                                   sticky= "W", padx=5, pady=5)
        else:
            self.MaxAmmoDiameterError_label.grid_forget()

        #excess rounds in grip mag warning
                
        GripMagazineCap= 140/GaussWeaponsCalcs.AmmoDiameter

        if (self.MagazineType =="Grip Magazine") and \
            (self.MagazineCap > GripMagazineCap):
            self.GripMagMaxRoundsError_label.configure(text="Too many rounds in grip magazine max rounds equals "\
                                             +str(int(GripMagazineCap))) 
            self.GripMagMaxRoundsError_label.grid(in_=self.ErrorsInfo, column=0, \
                                 sticky= "W", padx=5, pady=5)
        else:
            self.GripMagMaxRoundsError_label.grid_forget()

        # rounds too long for grip magazines    

        if (self.MagazineType =="Grip Magazine") and \
            (GaussWeaponsCalcs.AmmoDiameter*5 > 60):
            self.GripMagLengthError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
        else:
            self.GripMagLengthError_label.grid_forget()

        # max rounds for box magazines

        if (self.MagazineType == "Box Magazine"):
            if (GaussWeaponsCalcs.MagazineCap > 100) and \
                (GaussWeaponsCalcs.GaussAmmoWeight > 15):
                self.BoxMagCapError_label.configure(text="Max capacity 100 rounds")
                self.BoxMagCapError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
            elif (GaussWeaponsCalcs.MagazineCap > 200) and \
                    (GaussWeaponsCalcs.GaussAmmoWeight < 15):
                self.BoxMagCapError_label.configure(text="Max capacity 200 rounds")
                self.BoxMagCapError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
            else:
                self.BoxMagCapError_label.grid_forget()
        else:
            self.BoxMagCapError_label.grid_forget()

        #reciver too short for box mag warnings
        if (self.MagazineType == "Box Magazine"):
            if ((self.AmmoDiameter*5)+150) >(GaussWeaponsCalcs.RecieverLength*10):
                self.BoxMagLengthError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
            else:
                self.BoxMagLengthError_label.grid_forget()

        #wrong sight types warnings

        if ((self.SightType == "Telescopic sights") or\
            (self.SightType == "Electronic sights")) and \
            self.WeaponTypeVar == "Pistol":
            self.SightTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
        else:
            self.SightTypeError_label.grid_forget()

    def WidgetValues(self):
        WidgetValues = []
        WidgetValues.append(self.TechLevel.get())
        WidgetValues.append(self.WeaponName.get())
        WidgetValues.append(self.AmmoDiameter.get())
        WidgetValues.append(self.AmmoTypeVar.get())
        WidgetValues.append(self.MuzzleVelocity.get())
        WidgetValues.append(self.RateofFire.get())
        WidgetValues.append(self.MagazineCap.get())
        WidgetValues.append(self.StockType.get())
        WidgetValues.append(self.MountType.get())
        WidgetValues.append(self.MagazineType.get())
        WidgetValues.append(self.SightType.get())
        WidgetValues.append(self.RecoilAbsorb.get())
        WidgetValues.append(self.RecoilComp.get())
        WidgetValues.append(self.BayonetLug.get())
        WidgetValues.append(self.Grenade.get())
        WidgetValues.append(self.Silenced.get())
        WidgetValues.append(self.WeaponTypeVar.get())
        WidgetValues.append(self.LaserSight.get())

        return WidgetValues

    def Calc_Values(self):
        WidgetValues = self.WidgetValues()
        GaussWeaponsCalcs (WidgetValues)
        self.Design_Error_Checks ()
        self.FinalDesignBox.delete('1.0', 'end')
        self.FinalDesignBox.insert('1.0', GaussWeaponsCalcs.FinalDesign)

            
    def Check_Is_Not_Empty(self, name):
        CheckVariable = "self."+name+".get()"
        if len(eval(CheckVariable)) != 0:
            self.Calc_Values()

    def Save_Data (self):
        #collect data for saving

        #Design settings from inputs

        WidgetSaveValues = self.WidgetValues()

        WidgetSaveValues = ','.join(map(str,WidgetSaveValues))

        VehicleValues = [1,1]
        VehicleValues = ','.join(map(str,VehicleValues))

        #connect to database

        conn = sqlite3.connect('FireFusionAndSteel.db', isolation_level=None)

        c = conn.cursor()

        # create a table if not already there

        c.execute ('''CREATE TABLE IF NOT EXISTS Gauss ("id" INTEGER PRIMARY KEY,
                        "name" TEXT, "WidgetValues" TEXT, "VehicleValues" TEXT)
                        ''')
        # insert save data into table
        sql = '''INSERT INTO Gauss (name, WidgetValues, VehicleValues)
        VALUES (?,?,?)'''

        name = (str(self.WeaponName.get()))
        widget = WidgetSaveValues
        vehicle = VehicleValues

        data = (name,widget,vehicle)

        c.execute(sql, data)


    def Load_Data(self):

        #connect to database

        conn = sqlite3.connect('FireFusionAndSteel.db', isolation_level=None)

        conn.row_factory = lambda cursor, row: row[0]

        c = conn.cursor()

        # get list of weapon names
        
        rows = c.execute ('SELECT name FROM Gauss').fetchall()

        Load_Window(rows)

        Choice = Load_Window.Load_Choice

       
        SavedData = c.execute ('SELECT WidgetValues FROM Gauss WHERE name =?',\
                                            (Choice,)).fetchall()

        WidgetValuesJoined = SavedData[0]
        WidgetLoadedValues = WidgetValuesJoined.split(",")
        

        page_gauss = self.controller.get_page("GaussWeapons")
        page_gauss.TechLevel.set(WidgetLoadedValues[0])
        page_gauss.WeaponName.set(WidgetLoadedValues[1])
        page_gauss.AmmoDiameter.set(WidgetLoadedValues[2])
        page_gauss.AmmoTypeVar.set(WidgetLoadedValues[3])
        page_gauss.MuzzleVelocity.set(WidgetLoadedValues[4])
        page_gauss.RateofFire.set(WidgetLoadedValues[5])
        page_gauss.MagazineCap.set(WidgetLoadedValues[6])
        page_gauss.StockType.set(WidgetLoadedValues[7])
        page_gauss.MountType.set(WidgetLoadedValues[8])
        page_gauss.MagazineType.set(WidgetLoadedValues[9])
        page_gauss.SightType.set(WidgetLoadedValues[10])
        page_gauss.RecoilAbsorb.set(WidgetLoadedValues[11])
        page_gauss.RecoilComp.set(WidgetLoadedValues[12])
        page_gauss.BayonetLug.set(WidgetLoadedValues[13])
        page_gauss.Grenade.set(WidgetLoadedValues[14])
        page_gauss.Silenced.set(WidgetLoadedValues[15])
        page_gauss.WeaponTypeVar.set(WidgetLoadedValues[16])
        page_gauss.LaserSight.set(WidgetLoadedValues[17])
        self.Calc_Values()


