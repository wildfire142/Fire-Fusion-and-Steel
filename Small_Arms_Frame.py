import tkinter as tk
from tkinter import ttk
import sqlite3
import math
from FFS_Load_Window import Load_Window
from Small_Arms_Calcs import SmallArmsCalcs

class SmallArms(tk.Frame):

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
        self.TechLevelBox['values'] = (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, \
                                       15, 16, 17, 18, 19, 20, 21)
        self.TechLevelBox.grid(in_=self.CommonInfo, column=1, row=2, padx=5, pady=5)
        self.TechLevelBox.current(0)
        self.TechLevelBox.bind ('<<ComboboxSelected>>', lambda event: self.Receiver_Checks() )

         # Weapon type raido button
        self.WeaponTypeVar = tk.StringVar(value="1")

        self.radWeaponType1 = tk.Radiobutton(self, text="Pistol", \
                                           variable=self.WeaponTypeVar, value="Pistol", \
                                           command= lambda: self.Shotgun_Checks())
        self.radWeaponType1.grid(in_=self.CommonInfo, column=0, row=3, sticky=tk.W, \
                               padx=5, pady=5)
        
        self.radWeaponType2 = tk.Radiobutton(self, text="Longarm - needs two hands", \
                                           variable=self.WeaponTypeVar, value="Longarm", \
                                           command= lambda: self.Shotgun_Checks())
        self.radWeaponType2.grid(in_=self.CommonInfo, column=1, row=3, sticky=tk.W, \
                               padx=5, pady=5)

        self.radWeaponType3 = tk.Radiobutton(self, text="Shotgun", \
                                           variable=self.WeaponTypeVar, value="Shotgun", \
                                           command= lambda: self.Shotgun_Checks())
        self.radWeaponType3.grid(in_=self.CommonInfo, column=0, row=4, sticky=tk.W, \
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
        self.AmmoDiameter_label = ttk.Label(self, text="Bullet Diameter (mm)")
        self.AmmoDiameter_label.grid(in_=self.AmmoInfo, column=0, row=1, \
                                          sticky= "W", padx=5, pady=5)
        # Ammo diameter widget label
        self.CartridgeLength_label = ttk.Label(self, text="Cartridge Case Length (mm)")
        self.CartridgeLength_label.grid(in_=self.AmmoInfo, column=0, row=2, \
                                          sticky= "W", padx=5, pady=5)
        
        # Shotgun cartridge rounds number of bullets widget label
        self.ShotgunBullets_label = ttk.Label(self, text="Bullets in shotgun shell")
        self.ShotgunBullets_label.grid(in_=self.AmmoInfo, column=0, row=3, \
                                          sticky= "W", padx=5, pady=5)

        # Flechette rounds number of darts widget label
        self.ShotgunBullets_label = ttk.Label(self, text="Darts in flechette round")
        self.ShotgunBullets_label.grid(in_=self.AmmoInfo, column=0, row=4, \
                                          sticky= "W", padx=5, pady=5)

        # Ammo type radiobutton widget label
        self.AmmoType_label = ttk.Label(self, text="Ammo Type")
        self.AmmoType_label.grid(in_=self.AmmoInfo, column=0, row=5, \
                                          sticky= "W", padx=5, pady=5)

        # Case type radiobutton widget label
        self.CaseType_label = ttk.Label(self, text="Case Type")
        self.CaseType_label.grid(in_=self.AmmoInfo, column=0, row=7, \
                                          sticky= "W", padx=5, pady=5)

        # Production type radiobutton widget label
        self.ProdType_label = ttk.Label(self, text="Production Type")
        self.ProdType_label.grid(in_=self.AmmoInfo, column=0, row=9, \
                                          sticky= "W", padx=5, pady=5)

        #======================
        # widgets
        #======================

        # Adding a Textbox Entry widget for Ammo diameter
        self.AmmoDiameter = tk.StringVar(self, value="4")
        self.SmallArmsAmmoDiameter = ttk.Entry(self, width=15, textvariable=self.AmmoDiameter)
        self.SmallArmsAmmoDiameter.grid(in_=self.AmmoInfo, column=1, row=1, padx=5, pady=5)
        self.SmallArmsAmmoDiameter.bind ('<KeyRelease>',\
                                 lambda event: self.Check_Is_Not_Empty("AmmoDiameter") ) 

        # Adding a Textbox Entry widget for Cartridge Length
        self.CartridgeLength = tk.StringVar(self, value="9")
        self.SmallArmsCartridgeLength = ttk.Entry(self, width=15,\
                                                 textvariable=self.CartridgeLength)
        self.SmallArmsCartridgeLength.grid (in_=self.AmmoInfo, column=1, row=2, padx=5, pady=5)
        self.SmallArmsCartridgeLength.bind ('<KeyRelease>',\
                                 lambda event: self.Check_Is_Not_Empty("CartridgeLength") ) 

        # Adding a Textbox Entry widget for Shotgun Bullets
        self.ShotgunBullets = tk.StringVar(self, value="4")
        self.SmallArmsShotgunBullets = ttk.Entry(self, width=15,\
                                                 textvariable=self.ShotgunBullets)
        self.SmallArmsShotgunBullets.grid (in_=self.AmmoInfo, column=1, row=3, padx=5, pady=5)
        self.SmallArmsShotgunBullets.bind ('<KeyRelease>',\
                                 lambda event: self.Check_Is_Not_Empty("ShotgunBullets") ) 
        self.SmallArmsShotgunBullets.configure(state='disabled')


        # Adding a Textbox Entry widget for Flechette darts
        self.FlechetteDarts = tk.StringVar(self, value="4")
        self.SmallArmsFlechetteDarts = ttk.Entry(self, width=15,\
                                                 textvariable=self.FlechetteDarts)
        self.SmallArmsFlechetteDarts.grid (in_=self.AmmoInfo, column=1, row=4, padx=5, pady=5)
        self.SmallArmsFlechetteDarts.bind ('<KeyRelease>',\
                                 lambda event: self.Check_Is_Not_Empty("FlechetteDarts") ) 

        # Ammo type standard or ETC
        self.AmmoTypeVar = tk.StringVar()

        self.radAmmoType1 = tk.Radiobutton(self, text="Standard", \
                                           variable=self.AmmoTypeVar, value="Standard", \
                                           command= lambda : self.Calc_Values())
        self.radAmmoType1.grid(in_=self.AmmoInfo, column=0, row=6, sticky=tk.W, \
                               padx=5, pady=5)
        self.radAmmoType1.select()

        self.radAmmoType2 = tk.Radiobutton(self, text="Electrothermal-chemical", \
                                           variable=self.AmmoTypeVar, value="ETC", \
                                           command= lambda: self.Calc_Values())
        self.radAmmoType2.configure(state='disabled')
        self.radAmmoType2.grid(in_=self.AmmoInfo, column=1, row=6, sticky=tk.W, \
                               padx=5, pady=5)


        # case type necked or straight
        self.CaseTypeVar = tk.StringVar()

        self.radCaseType1 = tk.Radiobutton(self, text="Straight", \
                                           variable=self.CaseTypeVar, value="Straight", \
                                           command= lambda : self.Calc_Values())
        self.radCaseType1.grid(in_=self.AmmoInfo, column=0, row=8, sticky=tk.W, \
                               padx=5, pady=5)
        self.radCaseType1.select()

        self.radCaseType2 = tk.Radiobutton(self, text="Necked", \
                                           variable=self.CaseTypeVar, value="Necked", \
                                           command= lambda: self.Calc_Values())
        self.radCaseType2.configure(state='disabled')
        self.radCaseType2.grid(in_=self.AmmoInfo, column=1, row=8, sticky=tk.W, \
                               padx=5, pady=5)

        # production type mass produced military or conventional
        self.ProdTypeVar = tk.StringVar()

        self.radProdType1 = tk.Radiobutton(self, text="Mass produced military", \
                                           variable=self.ProdTypeVar, value="Military", \
                                           command= lambda : self.Calc_Values())
        self.radProdType1.grid(in_=self.AmmoInfo, column=0, row=10, sticky=tk.W, \
                               padx=5, pady=5)
        self.radProdType1.select()

        self.radProdType2 = tk.Radiobutton(self, text="Conventional", \
                                           variable=self.ProdTypeVar, value="onventional", \
                                           command= lambda: self.Calc_Values())
        self.radProdType2.grid(in_=self.AmmoInfo, column=1, row=10, sticky=tk.W, \
                               padx=5, pady=5)

#======================
# Weapon data Frame
#======================


        self.WeaponInfo = ttk.LabelFrame(self, text="Weapon Data")
        self.WeaponInfo.grid(column=1, row=0, sticky= "NWES", \
                             padx=5, pady=5, rowspan =2)


        #======================
        # Labels
        #======================

        # rifling widget label
        self.Rifling_label = ttk.Label(self, text="Rifling")
        self.Rifling_label.grid(in_=self.WeaponInfo, column=0, row=1, \
                                   sticky= "W", padx=5, pady=5)
        # barrel type widget label
        self.Rifling_label = ttk.Label(self, text="Barrel type")
        self.Rifling_label.grid(in_=self.WeaponInfo, column=0, row=3, \
                                   sticky= "W", padx=5, pady=5)

        # receiver type widget label
        self.Receiver_label = ttk.Label(self, text="Receiver type")
        self.Receiver_label.grid(in_=self.WeaponInfo, column=0, row=5, \
                                   sticky= "W", padx=5, pady=5)

        # Rate of Fire widget label
        self.RateofFire_label = ttk.Label(self, text="Rate of Fire")
        self.RateofFire_label.grid(in_=self.WeaponInfo, column=0, row=6, \
                                   sticky= "W", padx=5, pady=5)

        # magazine size widget label
        self.MagazineCap_label = ttk.Label(self, text="Magazine Capacity")
        self.MagazineCap_label.grid(in_=self.WeaponInfo, column=0, row=7, \
                                    sticky= "W", padx=5, pady=5)

        # magazine type widget label
        self.MagazineCap_label = ttk.Label(self, text="Magazine Type")
        self.MagazineCap_label.grid(in_=self.WeaponInfo, column=0, row=8, \
                                    sticky= "W", padx=5, pady=5)

        # stock widget label
        self.Stock_label = ttk.Label(self, text="Stock")
        self.Stock_label.grid(in_=self.WeaponInfo, column=0, row=9, \
                                    sticky= "W", padx=5, pady=5)

        # sight widget label
        self.Sight_label = ttk.Label(self, text="Sights")
        self.Sight_label.grid(in_=self.WeaponInfo, column=0, row=10, \
                                    sticky= "W", padx=5, pady=5)
        # Shock Absorber widget label
        self.RecoilAbsorb_label = ttk.Label(self, text="Recoil Reduction - Shock Absorber")
        self.RecoilAbsorb_label.grid(in_=self.WeaponInfo, column=0, row=12, \
                                    sticky= "W", padx=5, pady=5)

        # Compensator widget label
        self.RecoilComp_label = ttk.Label(self, text="Recoil Reduction - Compensator")
        self.RecoilComp_label.grid(in_=self.WeaponInfo, column=0, row=13, \
                                    sticky= "W", padx=5, pady=5)

        # Muzzle Brake widget label
        self.RecoilBrake_label = ttk.Label(self, text="Muzzle Brake")
        self.RecoilBrake_label.grid(in_=self.WeaponInfo, column=0, row=14, \
                                    sticky= "W", padx=5, pady=5)

        #======================
        # widgets
        #======================

        # Barrel Length adjuster

        self.BarrelLengthModVar = tk.DoubleVar()
        self.BarrelLengthMod = tk.Scale (self, from_=20, to_=230, orient='horizontal',\
                                         label="Actual Barrel Length as % of Average Barrel Length",\
                                         variable=self.BarrelLengthModVar)
        self.BarrelLengthMod.grid(in_=self.WeaponInfo, column=0, row=0, columnspan=2, \
                                  sticky="NWES", padx=5, pady=5)
        self.BarrelLengthMod.set(100)                                   
        self.BarrelLengthMod.bind ('<ButtonRelease-1>', lambda event: self.Calc_Values())

        # Rifling type smoothbore or rifled
        self.RiflingTypeVar = tk.StringVar()

        self.radRiflingType1 = tk.Radiobutton(self, text="Smoothbore", \
                                           variable=self.RiflingTypeVar, value="Smoothbore", \
                                           command= lambda : self.Calc_Values())
        self.radRiflingType1.grid(in_=self.WeaponInfo, column=0, row=2, sticky=tk.W, \
                               padx=5, pady=5)
        self.radRiflingType1.select()

        self.radRiflingType2 = tk.Radiobutton(self, text="Rifled", \
                                           variable=self.RiflingTypeVar, value="Rifled", \
                                           command= lambda: self.Calc_Values())
        self.radRiflingType2.grid(in_=self.WeaponInfo, column=1, row=2, sticky=tk.W, \
                               padx=5, pady=5)

        # Barrel type heavy or light
        self.BarrelTypeVar = tk.StringVar()

        self.radBarrelType1 = tk.Radiobutton(self, text="Light", \
                                           variable=self.BarrelTypeVar, value="Light", \
                                           command= lambda : Set_Outputs())
        self.radBarrelType1.grid(in_=self.WeaponInfo, column=0, row=4, sticky=tk.W, \
                               padx=5, pady=5)
        self.radBarrelType1.select()

        self.radBarrelType2 = tk.Radiobutton(self, text="Heavy", \
                                           variable=self.BarrelTypeVar, value="Heavy", \
                                           command= lambda: self.Calc_Values())
        self.radBarrelType2.grid(in_=self.WeaponInfo, column=1, row=4, sticky=tk.W, \
                               padx=5, pady=5)


        # Adding a Combo box widget for Reciever type
        self.RecieverTypeVar = tk.StringVar()
        self.RecieverBox = ttk.Combobox(self, textvariable=self.RecieverTypeVar,\
                                          state='readonly')
        self.RecieverBox['values'] = ('Individully Loadng', 'Revolver', 'Lever Action',\
                                        'Bolt action', 'Pump action', 'Heavy self-loading',\
                                        'Light self-loading')
        self.RecieverBox.grid(in_=self.WeaponInfo, column=1, row=5, padx=5, pady=5)
        self.RecieverBox.current(0)
        self.RecieverBox.bind ('<<ComboboxSelected>>', lambda event: self.Receiver_Checks() )

        # Adding a Combo box widget for Rate of Fire
        self.RateofFire = tk.StringVar()
        self.RateofFireBox = ttk.Combobox(self, width=12, textvariable=self.RateofFire,\
                                          state='readonly')
        self.RateofFireBox['values'] = ('SS')
        self.RateofFireBox.grid(in_=self.WeaponInfo, column=1, row=6, padx=5, pady=5)
        self.RateofFireBox.current(0)
        self.RateofFireBox.bind ('<<ComboboxSelected>>', lambda event: Sself.Calc_Values() )

        # Adding a Textbox Entry widget for Magazine Capacity
        self.MagazineCap = tk.StringVar(self, value="10")
        self.MagazineCapacity = ttk.Entry(self, width=15, textvariable=self.MagazineCap)
        self.MagazineCapacity.grid(in_=self.WeaponInfo, column=1, row=7, padx=5, pady=5)
        self.MagazineCapacity.bind ('<KeyRelease>',\
                                 lambda event: self.Check_Is_Not_Empty("MagazineCap") )

        # Adding a Combo box widget for magazine type
        self.MagazineType = tk.StringVar()
        self.MagazineTypeBox = ttk.Combobox(self, textvariable=self.MagazineType\
                                            , state='readonly')
        self.MagazineTypeBox['values'] = ('Breach Loaded', 'Cylinder', 'Belt', \
                                          'Grip Magazine', 'Clip', 'Tubular magazine', \
                                          'Box Magazine', 'Cassette')
        self.MagazineTypeBox.grid(in_=self.WeaponInfo, column=1, row=8, padx=5, pady=5)
        self.MagazineTypeBox.current(0)
        self.MagazineTypeBox.bind ('<<ComboboxSelected>>', lambda event: self.Rotary_Weapon_Checks() )

        # Adding a Combo box widget for Stock type
        self.StockType = tk.StringVar()
        self.StockTypeBox = ttk.Combobox(self, textvariable=self.StockType,\
                                         state='readonly')
        self.StockTypeBox['values'] = ('Wood pistol grip', 'Hollow pistol grip', 'Wooden stock',\
                                       'Carbine stock', 'Folding stock',\
                                       'Plastic stock', 'Bullpup')
        self.StockTypeBox.grid(in_=self.WeaponInfo, column=1, row=9, padx=5, pady=5)
        self.StockTypeBox.current(0)
        self.StockTypeBox.bind ('<<ComboboxSelected>>', lambda event: self.Calc_Values() )

        # Adding a Combo box widget for Sights
        self.SightType = tk.StringVar()
        self.SightTypeBox = ttk.Combobox(self, textvariable=self.SightType\
                                         ,state='readonly')
        self.SightTypeBox['values'] = ('Iron sights', 'Optic sights', 'Telescopic sights',\
                                       'Electronic sights')
        self.SightTypeBox.grid(in_=self.WeaponInfo, column=1, row=10, padx=5, pady=5)
        self.SightTypeBox.current(0)
        self.SightTypeBox.bind ('<<ComboboxSelected>>', lambda event: self.Calc_Values() )


        # lasersights option option

        self.LaserSight = tk.IntVar()
        self.LaserSightCheck = tk.Checkbutton(self, text="Laser Sight", \
                                           variable=self.LaserSight, \
                                           command= lambda: self.Calc_Values())
        self.LaserSightCheck.grid(in_=self.WeaponInfo, column=1, row=11, sticky=tk.W, \
                               padx=5, pady=5)
        self.LaserSightCheck.deselect()

        # Adding a Combo box widget for Recoil shock abosorber
        self.RecoilAbsorb = tk.StringVar()
        self.RecoilAbsorbBox = ttk.Combobox(self, textvariable=self.RecoilAbsorb)
        self.RecoilAbsorbBox['values'] = ('None', 'Folding SA stock', 'SA stock')
        self.RecoilAbsorbBox.grid(in_=self.WeaponInfo, column=1, row=12, padx=5, pady=5)
        self.RecoilAbsorbBox.current(0)
        self.RecoilAbsorbBox.bind ('<<ComboboxSelected>>', lambda event: self.Calc_Values() )

        # Adding a Combo box widget for Recoil Compenators
        self.RecoilComp = tk.StringVar()
        self.RecoilCompBox = ttk.Combobox(self, width=24, textvariable=self.RecoilComp,\
                                          state='readonly')
        self.RecoilCompBox['values'] = ('None', 'Gyroscopic Compensator',\
                                        'Inertial Compensator')
        self.RecoilCompBox.grid(in_=self.WeaponInfo, column=1, row=13, padx=5, pady=5)
        self.RecoilCompBox.current(0)
        self.RecoilCompBox.bind ('<<ComboboxSelected>>', lambda event: self.Calc_Values() )

        # Adding a Combo box widget for Muzzle brakes
        self.RecoilBrake = tk.StringVar()
        self.RecoilBrakeBox = ttk.Combobox(self, width=24, textvariable=self.RecoilBrake,\
                                          state='readonly')
        self.RecoilBrakeBox['values'] = ('None', 'Muzzle Brake',\
                                        'Long Muzzle Brake')
        self.RecoilBrakeBox.grid(in_=self.WeaponInfo, column=1, row=14, padx=5, pady=5)
        self.RecoilBrakeBox.current(0)
        self.RecoilBrakeBox.bind ('<<ComboboxSelected>>', lambda event: self.Calc_Values() )



#======================
# Weapon Options Frame
#======================


        self.OptionsInfo = ttk.LabelFrame(self, text="Weapon Options")
        self.OptionsInfo.grid(column=0, row=2, sticky= "NWES", padx=5, pady=5, \
                              columnspan=2)


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

        # Tublar magazine widget label
        self.WeaponAddOns_label = ttk.Label(self, text="Tubular magazine mount options")
        self.WeaponAddOns_label.grid(in_=self.OptionsInfo, column=2, row=0, \
                                    sticky= "W", padx=5, pady=5)

        # Flash suppressor widget label
        self.WeaponAddOns_label = ttk.Label(self, text="Flash Suppressor options")
        self.WeaponAddOns_label.grid(in_=self.OptionsInfo, column=2, row=3, \
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
                                           command= lambda: Set_Outputs())
        self.GrenadeCheck.grid(in_=self.OptionsInfo, column=1, row=5, sticky=tk.W, \
                               padx=5, pady=5)
        self.GrenadeCheck.deselect()
        
        # silenced option

        self.Silenced = tk.IntVar()
        self.SilencedCheck = tk.Checkbutton(self, text="Silenced Weapon", \
                                           variable=self.Silenced, \
                                           command= lambda: self.Calc_Values())
        self.SilencedCheck.grid(in_=self.OptionsInfo, column=1, row=6, sticky=tk.W, \
                               padx=5, pady=5)
        self.SilencedCheck.deselect()

        # supressor option

        self.Suppressor = tk.IntVar()
        self.SuppressorCheck = tk.Checkbutton(self, text="Supressed Weapon", \
                                           variable=self.Suppressor , \
                                           command= lambda: Set_Outputs())
        self.SuppressorCheck.grid(in_=self.OptionsInfo, column=2, row=6, sticky=tk.W, \
                               padx=5, pady=5)
        self.SuppressorCheck.deselect()

         # tubular magazine Options
        self.TubularMagType = tk.StringVar()

        self.radTubularMagType1 = tk.Radiobutton(self, text="Stock", \
                                           variable=self.TubularMagType, value='Stock', \
                                           command= lambda : self.Calc_Values())
        self.radTubularMagType1.grid(in_=self.OptionsInfo, column=2, row=1, sticky=tk.W, \
                               padx=5, pady=5)
        self.radTubularMagType1.configure(state='disabled')

        self.radTubularMagType2 = tk.Radiobutton(self, text="Underbarrel", \
                                           variable=self.TubularMagType, value='Barrel', \
                                           command= lambda: self.Calc_Values())
        self.radTubularMagType2.grid(in_=self.OptionsInfo, column=2, row=2, sticky=tk.W, \
                               padx=5, pady=5)            
        self.radTubularMagType2.configure(state='disabled')
        self.radTubularMagType2.select()

        # Adding a Combo box widget for flash supressors
        self.FlashSuppressor = tk.StringVar()
        self.FlashSuppressorBox = ttk.Combobox(self, width=24, textvariable=self.FlashSuppressor,\
                                          state='readonly')
        self.FlashSuppressorBox['values'] = ('None', 'Flash Suppressor',\
                                        'Long Flash Suppressor')
        self.FlashSuppressorBox.grid(in_=self.OptionsInfo, column=3, row=3, padx=5, pady=5)
        self.FlashSuppressorBox.current(0)
        self.FlashSuppressorBox.bind ('<<ComboboxSelected>>', lambda event: self.Calc_Values() )


        # rotary weapon option

        self.RotaryWeapon = tk.IntVar()
        self.RotaryWeaponCheck = tk.Checkbutton(self, text="Rotary Weapon", \
                                           variable=self.RotaryWeapon , \
                                           command= lambda: self.Rotary_Weapon_Checks())
        self.RotaryWeaponCheck.grid(in_=self.OptionsInfo, column=2, row=4, sticky=tk.W, \
                               padx=5, pady=5)
        self.RotaryWeaponCheck.deselect()


        # Adding a Textbox Entry widget for rotary barrels
        self.RotaryBarrels = tk.StringVar(self, value="1")
        self.RotaryBarrelsBox = ttk.Entry(self, width=15,\
                                                 textvariable=self.RotaryBarrels)
        self.RotaryBarrelsBox.grid (in_=self.OptionsInfo, column=2, row=5, padx=5, pady=5)
        self.RotaryBarrelsBox.bind ('<KeyRelease>', lambda event: self.Rotary_Weapon_Checks() )
        self.RotaryBarrelsBox.config (state='disabled')


#======================
# Design output Frame
#======================


        self.DesignInfo = ttk.LabelFrame(self, text="Design Statistics")
        self.DesignInfo.grid(column=2, row=0, sticky= "NWES",\
                             padx=5, pady=5, rowspan =2)


        #======================
        # Labels
        #======================



        #======================
        # widgets
        #======================


        # Adding a Textbox widget for Final Design
        self.FinalDesignBox = tk.Text(self, width=108, height=38)
        self.FinalDesignBox.grid(in_=self.DesignInfo, column=0, row=1, \
                                 sticky= "NWES", padx=5, pady=5)


#======================
# Errors Frame
#======================


        self.ErrorsInfo = ttk.LabelFrame(self, text="Design Errors")
        self.ErrorsInfo.grid(column=2, row=2, sticky= "NWES", \
                             padx=5, pady=5,)


        #======================
        # Labels
        #======================


        # Cylinder magazine size warning label
        self.CylinderMagMaxRoundsError_label = ttk.Label\
                               (self)
        # tubular magazine size warning label
        self.TubularMagMaxRoundsError_label = ttk.Label\
                               (self)

        # Grip magazine case type warning label
        self.GripMagCaseTypeError_label = ttk.Label\
                               (self, \
                                text="Straight cased rounds only")

        # Grip magazine size warning label
        self.GripMagMaxRoundsError_label = ttk.Label\
                               (self)

        # Grip magazine Length warning label
        self.GripMagLengthError_label = ttk.Label\
                               (self, \
                                text="Rounds too long for grip magazine use box magazine instead" )


        # Max Ammo diameter warning label
        self.MaxAmmoDiameterError_label = ttk.Label\
                               (self,text="Maximum ammo diameter 20mm" )
        
        # Box magazine size warning label
        self.BoxMagCapError_label = ttk.Label\
                               (self)

        # Sight Type warning label
        self.SightTypeError_label = ttk.Label\
                               (self, text="Can not fit that type of sight to a one handed weapon")

        # Sight Tech Type warning label
        self.SightTechTypeError_label = ttk.Label\
                               (self, text="Your tech level is too low to fit that sight")

        # Recoil Absorber Tech Type warning label
        self.RecoilAbsorbTechTypeError_label = ttk.Label\
                               (self, text="Your tech level is too low to fit that recoil absorber")

        # Recoil compensator Tech Type warning label
        self.RecoilCompTechTypeError_label = ttk.Label\
                               (self, text="Your tech level is too low to fit that recoil compmensator")

        # muzzle brake Type warning label
        self.RecoilBrakeTechTypeError_label = ttk.Label\
                               (self, text="Your tech level is too low to fit that muzzle brake")



        # Box mag max Length warning label
        self.BoxMagLengthError_label = ttk.Label\
                               (self,text="Receiver Length too short for a box magazine" )

        # Clip mag max Length warning label
        self.ClipMagLengthError_label = ttk.Label\
                               (self,text="Receiver Length too short for a clip feed" )

        # shotgun bullets warning label
        self.ShotgunBulletsError_label = ttk.Label\
                               (self,text="Number of bullets must be divisable by 4" )

        # flechette dart warning label
        self.FlechetteDartError_label = ttk.Label\
                               (self,text="Number of darts must be divisable by 4" )

        # barrel type warning label
        self.BarrelTypeError_label = ttk.Label\
                               (self,text="This design require a heavy barrel" )

        # belt type warning label
        self.BeltTypeError_label = ttk.Label\
                               (self,text="This belt feeds require a heavy receiver" )

        #======================
        # widgets
        #======================

    def on_show_frame(self, event):
        self.controller.currentpage = "SmallArms"

    def Shotgun_Checks(self):

        #disables shotgun ammo for non shotguns
        self.Calc_Values()
        if  self.WeaponTypeVar == "Shotgun":
            self.CaseTypeVar.set("Shotgun")
            self.SmallArmsShotgunBullets.configure(state='normal')
            self.radCaseType1.configure(state='disabled')
            self.radCaseType2.configure(state='disabled')
        else:
            self.SmallArmsShotgunBullets.configure(state='disabled')
            self.radCaseType1.configure(state='normal')
            self.radCaseType2.configure(state='normal')
            self.CaseTypeVar.set("blank")

    def Receiver_Checks(self):

        #selects only valid inputs for ROF depending on receiver type
        if self.RecieverTypeVar == "Individully Loadng":
            self.RateofFireBox['values'] = ('SS')
            self.RateofFireBox.current(0)
            self.RateofFire.set('SS')
        elif self.RecieverTypeVar == "Lever Action":
            self.RateofFireBox['values'] = ('LA')
            self.RateofFireBox.current(0)
            self.RateofFire.set('LA')
        elif self.RecieverTypeVar == "Bolt action":
            self.RateofFireBox['values'] = ('BA')
            self.RateofFireBox.current(0)
            self.RateofFire.set('BA')
        elif self.RecieverTypeVar == "Pump action":
            self.RateofFireBox['values'] = ('PA')
            self.RateofFireBox.current(0)
            self.RateofFire.set('PA')
        elif self.RecieverTypeVar == "Revolver":
                if self.TechLevel == 3:
                    self.RateofFireBox['values'] = ('SAR')
                    self.RateofFireBox.current(0)
                    self.RateofFire.set('SAR')
                else:
                    self.RateofFireBox['values'] = ('DAR')
                    self.RateofFireBox.current(0)
                    self.RateofFire.set('DAR')
        else:
            self.RateofFireBox['values'] = ('SA', '3', '5', '10',\
                                              '3/5', '5/10', '3/5/10')
            self.RateofFireBox.current(0)
            self.RateofFire.set('SA')
        self.Calc_Values()

    def Rotary_Weapon_Checks(self):
        # set options for rotary barrel weapons and removes invalid choices.
        lambda event: Check_Is_Not_Empty(self, "RotaryBarrels")
        if self.RotaryWeapon == 1:
            self.RotaryBarrelsBox.configure(state='normal')
            self.ROF_Rotary = int((self.RotaryBarrels - 1)*10)
            self.RateofFireBox['values'] = (self.ROF_Rotary)
            self.RateofFireBox.current(0)
            self.RateofFireBox.configure(state='disabled')
            self.RecieverBox['values'] = ('Heavy self-loading',)
            self.RecieverBox.current(0)
            self.RecieverTypeVar = "Heavy self-loading"
            self.RecieverBox.configure(state='disabled')
            self.radBarrelType2.select()
            self.BarrelTypeVar = "Heavy"
            self.radBarrelType1.configure(state='disabled')
            self.radBarrelType2.configure(state='disabled')
            self.MagazineTypeBox['values'] = ('Belt', 'Cassette')
            if self.MagazineType != 'Cassette':
                self.MagazineTypeBox.current(0)

        else:
            self.RateofFireBox.configure(state='normal')
            self.RotaryBarrelsBox.configure(state='disabled')
            self.RecieverBox.configure(state='normal')
            self.radBarrelType1.configure(state='normal')
            self.radBarrelType2.configure(state='normal')
            self.RecieverBox['values'] = ('Individully Loadng', 'Revolver', 'Lever Action',\
                                        'Bolt action', 'Pump action', 'Heavy self-loading',\
                                        'Light self-loading')
            self.Receiver_Checks()


    def Design_Error_Checks(self):

        #disables recoil comps for pistol weapons

        if self.WeaponTypeVar == "Pistol":
            self.RecoilCompBox.configure(state='disabled')
            self.RecoilAbsorbBox.configure(state='disabled')
        else:
            self.RecoilCompBox.configure(state='readonly')
            self.RecoilAbsorbBox.configure(state='readonly')

        #disables ETC primer until TL9+

        if self.TechLevel.get() >= 9:
            self.radAmmoType2.configure(state='normal')
        else:
            self.AmmoTypeVar.set("Standard")
            self.radAmmoType2.configure(state='disabled')

        #sets mag choices for ETC

        if self.AmmoTypeVar == "ETC":
            self.MagazineTypeBox['values'] = ('Belt', 'Grip Magazine', \
                                                  'Box Magazine', 'Cassette')
        else:
            self.MagazineTypeBox['values'] = ('Breach Loaded', 'Cylinder', 'Belt', \
                                          'Grip Magazine', 'Clip', 'Tubular magazine', \
                                          'Box Magazine', 'Cassette')


        #disables necked cartriges at TL 3

        if self.TechLevel.get() == 3:
            self.CaseTypeVar.set("Straight")
            self.radCaseType2.configure(state='disabled')
        else:
            self.radCaseType2.configure(state='normal')

        #disables tubular mag options until selected

        if self.MagazineType =="Tubular magazine":
            self.CaseTypeVar.set("Barrel")
            self.radTubularMagType1.configure(state='normal')
            self.radTubularMagType2.configure(state='normal')
        else:
            self.radTubularMagType1.configure(state='disabled')
            self.radTubularMagType2.configure(state='disabled')


        # max ammo diameter   

        if  SmallArmsCalcs.AmmoDiameter > 20.0:
            self.MaxAmmoDiameterError_label.grid(in_=self.ErrorsInfo, column=0, \
                                    sticky= "W", padx=5, pady=5)
        else:
            self.MaxAmmoDiameterError_label.grid_forget()

        #excess rounds in cylinder mag warning

        selfCylinderMagazineCap= round(19/(math.sqrt(SmallArmsCalcs.AmmoDiameter)),0)

        if (self.MagazineType =="Cylinder") and \
            (SmallArmsCalcs.MagazineCap > CylinderMagazineCap):
            self.CylinderMagMaxRoundsError_label.configure(text=\
                                                        "Too many rounds in cylinder"\
                                                        " magazine max rounds equals "\
                                                +str(int(self.CylinderMagazineCap))) 
            self.CylinderMagMaxRoundsError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
        else:
            self.CylinderMagMaxRoundsError_label.grid_forget()

        # Tubular magazine options

        # stock mounted mag
        if self.TubularMagType == "Stock":
            self.TubularMagazineCap = round\
                                 ((SmallArmsCalcs.StockLength/\
                                   (SmallArmsCalcs.AmmoLength/10)),0)
        else: # underbarrel mounted mag
            self.TubularMagazineCap = round\
                            ((SmallArmsCalcs.BarrelLength/\
                              (SmallArmsCalcs.AmmoLength/10)),0)

        if (self.MagazineType =="Tubular magazine") and \
            (SmallArmsCalcs.MagazineCap > self.TubularMagazineCap):
            self.TubularMagMaxRoundsError_label.configure(text=\
                                                        "Too many rounds in tubular"\
                                                        " magazine max rounds equals "\
                                                +str(int(self.TubularMagazineCap))) 
            self.TubularMagMaxRoundsError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
        else:
            self.TubularMagMaxRoundsError_label.grid_forget()

        # necked case type with grip mag

        if (self.MagazineType =="Grip Magazine") and \
            (self.CaseTypeVar =="Necked"):
            self.GripMagCaseTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
        else:
            self.GripMagCaseTypeError_label.grid_forget()

        #excess rounds in grip mag warning

        if self.AmmoTypeVar == "ETC":
            if self.TechLevel.get() <=4:
                GripMagazineCap= 80/(SmallArmsCalcs.AmmoDiameter+1)
            elif self.TechLevel.get() <=6:
                GripMagazineCap= 100/(SmallArmsCalcs.AmmoDiameter+1)
            elif self.TechLevel.get() ==7:
                GripMagazineCap= 120/(SmallArmsCalcs.AmmoDiameter+1)
            else: # tech lveel 8+
                GripMagazineCap= 140/(SmallArmsCalcs.AmmoDiameter+1)
        else: # standard primer rounds
            if self.TechLevel.get() <=4:
                GripMagazineCap= 80/SmallArmsCalcs.AmmoDiameter
            elif self.TechLevel.get() <=6:
                GripMagazineCap= 100/SmallArmsCalcs.AmmoDiameter
            elif self.TechLevel.get() ==7:
                GripMagazineCap= 120/SmallArmsCalcs.AmmoDiameter
            else: # tech lveel 8+
                GripMagazineCap = 140/SmallArmsCalcs.AmmoDiameter


        if (self.MagazineType =="Grip Magazine") and \
            (SmallArmsCalcs.MagazineCap > self.GripMagazineCap):
            self.GripMagMaxRoundsError_label.configure(text=\
                                                        "Too many rounds in grip"\
                                                        " magazine max rounds equals "\
                                                +str(int(self.GripMagazineCap)))
            self.GripMagMaxRoundsError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
        else:
            self.GripMagMaxRoundsError_label.grid_forget()

        # rounds too long for grip magazines

        if self.TechLevel.get() <=4:
            MaxAmmoLength = 30
        elif self.TechLevel.get() <=6:
            MaxAmmoLength = 40
        elif self.TechLevel.get() ==7:
            MaxAmmoLength = 50
        else: # tech level 8+
            MaxAmmoLength = 60

        if (self.MagazineType =="Grip Magazine") and \
            (SmallArmsCalcs.AmmoLength > MaxAmmoLength):
            self.GripMagLengthError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
        else:
            self.GripMagLengthError_label.grid_forget()

        # max rounds for box magazines

        if (self.MagazineType == "Box Magazine"):
            if (SmallArmsCalcs.MagazineCap > 100) and \
                (SmallArmsCalcs.AmmoWeight > 15):
                self.BoxMagCapError_label.configure(text="Max capacity 100 rounds")
                self.BoxMagCapError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
            elif (SmallArmsCalcs.MagazineCap > 200) and \
                    (SmallArmsCalcs.AmmoWeight < 15):
                self.BoxMagCapError_label.configure(text="Max capacity 200 rounds")
                self.BoxMagCapError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
            else:
                self.BoxMagCapError_label.grid_forget()
        else:
            self.BoxMagCapError_label.grid_forget()

        #reciver too short for box mag warnings
        if (self.MagazineType == "Box Magazine"):
            if (SmallArmsCalcs.AmmoLength+150) >(SmallArmsCalcs.RecieverLength*10):
                self.BoxMagLengthError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
            else:
                self.BoxMagLengthError_label.grid_forget()
        else:
            self.BoxMagLengthError_label.grid_forget()

        #reciver too short for clip mag warnings
        if (self.MagazineType == "Clip"):
            if (SmallArmsCalcs.AmmoLength+150) >(SmallArmsCalcs.RecieverLength*10):
                self.ClipMagLengthError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
            else:
                self.ClipMagLengthError_label.grid_forget()

        #wrong sight types warnings

        if ((self.SightType == "Telescopic sights") or\
            (self.SightType == "Electronic sights")) and  \
            self.WeaponTypeVar == "Pistol":
            self.SightTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
        else:
            self.SightTypeError_label.grid_forget()

        #Sight tech level types warnings

        if (self.LaserSight == 1) and (self.TechLevel.get() < 7):
            self.SightTechTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
        elif (self.SightType == "Optic sights") and (self.TechLevel.get() < 8):
            self.SightTechTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
        elif (self.SightType == "Telescopic sights") and (self.TechLevel.get() < 6):
            self.SightTechTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
        elif (self.SightType == "Electronic sights") and (self.TechLevel.get() < 9):
            self.SightTechTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
        else:
            self.SightTechTypeError_label.grid_forget()

        # recoil compenator warnings
            
        if (self.RecoilAbsorb == "SA stock") and (self.TechLevel.get < 5):
            self.RecoilAbsorbTechTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
        elif (self.RecoilAbsorb == "Folding SA stock") and (self.TechLevel.get() < 9):
            self.RecoilAbsorbTechTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
        else:
            self.RecoilAbsorbTechTypeError_label.grid_forget()

        if (self.RecoilComp == "Gyroscopic Compensator") and (self.TechLevel.get() < 10):
            self.RecoilCompTechTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
        elif (self.RecoilComp == "Inertial Compensator") and (self.TechLevel.get() < 14):
            self.RecoilCompTechTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
        else:
            self.RecoilCompTechTypeError_label.grid_forget()

        if (self.RecoilBrake == "Muzzle Brake") and (self.TechLevel.get() < 6):
            self.RecoilBrakeTechTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
        elif (self.RecoilBrake == "Long Muzzle Brake") and (self.TechLevel.get() < 7):
            self.RecoilBrakeTechTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
        else:
            self.RecoilBrakeTechTypeError_label.grid_forget()

        # shotgun bullets not divisable by 4

        if (SmallArmsCalcs.ShotgunBullets%4) != 0:
            self.ShotgunBulletsError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
        else:
            self.ShotgunBulletsError_label.grid_forget()

        # flechette darts not divisable by 4

        if (SmallArmsCalcs.FlechetteDarts%4) != 0:
            self.FlechetteDartError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
        else:
            self.FlechetteDartError_label.grid_forget()


        # light or heavy barrel

        if (SmallArmsCalcs.AverageMuzzleEnergy >= 5000) or (self.MountType == "Bipod")\
            or (self.MountType == "Tripod") or \
            (self.RecieverTypeVar == "Heavy self-loading") \
            and (self.BarrelTypeVar != "Heavy"):
            self.BarrelTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)      
        else:
            self.BarrelTypeError_label.grid_forget()


        #Belt feed check
        if (self.MagazineType =="Belt") and \
            (self.RecieverTypeVar != "Heavy self-loading"):
            self.BeltTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                sticky= "W", padx=5, pady=5)
        else:
            self.BeltTypeError_label.grid_forget()

    def WidgetValues(self):
        WidgetValues = []
        WidgetValues.append(self.TechLevel.get())
        WidgetValues.append(self.WeaponName.get())
        WidgetValues.append(self.AmmoDiameter.get())
        WidgetValues.append(self.CartridgeLength.get())
        WidgetValues.append(self.ShotgunBullets.get())
        WidgetValues.append(self.FlechetteDarts.get())
        WidgetValues.append(self.AmmoTypeVar.get())
        WidgetValues.append(self.CaseTypeVar.get())
        WidgetValues.append(self.ProdTypeVar.get())
        WidgetValues.append(self.BarrelLengthModVar.get())
        WidgetValues.append(self.RiflingTypeVar.get())
        WidgetValues.append(self.BarrelTypeVar.get())
        WidgetValues.append(self.RecieverTypeVar.get())
        WidgetValues.append(self.RateofFire.get())
        WidgetValues.append(self.MagazineCap.get())
        WidgetValues.append(self.StockType.get())
        WidgetValues.append(self.MountType.get())
        WidgetValues.append(self.MagazineType.get())
        WidgetValues.append(self.SightType.get())
        WidgetValues.append(self.RecoilAbsorb.get())
        WidgetValues.append(self.RecoilComp.get())
        WidgetValues.append(self.RecoilBrake.get())
        WidgetValues.append(self.BayonetLug.get())
        WidgetValues.append(self.Grenade.get())
        WidgetValues.append(self.Silenced.get())
        WidgetValues.append(self.WeaponTypeVar.get())
        WidgetValues.append(self.TubularMagType.get())
        WidgetValues.append(self.LaserSight.get())
        WidgetValues.append(self.Suppressor.get())
        WidgetValues.append(self.FlashSuppressor.get())
        WidgetValues.append(self.RotaryWeapon.get())
        WidgetValues.append(self.RotaryBarrels.get())

        return WidgetValues


    def Calc_Values(self):
        WidgetValues = self.WidgetValues()
        SmallArmsCalcs (WidgetValues)
        self.Design_Error_Checks ()
        self.FinalDesignBox.delete('1.0', 'end')
        self.FinalDesignBox.insert('1.0', SmallArmsCalcs.FinalDesign)       


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

        c.execute ('''CREATE TABLE IF NOT EXISTS SmallArms ("id" INTEGER PRIMARY KEY,
                        "name" TEXT, "WidgetValues" TEXT, "VehicleValues" TEXT)
                        ''')
        # insert save data into table
        sql = '''INSERT INTO SmallArms (name, WidgetValues, VehicleValues)
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
        
        rows = c.execute ('SELECT name FROM SmallArms').fetchall()

        Load_Window(rows)

        Choice = Load_Window.Load_Choice


        SavedData = c.execute ('SELECT WidgetValues FROM SmallArms WHERE name =?',\
                                            (Choice,)).fetchall()

        WidgetValuesJoined = SavedData[0]
        WidgetLoadedValues = WidgetValuesJoined.split(",")
        

        page_smallarms = self.controller.get_page("SmallArms") 
        page_smallarms.TechLevel.set(WidgetLoadedValues[0])
        page_smallarms.WeaponName.set(WidgetLoadedValues[1])
        page_smallarms.AmmoDiameter.set(WidgetLoadedValues[2])
        page_smallarms.CartridgeLength.set(WidgetLoadedValues[3])
        page_smallarms.ShotgunBullets.set(WidgetLoadedValues[4])
        page_smallarms.FlechetteDarts.set(WidgetLoadedValues[5])
        page_smallarms.AmmoTypeVar.set(WidgetLoadedValues[6])
        page_smallarms.CaseTypeVar.set(WidgetLoadedValues[7])
        page_smallarms.ProdTypeVar.set(WidgetLoadedValues[8])
        page_smallarms.BarrelLengthModVar.set(WidgetLoadedValues[9])
        page_smallarms.RiflingTypeVar.set(WidgetLoadedValues[10])
        page_smallarms.BarrelTypeVar.set(WidgetLoadedValues[11])
        page_smallarms.RecieverTypeVar.set(WidgetLoadedValues[12])
        page_smallarms.RateofFire.set(WidgetLoadedValues[13])
        page_smallarms.MagazineCap.set(WidgetLoadedValues[14])
        page_smallarms.StockType.set(WidgetLoadedValues[15])
        page_smallarms.MountType.set(WidgetLoadedValues[16])
        page_smallarms.MagazineType.set(WidgetLoadedValues[17])
        page_smallarms.SightType.set(WidgetLoadedValues[18])
        page_smallarms.RecoilAbsorb.set(WidgetLoadedValues[19])
        page_smallarms.RecoilComp.set(WidgetLoadedValues[20])
        page_smallarms.RecoilBrake.set(WidgetLoadedValues[21])
        page_smallarms.BayonetLug.set(WidgetLoadedValues[22])
        page_smallarms.Grenade.set(WidgetLoadedValues[23])
        page_smallarms.Silenced.set(WidgetLoadedValues[24])
        page_smallarms.WeaponTypeVar.set(WidgetLoadedValues[25])
        page_smallarms.TubularMagType.set(WidgetLoadedValues[26])
        page_smallarms.LaserSight.set(WidgetLoadedValues[27])
        page_smallarms.Suppressor.set(WidgetLoadedValues[28])
        page_smallarms.FlashSuppressor.set(WidgetLoadedValues[29])
        page_smallarms.RotaryWeapon.set(WidgetLoadedValues[30])
        page_smallarms.RotaryBarrels.set(WidgetLoadedValues[31])
        self.Calc_Values()
