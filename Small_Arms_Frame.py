# contents of Small arms frame
import tkinter as tk
from tkinter import ttk
import math

#======================
# GUI Frame Class
#======================


class Small_Arms (ttk.Frame):
    TechLevel = int()
    WeaponName = str()
    AmmoDiameter = str()
    ShotgunBullets = int()
    FlechetteDarts = int()
    CartridgeLength = str()
    AmmoTypeVar = str()
    CaseTypeVar = str()
    ProdTypeVar = str()
    BarrelLengthModVar =float()
    RiflingTypeVar = str()
    BarrelTypeVar = str()
    RecieverTypeVar = str()
    RateofFire = str()
    MagazineCap = str()
    StockType = str()
    MountType = str()
    MagazineType = str()
    SightType =str()
    RecoilAbsorb = str()
    RecoilComp = str()
    RecoilBrake = str()
    BayonetLug = int()
    Grenade = int()
    Silenced = int()
    WeaponTypeVar =str()
    TubularMagType = str()
    LaserSight = int()
    Suppressor = int()
    FlashSuppressor = str()
    RotaryWeapon = int()
    RotaryBarrels = str()
    
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)


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
                                 lambda event: Check_Is_Not_Empty(self, "WeaponName") ) 

        # Adding a Combo box widget for Tech Level
        self.TechLevel = tk.IntVar()
        self.TechLevelBox = ttk.Combobox(self, width=12, textvariable=self.TechLevel,\
                                         state='readonly')
        self.TechLevelBox['values'] = (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, \
                                       15, 16, 17, 18, 19, 20, 21)
        self.TechLevelBox.grid(in_=self.CommonInfo, column=1, row=2, padx=5, pady=5)
        self.TechLevelBox.current(0)
        self.TechLevelBox.bind ('<<ComboboxSelected>>', lambda event: Receiver_Checks() )

         # Weapon type raido button
        self.WeaponTypeVar = tk.StringVar(value="1")

        self.radWeaponType1 = tk.Radiobutton(self, text="Pistol", \
                                           variable=self.WeaponTypeVar, value="Pistol", \
                                           command= lambda: Shotgun_Checks())
        self.radWeaponType1.grid(in_=self.CommonInfo, column=0, row=3, sticky=tk.W, \
                               padx=5, pady=5)
        
        self.radWeaponType2 = tk.Radiobutton(self, text="Longarm - needs two hands", \
                                           variable=self.WeaponTypeVar, value="Longarm", \
                                           command= lambda: Shotgun_Checks())
        self.radWeaponType2.grid(in_=self.CommonInfo, column=1, row=3, sticky=tk.W, \
                               padx=5, pady=5)

        self.radWeaponType3 = tk.Radiobutton(self, text="Shotgun", \
                                           variable=self.WeaponTypeVar, value="Shotgun", \
                                           command= lambda: Shotgun_Checks())
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
                                 lambda event: Check_Is_Not_Empty(self, "AmmoDiameter") ) 

        # Adding a Textbox Entry widget for Cartridge Length
        self.CartridgeLength = tk.StringVar(self, value="9")
        self.SmallArmsCartridgeLength = ttk.Entry(self, width=15,\
                                                 textvariable=self.CartridgeLength)
        self.SmallArmsCartridgeLength.grid (in_=self.AmmoInfo, column=1, row=2, padx=5, pady=5)
        self.SmallArmsCartridgeLength.bind ('<KeyRelease>',\
                                 lambda event: Check_Is_Not_Empty(self, "CartridgeLength") ) 

        # Adding a Textbox Entry widget for Shotgun Bullets
        self.ShotgunBullets = tk.StringVar(self, value="4")
        self.SmallArmsShotgunBullets = ttk.Entry(self, width=15,\
                                                 textvariable=self.ShotgunBullets)
        self.SmallArmsShotgunBullets.grid (in_=self.AmmoInfo, column=1, row=3, padx=5, pady=5)
        self.SmallArmsShotgunBullets.bind ('<KeyRelease>',\
                                 lambda event: Check_Is_Not_Empty(self, "ShotgunBullets") ) 
        self.SmallArmsShotgunBullets.configure(state='disabled')


        # Adding a Textbox Entry widget for Flechette darts
        self.FlechetteDarts = tk.StringVar(self, value="4")
        self.SmallArmsFlechetteDarts = ttk.Entry(self, width=15,\
                                                 textvariable=self.FlechetteDarts)
        self.SmallArmsFlechetteDarts.grid (in_=self.AmmoInfo, column=1, row=4, padx=5, pady=5)
        self.SmallArmsFlechetteDarts.bind ('<KeyRelease>',\
                                 lambda event: Check_Is_Not_Empty(self, "FlechetteDarts") ) 

        # Ammo type standard or ETC
        self.AmmoTypeVar = tk.StringVar()

        self.radAmmoType1 = tk.Radiobutton(self, text="Standard", \
                                           variable=self.AmmoTypeVar, value="Standard", \
                                           command= lambda : Set_Outputs())
        self.radAmmoType1.grid(in_=self.AmmoInfo, column=0, row=6, sticky=tk.W, \
                               padx=5, pady=5)
        self.radAmmoType1.select()

        self.radAmmoType2 = tk.Radiobutton(self, text="Electrothermal-chemical", \
                                           variable=self.AmmoTypeVar, value="ETC", \
                                           command= lambda: Set_Outputs())
        self.radAmmoType2.configure(state='disabled')
        self.radAmmoType2.grid(in_=self.AmmoInfo, column=1, row=6, sticky=tk.W, \
                               padx=5, pady=5)


        # case type necked or straight
        self.CaseTypeVar = tk.StringVar()

        self.radCaseType1 = tk.Radiobutton(self, text="Straight", \
                                           variable=self.CaseTypeVar, value="Straight", \
                                           command= lambda : Set_Outputs())
        self.radCaseType1.grid(in_=self.AmmoInfo, column=0, row=8, sticky=tk.W, \
                               padx=5, pady=5)
        self.radCaseType1.select()

        self.radCaseType2 = tk.Radiobutton(self, text="Necked", \
                                           variable=self.CaseTypeVar, value="Necked", \
                                           command= lambda: Set_Outputs())
        self.radCaseType2.configure(state='disabled')
        self.radCaseType2.grid(in_=self.AmmoInfo, column=1, row=8, sticky=tk.W, \
                               padx=5, pady=5)

        # production type mass produced military or conventional
        self.ProdTypeVar = tk.StringVar()

        self.radProdType1 = tk.Radiobutton(self, text="Mass produced military", \
                                           variable=self.ProdTypeVar, value="Military", \
                                           command= lambda : Set_Outputs())
        self.radProdType1.grid(in_=self.AmmoInfo, column=0, row=10, sticky=tk.W, \
                               padx=5, pady=5)
        self.radProdType1.select()

        self.radProdType2 = tk.Radiobutton(self, text="Conventional", \
                                           variable=self.ProdTypeVar, value="onventional", \
                                           command= lambda: Set_Outputs())
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
        self.BarrelLengthMod.bind ('<ButtonRelease-1>', lambda event: Set_Outputs() )

        # Rifling type smoothbore or rifled
        self.RiflingTypeVar = tk.StringVar()

        self.radRiflingType1 = tk.Radiobutton(self, text="Smoothbore", \
                                           variable=self.RiflingTypeVar, value="Smoothbore", \
                                           command= lambda : Set_Outputs())
        self.radRiflingType1.grid(in_=self.WeaponInfo, column=0, row=2, sticky=tk.W, \
                               padx=5, pady=5)
        self.radRiflingType1.select()

        self.radRiflingType2 = tk.Radiobutton(self, text="Rifled", \
                                           variable=self.RiflingTypeVar, value="Rifled", \
                                           command= lambda: Set_Outputs())
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
                                           command= lambda: Set_Outputs())
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
        self.RecieverBox.bind ('<<ComboboxSelected>>', lambda event: Receiver_Checks() )

        # Adding a Combo box widget for Rate of Fire
        self.RateofFire = tk.StringVar()
        self.RateofFireBox = ttk.Combobox(self, width=12, textvariable=self.RateofFire,\
                                          state='readonly')
        self.RateofFireBox['values'] = ('SS')
        self.RateofFireBox.grid(in_=self.WeaponInfo, column=1, row=6, padx=5, pady=5)
        self.RateofFireBox.current(0)
        self.RateofFireBox.bind ('<<ComboboxSelected>>', lambda event: Set_Outputs() )

        # Adding a Textbox Entry widget for Magazine Capacity
        self.MagazineCap = tk.StringVar(self, value="10")
        self.MagazineCapacity = ttk.Entry(self, width=15, textvariable=self.MagazineCap)
        self.MagazineCapacity.grid(in_=self.WeaponInfo, column=1, row=7, padx=5, pady=5)
        self.MagazineCapacity.bind ('<KeyRelease>',\
                                 lambda event: Check_Is_Not_Empty(self, "MagazineCap") )

        # Adding a Combo box widget for magazine type
        self.MagazineType = tk.StringVar()
        self.MagazineTypeBox = ttk.Combobox(self, textvariable=self.MagazineType\
                                            , state='readonly')
        self.MagazineTypeBox['values'] = ('Breach Loaded', 'Cylinder', 'Belt', \
                                          'Grip Magazine', 'Clip', 'Tubular magazine', \
                                          'Box Magazine', 'Cassette')
        self.MagazineTypeBox.grid(in_=self.WeaponInfo, column=1, row=8, padx=5, pady=5)
        self.MagazineTypeBox.current(0)
        self.MagazineTypeBox.bind ('<<ComboboxSelected>>', lambda event: Rotary_Weapon_Checks() )

        # Adding a Combo box widget for Stock type
        self.StockType = tk.StringVar()
        self.StockTypeBox = ttk.Combobox(self, textvariable=self.StockType,\
                                         state='readonly')
        self.StockTypeBox['values'] = ('Wood pistol grip', 'Hollow pistol grip', 'Wooden stock',\
                                       'Carbine stock', 'Folding stock',\
                                       'Plastic stock', 'Bullpup')
        self.StockTypeBox.grid(in_=self.WeaponInfo, column=1, row=9, padx=5, pady=5)
        self.StockTypeBox.current(0)
        self.StockTypeBox.bind ('<<ComboboxSelected>>', lambda event: Set_Outputs() )

        # Adding a Combo box widget for Sights
        self.SightType = tk.StringVar()
        self.SightTypeBox = ttk.Combobox(self, textvariable=self.SightType\
                                         ,state='readonly')
        self.SightTypeBox['values'] = ('Iron sights', 'Optic sights', 'Telescopic sights',\
                                       'Electronic sights')
        self.SightTypeBox.grid(in_=self.WeaponInfo, column=1, row=10, padx=5, pady=5)
        self.SightTypeBox.current(0)
        self.SightTypeBox.bind ('<<ComboboxSelected>>', lambda event: Set_Outputs() )


        # lasersights option option

        self.LaserSight = tk.IntVar()
        self.LaserSightCheck = tk.Checkbutton(self, text="Laser Sight", \
                                           variable=self.LaserSight, \
                                           command= lambda: Set_Outputs())
        self.LaserSightCheck.grid(in_=self.WeaponInfo, column=1, row=11, sticky=tk.W, \
                               padx=5, pady=5)
        self.LaserSightCheck.deselect()

        # Adding a Combo box widget for Recoil shock abosorber
        self.RecoilAbsorb = tk.StringVar()
        self.RecoilAbsorbBox = ttk.Combobox(self, textvariable=self.RecoilAbsorb)
        self.RecoilAbsorbBox['values'] = ('None', 'Folding SA stock', 'SA stock')
        self.RecoilAbsorbBox.grid(in_=self.WeaponInfo, column=1, row=12, padx=5, pady=5)
        self.RecoilAbsorbBox.current(0)
        self.RecoilAbsorbBox.bind ('<<ComboboxSelected>>', lambda event: Set_Outputs() )

        # Adding a Combo box widget for Recoil Compenators
        self.RecoilComp = tk.StringVar()
        self.RecoilCompBox = ttk.Combobox(self, width=24, textvariable=self.RecoilComp,\
                                          state='readonly')
        self.RecoilCompBox['values'] = ('None', 'Gyroscopic Compensator',\
                                        'Inertial Compensator')
        self.RecoilCompBox.grid(in_=self.WeaponInfo, column=1, row=13, padx=5, pady=5)
        self.RecoilCompBox.current(0)
        self.RecoilCompBox.bind ('<<ComboboxSelected>>', lambda event: Set_Outputs() )

        # Adding a Combo box widget for Muzzle brakes
        self.RecoilBrake = tk.StringVar()
        self.RecoilBrakeBox = ttk.Combobox(self, width=24, textvariable=self.RecoilBrake,\
                                          state='readonly')
        self.RecoilBrakeBox['values'] = ('None', 'Muzzle Brake',\
                                        'Long Muzzle Brake')
        self.RecoilBrakeBox.grid(in_=self.WeaponInfo, column=1, row=14, padx=5, pady=5)
        self.RecoilBrakeBox.current(0)
        self.RecoilBrakeBox.bind ('<<ComboboxSelected>>', lambda event: Set_Outputs() )



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
                                           command= lambda : Set_Outputs())
        self.radMountType1.grid(in_=self.OptionsInfo, column=1, row=0, sticky=tk.W, \
                               padx=5, pady=5)
        self.radMountType1.select()

        self.radMountType2 = tk.Radiobutton(self, text="Bipod", \
                                           variable=self.MountType, value='Bipod', \
                                           command= lambda: Set_Outputs())
        self.radMountType2.grid(in_=self.OptionsInfo, column=1, row=1, sticky=tk.W, \
                               padx=5, pady=5)

        self.radMountType3 = tk.Radiobutton(self, text="Tripod", \
                                           variable=self.MountType, value='Tripod', \
                                           command= lambda: Set_Outputs())
        self.radMountType3.grid(in_=self.OptionsInfo, column=1, row=2, sticky=tk.W, \
                               padx=5, pady=5)

        self.radMountType4 = tk.Radiobutton(self, text="Vehicle Mounted", \
                                           variable=self.MountType, value='Vehicle', \
                                           command= lambda: Set_Outputs())
        self.radMountType4.grid(in_=self.OptionsInfo, column=1, row=3, sticky=tk.W, \
                               padx=5, pady=5)

        # bayonet lug option
        self.BayonetLug = tk.StringVar()
        self.BayonetLugCheck = tk.Checkbutton(self, text="Bayonet Lug", \
                                           variable=self.BayonetLug, \
                                           command= lambda: Set_Outputs())
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
                                           command= lambda: Set_Outputs())
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
                                           command= lambda : Set_Outputs())
        self.radTubularMagType1.grid(in_=self.OptionsInfo, column=2, row=1, sticky=tk.W, \
                               padx=5, pady=5)
        self.radTubularMagType1.configure(state='disabled')

        self.radTubularMagType2 = tk.Radiobutton(self, text="Underbarrel", \
                                           variable=self.TubularMagType, value='Barrel', \
                                           command= lambda: Set_Outputs())
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
        self.FlashSuppressorBox.bind ('<<ComboboxSelected>>', lambda event: Set_Outputs() )


        # rotary weapon option

        self.RotaryWeapon = tk.IntVar()
        self.RotaryWeaponCheck = tk.Checkbutton(self, text="Rotary Weapon", \
                                           variable=self.RotaryWeapon , \
                                           command= lambda: Rotary_Weapon_Checks())
        self.RotaryWeaponCheck.grid(in_=self.OptionsInfo, column=2, row=4, sticky=tk.W, \
                               padx=5, pady=5)
        self.RotaryWeaponCheck.deselect()


        # Adding a Textbox Entry widget for rotary barrels
        self.RotaryBarrels = tk.StringVar(self, value="1")
        self.RotaryBarrelsBox = ttk.Entry(self, width=15,\
                                                 textvariable=self.RotaryBarrels)
        self.RotaryBarrelsBox.grid (in_=self.OptionsInfo, column=2, row=5, padx=5, pady=5)
        self.RotaryBarrelsBox.bind ('<KeyRelease>', lambda event: Rotary_Weapon_Checks() )
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

        def Shotgun_Checks():

            #disables shotgun ammo for non shotguns
            Set_Outputs ()
            if  Small_Arms.WeaponTypeVar == "Shotgun":
                self.CaseTypeVar.set("Shotgun")
                self.SmallArmsShotgunBullets.configure(state='normal')
                self.radCaseType1.configure(state='disabled')
                self.radCaseType2.configure(state='disabled')
            else:
                self.SmallArmsShotgunBullets.configure(state='disabled')
                self.radCaseType1.configure(state='normal')
                self.radCaseType2.configure(state='normal')
                self.CaseTypeVar.set("blank")

        def Receiver_Checks():

            #selects only valid in puts for ROF depending on receiver type
            Set_Outputs ()
            if Small_Arms.RecieverTypeVar == "Individully Loadng":
                self.RateofFireBox['values'] = ('SS')
                self.RateofFireBox.current(0)
                Small_Arms.RateofFire = 'SS'
            elif Small_Arms.RecieverTypeVar == "Lever Action":
                self.RateofFireBox['values'] = ('LA')
                self.RateofFireBox.current(0)
                Small_Arms.RateofFire = 'LA'
            elif Small_Arms.RecieverTypeVar == "Bolt action":
                self.RateofFireBox['values'] = ('BA')
                self.RateofFireBox.current(0)
                Small_Arms.RateofFire = 'BA'
            elif Small_Arms.RecieverTypeVar == "Pump action":
                self.RateofFireBox['values'] = ('PA')
                self.RateofFireBox.current(0)
                Small_Arms.RateofFire = 'PA'
            elif Small_Arms.RecieverTypeVar == "Revolver":
                    if Small_Arms.TechLevel == 3:
                        self.RateofFireBox['values'] = ('SAR')
                        self.RateofFireBox.current(0)
                        Small_Arms.RateofFire =  'SAR'
                    else:
                        self.RateofFireBox['values'] = ('DAR')
                        self.RateofFireBox.current(0)
                        Small_Arms.RateofFire =  'DAR'
            else:
                self.RateofFireBox['values'] = ('SA', '3', '5', '10',\
                                              '3/5', '5/10', '3/5/10')
                self.RateofFireBox.current(0)
                Small_Arms.RateofFire = 'SA'
            Small_Arms_Calcs ()
            Design_Error_Checks ()
            self.FinalDesignBox.delete('1.0', 'end')
            self.FinalDesignBox.insert('1.0', Small_Arms_Calcs.FinalDesign)

        def Rotary_Weapon_Checks():
            # set options for rotary barrel weapons and removes invalid choices.
            lambda event: Check_Is_Not_Empty(self, "RotaryBarrels")
            Set_Outputs ()
            if Small_Arms.RotaryWeapon == 1:
                self.RotaryBarrelsBox.configure(state='normal')
                ROF_Rotary = int((Small_Arms.RotaryBarrels - 1)*10)
                self.RateofFireBox['values'] = (ROF_Rotary)
                self.RateofFireBox.current(0)
                self.RateofFireBox.configure(state='disabled')
                self.RecieverBox['values'] = ('Heavy self-loading',)
                self.RecieverBox.current(0)
                Small_Arms.RecieverTypeVar = "Heavy self-loading"
                self.RecieverBox.configure(state='disabled')
                self.radBarrelType2.select()
                Small_Arms.BarrelTypeVar = "Heavy"
                self.radBarrelType1.configure(state='disabled')
                self.radBarrelType2.configure(state='disabled')
                self.MagazineTypeBox['values'] = ('Belt', 'Cassette')
                if Small_Arms.MagazineType != 'Cassette':
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
                Receiver_Checks()


        def Design_Error_Checks():

            #disables recoil comps for pistol weapons

            if Small_Arms.WeaponTypeVar == "Pistol":
                self.RecoilCompBox.configure(state='disabled')
                self.RecoilAbsorbBox.configure(state='disabled')
            else:
                self.RecoilCompBox.configure(state='readonly')
                self.RecoilAbsorbBox.configure(state='readonly')

            #disables ETC primer until TL9+

            if Small_Arms.TechLevel >= 9:
                self.radAmmoType2.configure(state='normal')
            else:
                self.AmmoTypeVar.set("Standard")
                self.radAmmoType2.configure(state='disabled')

            #sets mag choices for ETC

            if Small_Arms.AmmoTypeVar == "ETC":
                self.MagazineTypeBox['values'] = ('Belt', 'Grip Magazine', \
                                                  'Box Magazine', 'Cassette')
            else:
                self.MagazineTypeBox['values'] = ('Breach Loaded', 'Cylinder', 'Belt', \
                                          'Grip Magazine', 'Clip', 'Tubular magazine', \
                                          'Box Magazine', 'Cassette')


            #disables necked cartriges at TL 3

            if Small_Arms.TechLevel == 3:
                self.CaseTypeVar.set("Straight")
                self.radCaseType2.configure(state='disabled')
            else:
                self.radCaseType2.configure(state='normal')

            #disables tubular mag options until selected

            if Small_Arms.MagazineType =="Tubular magazine":
                self.CaseTypeVar.set("Barrel")
                self.radTubularMagType1.configure(state='normal')
                self.radTubularMagType2.configure(state='normal')
            else:
                self.radTubularMagType1.configure(state='disabled')
                self.radTubularMagType2.configure(state='disabled')


            # max ammo diameter   

            if  Small_Arms_Calcs.AmmoDiameter > 20.0:
                self.MaxAmmoDiameterError_label.grid(in_=self.ErrorsInfo, column=0, \
                                    sticky= "W", padx=5, pady=5)
            else:
                self.MaxAmmoDiameterError_label.grid_forget()

            #excess rounds in cylinder mag warning

            CylinderMagazineCap= round(19/(math.sqrt(Small_Arms_Calcs.AmmoDiameter)),0)

            if (Small_Arms.MagazineType =="Cylinder") and \
               (Small_Arms_Calcs.MagazineCap > CylinderMagazineCap):
                self.CylinderMagMaxRoundsError_label.configure(text=\
                                                           "Too many rounds in cylinder"\
                                                           " magazine max rounds equals "\
                                                 +str(int(CylinderMagazineCap))) 
                self.CylinderMagMaxRoundsError_label.grid(in_=self.ErrorsInfo, column=0, \
                                    sticky= "W", padx=5, pady=5)
            else:
                self.CylinderMagMaxRoundsError_label.grid_forget()

            # Tubular magazine options

            # stock mounted mag
            if Small_Arms.TubularMagType == "Stock":
                TubularMagazineCap = round\
                                 ((Small_Arms_Calcs.StockLength/(Small_Arms_Calcs.AmmoLength/10)),0)
            else: # underbarrel mounted mag
                TubularMagazineCap = round\
                                 ((Small_Arms_Calcs.BarrelLength/(Small_Arms_Calcs.AmmoLength/10)),0)

            if (Small_Arms.MagazineType =="Tubular magazine") and \
               (Small_Arms_Calcs.MagazineCap > TubularMagazineCap):
                self.TubularMagMaxRoundsError_label.configure(text=\
                                                           "Too many rounds in tubular"\
                                                           " magazine max rounds equals "\
                                                 +str(int(TubularMagazineCap))) 
                self.TubularMagMaxRoundsError_label.grid(in_=self.ErrorsInfo, column=0, \
                                    sticky= "W", padx=5, pady=5)
            else:
                self.TubularMagMaxRoundsError_label.grid_forget()

            # necked case type with grip mag

            if (Small_Arms.MagazineType =="Grip Magazine") and \
               (Small_Arms.CaseTypeVar =="Necked"):
                self.GripMagCaseTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                    sticky= "W", padx=5, pady=5)
            else:
                self.GripMagCaseTypeError_label.grid_forget()

            #excess rounds in grip mag warning

            if Small_Arms.AmmoTypeVar == "ETC":
                if Small_Arms.TechLevel <=4:
                    GripMagazineCap= 80/(Small_Arms_Calcs.AmmoDiameter+1)
                elif Small_Arms.TechLevel <=6:
                    GripMagazineCap= 100/(Small_Arms_Calcs.AmmoDiameter+1)
                elif Small_Arms.TechLevel ==7:
                    GripMagazineCap= 120/(Small_Arms_Calcs.AmmoDiameter+1)
                else: # tech lveel 8+
                    GripMagazineCap= 140/(Small_Arms_Calcs.AmmoDiameter+1)
            else: # standard primer rounds
                if Small_Arms.TechLevel <=4:
                    GripMagazineCap= 80/Small_Arms_Calcs.AmmoDiameter
                elif Small_Arms.TechLevel <=6:
                    GripMagazineCap= 100/Small_Arms_Calcs.AmmoDiameter
                elif Small_Arms.TechLevel ==7:
                    GripMagazineCap= 120/Small_Arms_Calcs.AmmoDiameter
                else: # tech lveel 8+
                    GripMagazineCap= 140/Small_Arms_Calcs.AmmoDiameter


            if (Small_Arms.MagazineType =="Grip Magazine") and \
               (Small_Arms_Calcs.MagazineCap > GripMagazineCap):
                self.GripMagMaxRoundsError_label.configure(text=\
                                                           "Too many rounds in grip"\
                                                           " magazine max rounds equals "\
                                                 +str(int(GripMagazineCap)))
                self.GripMagMaxRoundsError_label.grid(in_=self.ErrorsInfo, column=0, \
                                    sticky= "W", padx=5, pady=5)
            else:
                self.GripMagMaxRoundsError_label.grid_forget()

            # rounds too long for grip magazines

            if Small_Arms.TechLevel <=4:
                MaxAmmoLength = 30
            elif Small_Arms.TechLevel <=6:
                MaxAmmoLength = 40
            elif Small_Arms.TechLevel ==7:
                MaxAmmoLength = 50
            else: # tech lveel 8+
                MaxAmmoLength = 60

            if (Small_Arms.MagazineType =="Grip Magazine") and \
               (Small_Arms_Calcs.AmmoLength > MaxAmmoLength):
                self.GripMagLengthError_label.grid(in_=self.ErrorsInfo, column=0, \
                                    sticky= "W", padx=5, pady=5)
            else:
                self.GripMagLengthError_label.grid_forget()

            # max rounds for box magazines

            if (Small_Arms.MagazineType == "Box Magazine"):
                if (Small_Arms_Calcs.MagazineCap > 100) and \
                   (Small_Arms_Calcs.AmmoWeight > 15):
                    self.BoxMagCapError_label.configure(text="Max capacity 100 rounds")
                    self.BoxMagCapError_label.grid(in_=self.ErrorsInfo, column=0, \
                                    sticky= "W", padx=5, pady=5)
                elif (Small_Arms_Calcs.MagazineCap > 200) and \
                     (Small_Arms_Calcs.AmmoWeight < 15):
                    self.BoxMagCapError_label.configure(text="Max capacity 200 rounds")
                    self.BoxMagCapError_label.grid(in_=self.ErrorsInfo, column=0, \
                                    sticky= "W", padx=5, pady=5)
                else:
                    self.BoxMagCapError_label.grid_forget()
            else:
                self.BoxMagCapError_label.grid_forget()

            #reciver too short for box mag warnings
            if (Small_Arms.MagazineType == "Box Magazine"):
                if (Small_Arms_Calcs.AmmoLength+150) >(Small_Arms_Calcs.RecieverLength*10):
                    self.BoxMagLengthError_label.grid(in_=self.ErrorsInfo, column=0, \
                                    sticky= "W", padx=5, pady=5)
                else:
                    self.BoxMagLengthError_label.grid_forget()
            else:
                self.BoxMagLengthError_label.grid_forget()

            #reciver too short for clip mag warnings
            if (Small_Arms.MagazineType == "Clip"):
                if (Small_Arms_Calcs.AmmoLength+150) >(Small_Arms_Calcs.RecieverLength*10):
                    self.ClipMagLengthError_label.grid(in_=self.ErrorsInfo, column=0, \
                                    sticky= "W", padx=5, pady=5)
                else:
                    self.ClipMagLengthError_label.grid_forget()

            #wrong sight types warnings

            if ((Small_Arms.SightType == "Telescopic sights") or\
               (Small_Arms.SightType == "Electronic sights")) and  \
               Small_Arms.WeaponTypeVar == "Pistol":
                self.SightTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                    sticky= "W", padx=5, pady=5)
            else:
                self.SightTypeError_label.grid_forget()

            #Sight tech level types warnings

            if (Small_Arms.LaserSight == 1) and (Small_Arms.TechLevel < 7):
                self.SightTechTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                    sticky= "W", padx=5, pady=5)
            elif (Small_Arms.SightType == "Optic sights") and (Small_Arms.TechLevel < 8):
                self.SightTechTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                    sticky= "W", padx=5, pady=5)
            elif (Small_Arms.SightType == "Telescopic sights") and (Small_Arms.TechLevel < 6):
                self.SightTechTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                    sticky= "W", padx=5, pady=5)
            elif (Small_Arms.SightType == "Electronic sights") and (Small_Arms.TechLevel < 9):
                self.SightTechTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                    sticky= "W", padx=5, pady=5)
            else:
                self.SightTechTypeError_label.grid_forget()

            # recoil compenator warnings
            
            if (Small_Arms.RecoilAbsorb == "SA stock") and (Small_Arms.TechLevel < 5):
                self.RecoilAbsorbTechTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                    sticky= "W", padx=5, pady=5)
            elif (Small_Arms.RecoilAbsorb == "Folding SA stock") and (Small_Arms.TechLevel < 9):
                self.RecoilAbsorbTechTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                    sticky= "W", padx=5, pady=5)
            else:
                self.RecoilAbsorbTechTypeError_label.grid_forget()

            if (Small_Arms.RecoilComp == "Gyroscopic Compensator") and (Small_Arms.TechLevel < 10):
                self.RecoilCompTechTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                    sticky= "W", padx=5, pady=5)
            elif (Small_Arms.RecoilComp == "Inertial Compensator") and (Small_Arms.TechLevel < 14):
                self.RecoilCompTechTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                    sticky= "W", padx=5, pady=5)
            else:
                self.RecoilCompTechTypeError_label.grid_forget()

            if (Small_Arms.RecoilBrake == "Muzzle Brake") and (Small_Arms.TechLevel < 6):
                self.RecoilBrakeTechTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                    sticky= "W", padx=5, pady=5)
            elif (Small_Arms.RecoilBrake == "Long Muzzle Brake") and (Small_Arms.TechLevel < 7):
                self.RecoilBrakeTechTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                    sticky= "W", padx=5, pady=5)
            else:
                self.RecoilBrakeTechTypeError_label.grid_forget()

            # shotgun bullets not divisable by 4

            if (Small_Arms_Calcs.ShotgunBullets%4) != 0:
                self.ShotgunBulletsError_label.grid(in_=self.ErrorsInfo, column=0, \
                                    sticky= "W", padx=5, pady=5)
            else:
                self.ShotgunBulletsError_label.grid_forget()

            # flechette darts not divisable by 4

            if (Small_Arms_Calcs.FlechetteDarts%4) != 0:
                self.FlechetteDartError_label.grid(in_=self.ErrorsInfo, column=0, \
                                    sticky= "W", padx=5, pady=5)
            else:
                self.FlechetteDartError_label.grid_forget()


            # light or heavy barrel

            if (Small_Arms_Calcs.AverageMuzzleEnergy >= 5000) or (self.MountType == "Bipod")\
               or (self.MountType == "Tripod") or \
               (Small_Arms.RecieverTypeVar == "Heavy self-loading") \
               and (Small_Arms.BarrelTypeVar != "Heavy"):
                self.BarrelTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                    sticky= "W", padx=5, pady=5)      
            else:
                self.BarrelTypeError_label.grid_forget()


            #Belt feed check
            if (Small_Arms.MagazineType =="Belt") and \
               (Small_Arms.RecieverTypeVar != "Heavy self-loading"):
                self.BeltTypeError_label.grid(in_=self.ErrorsInfo, column=0, \
                                    sticky= "W", padx=5, pady=5)
            else:
                self.BeltTypeError_label.grid_forget()          

        def Set_Outputs():
            Small_Arms.TechLevel =self.TechLevel.get()
            Small_Arms.WeaponName =self.WeaponName.get()
            Small_Arms.AmmoDiameter = self.AmmoDiameter.get()
            Small_Arms.CartridgeLength = self.CartridgeLength.get()
            Small_Arms.ShotgunBullets = self.ShotgunBullets.get()
            Small_Arms.FlechetteDarts = self.FlechetteDarts.get()
            Small_Arms.AmmoTypeVar = self.AmmoTypeVar.get()
            Small_Arms.CaseTypeVar = self.CaseTypeVar.get()
            Small_Arms.ProdTypeVar = self.ProdTypeVar.get()
            Small_Arms.BarrelLengthModVar = self.BarrelLengthModVar.get()
            Small_Arms.RiflingTypeVar = self.RiflingTypeVar.get()
            Small_Arms.BarrelTypeVar = self.BarrelTypeVar.get()
            Small_Arms.RecieverTypeVar = self.RecieverTypeVar.get()
            Small_Arms.RateofFire = self.RateofFire.get()
            Small_Arms.MagazineCap = self.MagazineCap.get()
            Small_Arms.StockType = self.StockType.get()
            Small_Arms.MountType = self.MountType.get()
            Small_Arms.MagazineType = self.MagazineType.get()
            Small_Arms.SightType = self.SightType.get()
            Small_Arms.RecoilAbsorb =self.RecoilAbsorb.get()
            Small_Arms.RecoilComp = self.RecoilComp.get()
            Small_Arms.RecoilBrake = self.RecoilBrake.get()
            Small_Arms.BayonetLug = self.BayonetLug.get()
            Small_Arms.Grenade = self.Grenade.get()
            Small_Arms.Silenced = self.Silenced.get()
            Small_Arms.WeaponTypeVar = self.WeaponTypeVar.get()
            Small_Arms.TubularMagType = self.TubularMagType.get()
            Small_Arms.LaserSight = self.LaserSight.get()
            Small_Arms.Suppressor = self.Suppressor.get()
            Small_Arms.FlashSuppressor = self.FlashSuppressor.get()
            Small_Arms.RotaryWeapon = self.RotaryWeapon.get()
            Small_Arms.RotaryBarrels = self.RotaryBarrels.get()
            Small_Arms_Calcs ()
            Design_Error_Checks ()
            self.FinalDesignBox.delete('1.0', 'end')
            self.FinalDesignBox.insert('1.0', Small_Arms_Calcs.FinalDesign)

        def Check_Is_Not_Empty(self, name):
            CheckVariable = "self."+name+".get()"
            if len(eval(CheckVariable)) != 0:
                Set_Outputs()

      

class Small_Arms_Calcs ():

    FinalDesign = str()
    AmmoWeight = float()
    RecieverLength =float()
    AmmoLength = float()
    BarrelLength = float()
    StockLength = int()
    AverageMuzzleEnergy = float()
    AmmoDiameter = float()
    CartridgeLength = float()
    ShotgunBullets = int()
    FlechetteDarts = int()
    MagazineCap = int()
    RotaryBarrels = int()
    
    
    def __init__(self,):

        TechLevel = int(Small_Arms.TechLevel)
        AmmoDiameter = float(Small_Arms.AmmoDiameter)
        CartridgeLength = float(Small_Arms.CartridgeLength)
        ShotgunBullets = int(Small_Arms.ShotgunBullets)
        FlechetteDarts = int(Small_Arms.FlechetteDarts)
        AmmoTypeVar = Small_Arms.AmmoTypeVar
        CaseTypeVar = Small_Arms.CaseTypeVar
        BarrelLengthModVar = float(Small_Arms.BarrelLengthModVar)
        RiflingTypeVar = Small_Arms.RiflingTypeVar
        BarrelTypeVar = Small_Arms.BarrelTypeVar
        RecieverTypeVar = Small_Arms.RecieverTypeVar
        AmmoTypeVar = Small_Arms.AmmoTypeVar
        RateofFire = Small_Arms.RateofFire
        WeaponName = Small_Arms.WeaponName
        MagazineCap = int(Small_Arms.MagazineCap)
        StockType = Small_Arms.StockType
        MountType = Small_Arms.MountType
        Options = str()
        MagazineType = Small_Arms.MagazineType
        SightType = Small_Arms.SightType
        RecoilAbsorb = Small_Arms.RecoilAbsorb
        RecoilComp = Small_Arms.RecoilComp
        BayonetLug = int(Small_Arms.BayonetLug)
        Grenade = int(Small_Arms.Grenade)
        Silenced = int(Small_Arms.Silenced)
        LaserSight = int(Small_Arms.LaserSight)
        RecoilBrake = Small_Arms.RecoilBrake
        Suppressor = int(Small_Arms.Suppressor)
        FlashSuppressor = Small_Arms.FlashSuppressor
        RotaryWeapon = int(Small_Arms.RotaryWeapon)
        RotaryBarrels = int(Small_Arms.RotaryBarrels)

#======================
# ammo design section
#======================

        if Small_Arms.WeaponTypeVar == "Shotgun":
            AmmoLength = CartridgeLength #in mm, shotgun
        elif CaseTypeVar == "Straight":
            AmmoLength = CartridgeLength + AmmoDiameter #in mm straight cartridge
        else:
            AmmoLength = CartridgeLength + (2*AmmoDiameter) #in mm necked cartridge

        if Small_Arms.WeaponTypeVar == "Shotgun":
            AmmoWeight = 0.003*CartridgeLength*math.pi*pow((AmmoDiameter/2),2)
        elif CaseTypeVar == "Straight":
            AmmoWeight = 0.008*CartridgeLength*math.pi*pow((AmmoDiameter/2),2)#straight cartridge
        else:
            AmmoWeight = 0.01*CartridgeLength*math.pi*pow((AmmoDiameter/2),2) #necked cartridge

        AmmoWeight = round(AmmoWeight,1) # in grams

        #Cartrigde mods based on type and primer type
        if AmmoTypeVar == "Standard": # standard primers
            if Small_Arms.WeaponTypeVar == "Shotgun": 
                MuzzleVelCartMods = 0.2
            elif CaseTypeVar == "Straight": 
                MuzzleVelCartMods = 0.4
            else: # necked cartridges
                MuzzleVelCartMods = 1.6
        else: # ETC cartridges
            if Small_Arms.WeaponTypeVar == "Shotgun": 
                MuzzleVelCartMods = 0.3
            elif CaseTypeVar == "Straight": 
                MuzzleVelCartMods = 0.8
            else: # necked cartridges
                MuzzleVelCartMods = 3.2


        MuzzleVelTLMod = [0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.3]

        if TechLevel >9:
           MuzzleVelocityTLMult = 1.3
        else:
            MuzzleVelocityTLMult = MuzzleVelTLMod [TechLevel-3]

        # in joules
        AverageMuzzleEnergy = MuzzleVelocityTLMult*MuzzleVelCartMods*\
                                CartridgeLength*math.pi*pow((AmmoDiameter/2),2)

        if AverageMuzzleEnergy > 10000:
            PriceTypeMult = 0.05
        elif Small_Arms.WeaponTypeVar == "Shotgun":
            PriceTypeMult = 0.01
        elif Small_Arms.ProdTypeVar == "Military":
            PriceTypeMult = 0.02
        else:
            PriceTypeMult = 0.04

        AmmoPrice = AmmoWeight * PriceTypeMult # in Credits


#======================
# Barrel figures
#======================

        #Rifling mods mods based on type and primer type
        if AmmoTypeVar == "Standard": # standard primers
            if RiflingTypeVar == "Smoothbore": 
                RiflingMod = 4
            else: # Rifled
                RiflingMod = 1
        else: # ETC cartridges
            if RiflingTypeVar == "Smoothbore": 
                RiflingMod = 3
            else: # Rifled
                RiflingMod = 0.5


        AverageBarrelLength = (AverageMuzzleEnergy/pow(AmmoDiameter,2))*RiflingMod


        if AverageBarrelLength < 10:
            AverageBarrelLength = 10

        BarrelLength = AverageBarrelLength/100*BarrelLengthModVar # in cm

        if BarrelTypeVar == "Light":
            BarrelWeight = 0.02*BarrelLength # in kg
        else: #heavy barrels
            BarrelWeight = 0.03*BarrelLength # in kg

        # djusment for rotary weapons
        if RotaryWeapon == 1:
            BarrelWeight = BarrelWeight * RotaryBarrels

        if RiflingTypeVar == "Smoothbore":
            BarrelPrice = BarrelWeight*100 # in Credits
        elif BarrelTypeVar == "Light": # light rifled barrels
            BarrelPrice = BarrelWeight*600 # in Credits
        else: # heavy rifled barrels
            BarrelPrice = BarrelWeight*600 # in Credits

        MuzzleEnergy = AverageMuzzleEnergy*(1+(0.5*((BarrelLength/AverageBarrelLength)-1)))


#======================
#Receiver figures
#======================

        ReceiverTLMods =[1, 0.55, 0.55, 0.5, 0.5, 0.45,0.45,\
                         0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, \
                         0.4, 0.4, 0.4, 0.4, 0.4] # for TL 3-21
        

        RecieverLength = ReceiverTLMods[TechLevel-3]*(math.sqrt(AverageMuzzleEnergy))

        #ammo Length in mm receiver Length in cm
        if RecieverLength < (10/AmmoLength):
            RecieverLength = (10/AmmoLength)


        # checks for primer type then barrel type 
        if AmmoTypeVar == "Standard": # standard primers
            if BarrelTypeVar == "Light": 
                ReceiverWeight = 0.001*AverageMuzzleEnergy
            else: # Heavy barrel
                ReceiverWeight = 0.002*AverageMuzzleEnergy
        else: # ETC cartridges
            if BarrelTypeVar == "Light": 
                ReceiverWeight = 0.0005*AverageMuzzleEnergy +0.3
            else: # Heavy barrel
                ReceiverWeight = 0.001*AverageMuzzleEnergy +0.3

        #adjustment for shotguns
        if Small_Arms.WeaponTypeVar == "Shotgun":
            ReceiverWeight = ReceiverWeight*0.6

        # adjustment for rotary weapons
        if RotaryWeapon == 1:
            ReceiverWeight = ReceiverWeight * (1+(RotaryBarrels/10))

        if RecieverTypeVar == "Individully Loadng":
            ReceiverPriceMod = 50
        elif RecieverTypeVar == "Revolver":
            ReceiverPriceMod = 150
        elif RecieverTypeVar == "Lever Action":
            ReceiverPriceMod = 300
        elif RecieverTypeVar == "Bolt action":
            ReceiverPriceMod = 300
        elif (RecieverTypeVar == "Heavy self-loading") \
             or (RecieverTypeVar == "Light self-loading"):
            if RateofFire == "SA":
                ReceiverPriceMod = 200
            elif (RateofFire == "3") or (RateofFire == "5") or (RateofFire == "10"):
                ReceiverPriceMod = 250
            else: #multiple select fire options
                ReceiverPriceMod = 300
        else: # Pump action
            ReceiverPriceMod = 300

        if AmmoTypeVar == "Standard": # standard primers
            ReceiverPrice = ReceiverWeight*ReceiverPriceMod
        else: # ETC cartridges
            ReceiverPrice = 200 + ReceiverWeight*ReceiverPriceMod


#======================
#stock figures
#======================


# in cm
        if StockType == "Wood pistol grip":
            StockLength = 0
        elif StockType == "Hollow pistol grip":
            StockLength = 0
        elif StockType == "Wooden stock":
            StockLength = 25
        elif StockType == "Carbine stock":
            StockLength = 25
        elif StockType == "Folding stock":
            StockLength = 25
        elif StockType == "Plastic stock":
            StockLength = 25
        else: #Bullpup rifle stock
            StockLength = 5

# in kg

        if StockType == "Wood pistol grip":
            StockWeight = 0.2
        elif StockType == "Hollow pistol grip":
            StockWeight = 0.1
        elif StockType == "Wooden stock":
            StockWeight = 1
        elif StockType == "Carbine stock":
            StockWeight = 0.7
        elif StockType == "Folding stock":
            StockWeight = 0.5
        elif StockType == "Plastic stock":
            StockWeight = 0.5
        else: #Bullpup rifle stock
            StockWeight = 0.1

# in Cr

        if StockType == "Wood pistol grip":
            StockPrice = 5
        elif StockType == "Hollow pistol grip":
            StockPrice = 25
        elif StockType == "Wooden stock":
            StockPrice = 25
        elif StockType == "Carbine stock":
            StockPrice = 20
        elif StockType == "Folding stock":
            StockPrice = 50
        elif StockType == "Plastic stock":
            StockPrice = 30
        else: #Bullpup rifle stock
            StockPrice = 10

#======================
#feed figures
#======================



        if MagazineType == "Cassette":
            MagazineEmptyWeight = 2
        else: #all other magazine types
            MagazineEmptyWeight = (0.0006 * ((MagazineCap+4)*AmmoWeight)) #in kg

        MagazineLoadedWeight = MagazineEmptyWeight + \
                               (MagazineCap*(AmmoWeight/1000)) #in kg

        if MagazineType == "Cassette":
            MagazinePrice = math.ceil(500*AmmoPrice)
        else: #all other magazine types
            MagazinePrice = math.ceil(10*MagazineEmptyWeight)

        # addjustments for Electrothermal-chemical batteries
        if TechLevel == 9:
            ETCTLMod = 0.027
        elif TechLevel == 10:
            ETCTLMod = 0.019
        elif TechLevel == 11:
            ETCTLMod = 0.013
        else: #TL12 +
            ETCTLMod = 0.011

        
        if AmmoTypeVar == "ETC":
            MagazineEmptyWeight = MagazineEmptyWeight + (ETCTLMod * MagazineCap)
            MagazinePrice = MagazinePrice + (5*MagazineCap)



        MagazineLoadedPrice = MagazinePrice + (MagazineCap*AmmoPrice)


#======================
# sight values
#======================

        if SightType =="Optic sights":
            SightMass = 0.1
            SightPrice = 150
        elif SightType =="Telescopic sights":
            SightMass = 0.1
            SightPrice = 200
        elif SightType =="Electronic sights":
            SightMass = 0.2
            SightPrice = 2000
        else: #iron sights
            SightMass = 0.0
            SightPrice = 0

        if LaserSight == 1:
            if TechLevel == 8:
                LaserSightMass = 1.0
                LaserSightPrice = 400
            elif TechLevel == 9:
                LaserSightMass = 0.5
                LaserSightPrice = 100
            else: # tech level 10+
                LaserSightMass = 0.5
                LaserSightPrice = 300
        else: # no sight fitted
                LaserSightMass = 0
                LaserSightPrice = 0

#======================
# compensators Values
#======================

        if RecoilAbsorb == "Folding SA stock":
            RecoilAbsorbWeight = 0.2
            RecoilAbsorbPrice = 150
        elif RecoilAbsorb == "SA stock":
            if TechLevel == (5 or 6):
                RecoilAbsorbWeight = 0.1
                RecoilAbsorbPrice = 50
            elif TechLevel >= 7:
                RecoilAbsorbWeight = 0.2
                RecoilAbsorbPrice = 75
            else: #TL <5
                RecoilAbsorbWeight = 0
                RecoilAbsorbPrice = 0
        else: #no recoil absorber
            RecoilAbsorbWeight = 0
            RecoilAbsorbPrice = 0

        if RecoilComp == "Gyroscopic Compensator":
            RecoilCompWeight = 0.5
            RecoilCompPrice = 300
        elif RecoilComp == "Inertial Compensator":
            RecoilCompWeight = 1
            RecoilCompPrice = 1000
        else: #no recoil absorber
            RecoilCompWeight = 0
            RecoilCompPrice = 0

        if RecoilBrake == "Muzzle Brake":
            RecoilBrakeLength = 4
            RecoilBrakeWeight = 0.2
            RecoilBrakePrice = 50
        elif RecoilBrake == "Long Muzzle Brake":
            RecoilBrakeLength = 8
            RecoilBrakeWeight = 0.4
            RecoilBrakePrice = 200
        else: #no recoil absorber
            RecoilBrakeLength = 0
            RecoilBrakeWeight = 0
            RecoilBrakePrice = 0

#======================
# bipod values
#======================

        if MountType == "Bipod":
            MountWeight = 0.0005*MuzzleEnergy
            if MountWeight < 1:
                MountWeight = 1
            MountPrice = 50 +(MountWeight * 10)
        else: #no mount vehicle or tripod - calculated below 
            MountWeight = 0
            MountPrice = 0

#======================
# grenade adaptor addon
#======================

        if Grenade == 1:
            GrenadeLength = 5
            GrenadePrice = 50
        else: #no adaptor
            GrenadeLength = 0
            GrenadePrice = 0

#======================
# Damage values
#======================
        

        BaseDamageValue = round(math.sqrt(MuzzleEnergy)/15,0) #base weapon damage

        # damage for HE and HEAP rounds

        HEAPDamageValue = pow((AmmoDiameter+TechLevel)-7,3)
        HEAPDamageValue = round(math.sqrt(HEAPDamageValue+MuzzleEnergy)/15,0)

        # shotgun damage values

        ShotgunMediumDamage = int(round(math.sqrt((MuzzleEnergy/ShotgunBullets))/15,0))
        ShotgunShortDamage = str(int(0.75*ShotgunBullets*ShotgunMediumDamage))

        ShotgunBulletMuzzleEnergy = (MuzzleEnergy/ShotgunBullets)

        if ShotgunBulletMuzzleEnergy >=601:
            if ShotgunBulletMuzzleEnergy < 601:
                ShotgunPenetration = "Nil"
            elif ShotgunBulletMuzzleEnergy < 2001:
                ShotgunPenetration = "1-Nil"
            elif ShotgunBulletMuzzleEnergy < 3001:
                ShotgunPenetration = "2-Nil"
            elif ShotgunBulletMuzzleEnergy < 5001:
                ShotgunPenetration = "2-3-Nil"
            elif ShotgunBulletMuzzleEnergy < 10001:
                ShotgunPenetration = "2-4-6"
            elif ShotgunBulletMuzzleEnergy < 20001:
                ShotgunPenetration = "2-3-4"
            elif ShotgunBulletMuzzleEnergy < 50001:
                ShotgunPenetration = "2-2-3"
            else:
                ShotgunPenetration = "2-2-2"
            ShotgunShortDamage = str(ShotgunMediumDamage)+"x"+str(int(0.75*ShotgunBullets))
        else:
            ShotgunPenetration = "3-4-5"


        # flechette damage values

        FlechetteMediumDamage = int(round(math.sqrt((MuzzleEnergy/FlechetteDarts))/15,0))

        FlechetteDartMuzzleEnergy = (MuzzleEnergy/FlechetteDarts)

        if FlechetteDartMuzzleEnergy < 601:
            FlechettePenetration = "Nil"
        elif FlechetteDartMuzzleEnergy < 2001:
            FlechettePenetration = "1-Nil"
        elif FlechetteDartMuzzleEnergy < 3001:
            FlechettePenetration = "2-Nil"
        elif FlechetteDartMuzzleEnergy < 5001:
            FlechettePenetration = "2-3-Nil"
        elif FlechetteDartMuzzleEnergy < 10001:
            FlechettePenetration = "2-4-6"
        elif FlechetteDartMuzzleEnergy < 20001:
            FlechettePenetration = "2-3-4"
        elif FlechetteDartMuzzleEnergy < 50001:
            FlechettePenetration = "2-2-3"
        else:
            FlechettePenetration = "2-2-2"

        if FlechetteDartMuzzleEnergy >=601:
            FlechetteShortDamage = str(FlechetteMediumDamage)\
                                   +"x"+str(int(0.75*FlechetteDarts))
        else:
            FlechetteShortDamage = str(int(0.75*FlechetteDarts*FlechetteMediumDamage))


        # Penetration

        if MuzzleEnergy < 601:
            Penetration = "Nil"
        elif MuzzleEnergy < 2001:
            Penetration = "1-Nil"
        elif MuzzleEnergy < 3001:
            Penetration = "2-Nil"
        elif MuzzleEnergy < 5001:
            Penetration = "2-3-Nil"
        elif MuzzleEnergy < 10001:
            Penetration = "2-4-6"
        elif MuzzleEnergy < 20001:
            Penetration = "2-3-4"
        elif MuzzleEnergy < 50001:
            Penetration = "2-2-3"
        else:
            Penetration = "2-2-2"

        if Penetration == "Nil":
            DSPenetration = "1-Nil"
        elif Penetration == "1-Nil":
            DSPenetration = "1-2-Nil"
        elif Penetration == "2-Nil":
            DSPenetration = "2-3-Nil"
        elif Penetration == "2-3-Nil":
            DSPenetration = "1-2-Nil"
        elif Penetration == "2-4-6":
            DSPenetration = "1-3-5"
        elif Penetration == "2-3-4":
            DSPenetration = "1-2-3"
        elif Penetration == "2-2-3":
            DSPenetration = "1-1-2"
        else:
            DSPenetration = "1-1-1"

#======================
# Shotgun burst
#======================

        if ShotgunBullets ==4:
            ShotgunBurst = 3
        elif ShotgunBullets ==8:
            ShotgunBurst = 5
        elif ShotgunBullets ==12:
            ShotgunBurst = 10
        else: # non easy numbers of bullets
            ShotgunBurst10 = round(ShotgunBullets/12,0)
            if ShotgunBullets%12 == 4:
                ShotgunBurstOther = 3
            elif ShotgunBullets%12 == 8:
                ShotgunBurstOther = 5
            else: # if divisable by 12
                ShotgunBurstOther = 0
                
            if ShotgunBurstOther == 0:
                ShotgunBurst = str(int(ShotgunBurst10)) +"x10"
            else:
                ShotgunBurst = str(int(ShotgunBurst10)) +"x10," + str(ShotgunBurstOther)

#======================
# Flechette burst
#======================

        if FlechetteDarts ==4:
            FlechetteBurst = 3
        elif FlechetteDarts ==8:
            FlechetteBurst = 5
        elif FlechetteDarts ==12:
            FlechetteBurst = 10
        else: # non easy numbers of darts
            FlechetteBurst10 = round(ShotgunBullets/12,0)
            if FlechetteDarts%12 == 4:
                FlechetteBurstOther = 3
            elif FlechetteDarts%12 == 8:
                FlechetteBurstOther = 5
            else: # if divisable by 12
                FlechetteBurstOther = 0
                
            if FlechetteBurstOther == 0:
                FlechetteBurst = str(int(FlechetteBurst10)) +"x10"
            else:
                FlechetteBurst = str(int(FlechetteBurst10)) +"x10," + str(FlechetteBurstOther)

#======================
# Range Values
#======================

        #stock and mount mods to range
        if Small_Arms.WeaponTypeVar == "Shotgun":
            RangeConfigMod = 0.5
        elif RecieverTypeVar == "Bolt action":
            if Small_Arms.WeaponTypeVar == "Pistol":
                RangeConfigMod = (1.1*0.4)
            else: #two handed bolt action
                RangeConfigMod = (1.1*1.3)
        elif StockType == "Bullpup":
            if Small_Arms.WeaponTypeVar == "Pistol":
                RangeConfigMod = (0.9*0.4)
            else: #two handed bullpup
                RangeConfigMod = (0.9*1.3)
        elif Small_Arms.WeaponTypeVar == "Pistol":
            RangeConfigMod = 0.4
        else: #two handed weapons
            RangeConfigMod = 1.3
            
        # two handed weapon mod not later mount range mod
        if MountType == "Tripod":
            RangeConfigMod = 1.3
        if MountType == "Vehicle":
            RangeConfigMod = 1.3

        # barrel Length range mod

        if ((BarrelLength/AverageBarrelLength)-1) < 0: #negative values
            BarrelRangeModConstant = 1.2
        else: #positive values 
            BarrelRangeModConstant = 0.75

        BarrelRangeMod = 1 + (((BarrelLength/AverageBarrelLength)-1)*BarrelRangeModConstant)
            
        #base range calcs

        BaseShortRange = math.sqrt(MuzzleEnergy) * RangeConfigMod * BarrelRangeMod
        BaseTranqRange = BaseShortRange * 0.6
        BaseHEAPRange = BaseShortRange * 0.75
        BaseDSRange = BaseShortRange * 1.2

        #sight range adjustments

        #optic sight multiplier based on tech level
        if TechLevel == 7:
            OpticRangeMult = 1.05
        elif TechLevel == 8:
            OpticRangeMult = 1.1
        elif TechLevel >= 9:
            OpticRangeMult = 1.15
        else: #cover techlevels below 7 even though sight is tech level 7+
            OpticRangeMult = 1

        if SightType == "Optic sights":
            FinalShortRange = BaseShortRange * OpticRangeMult
            FinalTranqRange = BaseTranqRange * OpticRangeMult
            FinalHEAPRange = BaseHEAPRange * OpticRangeMult
            FinalDSRange = BaseDSRange * OpticRangeMult
        elif SightType =="Telescopic sights":
            FinalShortRange = BaseShortRange + 15
            FinalTranqRange = BaseTranqRange + 15
            FinalHEAPRange = BaseHEAPRange + 15
            FinalDSRange = BaseDSRange +15
        elif SightType =="Electronic sights":
            FinalShortRange = BaseShortRange + 20
            FinalTranqRange = BaseTranqRange + 20
            FinalHEAPRange = BaseHEAPRange + 20
            FinalDSRange = BaseDSRange + 20
        else: # iron sights
            FinalShortRange = BaseShortRange
            FinalTranqRange = BaseTranqRange
            FinalHEAPRange = BaseHEAPRange
            FinalDSRange = BaseDSRange

        #Mount range adjustments

        if MountType == "Bipod":
            MountBaseShortRange = BaseShortRange * 1.3
            MountBaseTranqRange = BaseTranqRange * 1.3
            MountBaseHEAPRange = BaseHEAPRange * 1.3
            MountBaseDSRange = BaseDSRange * 1.3
            MountFinalShortRange = FinalShortRange * 1.3
            MountFinalTranqRange = FinalTranqRange * 1.3
            MountFinalHEAPRange = FinalHEAPRange * 1.3
            MountFinalDSRange = FinalDSRange * 1.3
        elif (MountType == "Tripod") or (MountType == "Vehicle"):
            MountBaseShortRange = BaseShortRange * 2
            MountBaseTranqRange = BaseTranqRange * 2
            MountBaseHEAPRange = BaseHEAPRange * 2
            MountBaseDSRange = BaseDSRange * 2
            MountFinalShortRange = FinalShortRange * 2
            MountFinalTranqRange = FinalTranqRange * 2
            MountFinalHEAPRange = FinalHEAPRange * 2
            MountFinalDSRange = FinalDSRange * 2
        else:
            MountBaseShortRange = 0
            MountBaseTranqRange = 0
            MountBaseHEAPRange = 0
            MountBaseDSRange = 0
            MountFinalShortRange = 0
            MountFinalTranqRange = 0
            MountFinalHEAPRange = 0
            MountFinalDSRange = 0

#======================
# Final range adjustments
#======================

        # caping base ranges

        if BaseShortRange > 300:
            BaseShortRange = 300
        if BaseHEAPRange > 300:
            BaseHEAPRange = 300
        if BaseDSRange > 300:
            BaseDSRange = 300
        if BaseTranqRange > 30:
            BaseTranqRange = 30
        if MountBaseShortRange > 300:
            MountBaseShortRange = 300
        if MountBaseHEAPRange > 300:
            MountBaseHEAPRange = 300
        if MountBaseDSRange > 300:
            MountBaseDSRange = 300
        if MountBaseTranqRange > 30:
            MountBaseTranqRange = 30

        #sight adjusted ranges

        if FinalShortRange > 300:
            FinalShortRange = 300
        elif FinalShortRange < 20:
            FinalShortRange = int(round(FinalShortRange,0))
        else:
            FinalShortRange = int(round(FinalShortRange,-1))

        if FinalHEAPRange > 300:
            FinalHEAPRange = 300
        elif FinalShortRange < 20:
            FinalHEAPRange = int(round(FinalHEAPRange,0))
        else:
            FinalHEAPRange = int(round(FinalHEAPRange,-1))

        if FinalDSRange > 300:
            FinalDSRange = 300
        elif FinalShortRange < 20:
            FinalDSRange = int(round(FinalDSRange,0))
        else:
            FinalDSRange = int(round(FinalDSRange,-1))

        if FinalTranqRange > 30:
            FinalTranqRange = 30
        elif FinalTranqRange < 4:
            FinalTranqRange = 4
        else:
            FinalTranqRange = int(round(FinalTranqRange,0))

        #mount adjusted ranges

        if MountFinalShortRange > 300:
            MountFinalShortRange = 300
        elif MountFinalShortRange < 20:
            MountFinalShortRange = int(round(MountFinalShortRange,0))
        else:
            MountFinalShortRange = int(round(MountFinalShortRange,-1))

        if MountFinalHEAPRange > 300:
            MountFinalHEAPRange = 300
        elif MountFinalShortRange < 20:
            MountFinalHEAPRange = int(round(MountFinalHEAPRange,0))
        else:
            MountFinalHEAPRange = int(round(MountFinalHEAPRange,-1))

        if MountFinalDSRange > 300:
            MountFinalDSRange = 300
        elif MountFinalShortRange < 20:
            MountFinalDSRange = int(round(MountFinalDSRange,0))
        else:
            MountFinalDSRange = int(round(MountFinalDSRange,-1))
            
        if MountFinalTranqRange > 30:
            MountFinalTranqRange = 30
        elif MountFinalTranqRange < 4:
            MountFinalTranqRange = 4
        else:
            MountFinalTranqRange = int(round(MountFinalTranqRange,0))

#======================
#silencer Length, weight price details
#======================


        if Silenced == 1:
            SilencerLength = MuzzleEnergy/25
            SilencerWeight = 0.025 * SilencerLength
            SilencerPrice = 5 * SilencerLength
        else:
            SilencerLength = 0
            SilencerWeight = 0
            SilencerPrice = 0

        if Suppressor == 1:
            SuppressorLength = MuzzleEnergy/100
            SuppressorWeight = 0.025 * SuppressorLength
            SuppressorPrice = 5 * SuppressorLength
        else:
            SuppressorLength = 0
            SuppressorWeight = 0
            SuppressorPrice = 0

#======================
# flash supressor
#======================

        if FlashSuppressor == "Flash Suppressor":
            FlashLength = MuzzleEnergy/300
            FlashWeight = 0.01 * FlashLength
            FlashPrice = 1 * FlashLength
        elif FlashSuppressor == "Long Flash Suppressor":
            FlashLength = MuzzleEnergy/150
            FlashWeight = 0.01 * FlashLength
            FlashPrice = 1 * FlashLength
        else: # none fitted
            FlashLength = 0
            FlashWeight = 0
            FlashPrice = 0
        # if muzzle brake fitted take slonger Length
        if RecoilBrakeLength >= FlashLength:
            FlashLength = 0
        else: #flash supressor longer
            RecoilBrakeLength = 0

#======================
# Final values calculations
#======================

        FinalLength = round(BarrelLength + RecieverLength + StockLength + \
                            GrenadeLength + SilencerLength + SuppressorLength\
                            + RecoilBrakeLength + FlashLength, 1)
        FinalEmptyWeight = round(BarrelWeight + ReceiverWeight + StockWeight \
                                 + MagazineEmptyWeight + SightMass + RecoilAbsorbWeight\
                                 + RecoilCompWeight + MountWeight + LaserSightMass\
                                 + RecoilBrakeWeight + SilencerWeight + SuppressorWeight\
                                 + FlashWeight, 3)
        FinalLoadedWeight = round (FinalEmptyWeight - MagazineEmptyWeight \
                                   + MagazineLoadedWeight, 3)
        FinalPrice = round(BarrelPrice + ReceiverPrice + StockPrice + SightPrice\
                           + RecoilAbsorbPrice + RecoilCompPrice + \
                           MountPrice + GrenadePrice + LaserSightPrice\
                           + RecoilBrakePrice + SilencerPrice + SuppressorPrice\
                           + FlashPrice, 2)
        MagazineLoadedWeight = round(MagazineLoadedWeight,4)
        MagazineEmptyWeight = round(MagazineEmptyWeight,4)
        MagazineLoadedPrice =round(MagazineLoadedPrice,2)
        MagazineType = MagazineType.lower()

#======================
# features options variable
#======================

        if SightType == "Optic sights":
            if LaserSight == 1:
                SightOption = "Optic sights and laser sights"
            else: # optic but no laser sight
                SightOption = "Optic sights"
        elif SightType == "Telescopic sights":
            if LaserSight == 1:
                SightOption = "Telescopic sights and laser sights"
            else: # telescopic but no laser sight
                SightOption = "Telescopic sights"
        elif SightType == "Electronic sights":
            if LaserSight == 1:
                SightOption = "Electronic sights and laser sights"
            else: # Electronic but no laser sight
                SightOption = "Electronic sights"
        else: #No sights fitted
            if LaserSight == 1:
                SightOption = "Laser sights"
            else: # no sights fitted
                SightOption = ""


        if MountType == "Bipod":
            if SightOption == "":
                MountOption = "Bipod"
            else:
                MountOption = ", bipod"
        elif MountType == "Tripod":
            if SightOption == "":
                MountOption = "Tripod"
            else:
                MountOption = ", yripod"
        elif MountType == "Vehicle":
            if SightOption == "":
                MountOption = "Vehicle Mount"
            else:
                MountOption = ", vehicle Mount"
        else: #No Mountings fitted
            MountOption = ""

        if BayonetLug == 1:
            if (MountOption == "") and (SightOption ==""):
                BayonetOption = "Bayonet lug"
            else:
                BayonetOption = ", bayonet lug"    
        else: #no Bayonet lug
            BayonetOption = ""

        if Grenade == 1:
            if (BayonetOption == "") and (MountOption == "") and \
               (SightOption ==""):
                GrenadeOption = "Grenade adaptor"
            else:
                GrenadeOption = ", grenade adaptor"
        else: #no Grenade Adaptor
            GrenadeOption = ""

        if Silenced == 1:
            if (BayonetOption == "") and (MountOption == "") \
               and (SightOption =="") and (GrenadeOption == ""):
                SilencedOption = "Silenced weapon"
            else:
                SilencedOption = ", silenced weapon"
        else: #not Silenced capable
            SilencedOption = ""

        if RecoilAbsorb == "Folding SA stock":
            if (BayonetOption == "") and (MountOption == "") \
               and (SightOption =="") and (GrenadeOption == "") \
               and (SilencedOption == ""):
                RecoilAbsorbOption = "Folding shock absorbing stock"
            else:
                RecoilAbsorbOption = ", folding shock absorbing stock"
        elif RecoilAbsorb == "SA stock":
            if (BayonetOption == "") and (MountOption == "") \
               and (SightOption =="") and (GrenadeOption == "") \
               and (SilencedOption == ""):
                RecoilAbsorbOption = "Shock absorbing stock"
            else:
                RecoilAbosrbOption = ", shock absorbing stock"
        else: #no recoil absorber
            RecoilAbsorbOption = ""

        if RecoilComp == "Gyroscopic Compensator":
            if (BayonetOption == "") and (MountOption == "") \
               and (SightOption =="") and (GrenadeOption == "") \
               and (SilencedOption == "") and (RecoilAbsorbOption == ""):
                RecoilCompOption = "Gyroscopic Compensator"
            else:
                RecoilCompOption = ", gyroscopic compensator"
        elif RecoilComp == "Inertial Compensator":
            if (BayonetOption == "") and (MountOption == "") \
               and (SightOption =="") and (GrenadeOption == "") \
               and (SilencedOption == "") and (RecoilAbsorbOption == ""):
                RecoilCompOption = "Inertial Compensator"
            else:
                RecoilCompOption = ", inertial compensator"
        else: #no recoil compensator
            RecoilCompOption = ""

        if RecoilBrake == "Muzzle Brake":
            if (BayonetOption == "") and (MountOption == "") \
               and (SightOption =="") and (GrenadeOption == "") \
               and (SilencedOption == "") and (RecoilAbsorbOption == "")\
                and(RecoilCompOption == ""):
                RecoilBrakeOption = "Muzzle Brake"
            else:
                RecoilBrakeOption = ", muzzle brake"
        elif RecoilBrake == "Long Muzzle Brake":
            if (BayonetOption == "") and (MountOption == "") \
               and (SightOption =="") and (GrenadeOption == "") \
               and (SilencedOption == "") and (RecoilAbsorbOption == "")\
                and(RecoilCompOption == ""):
                RecoilBrakeOption = "Long Muzzle Brake"
            else:
                RecoilBrakeOption = ", long muzzle brake"
        else: #no muzzle brake
            RecoilBrakeOption = ""

        if Suppressor == 1:
            if (BayonetOption == "") and (MountOption == "") \
               and (SightOption =="") and (GrenadeOption == "") \
               and (SilencedOption == "") and (RecoilAbsorbOption == "")\
                and(RecoilCompOption == "") and(RecoilBrakeOption == ""):
                SuppressedOption = "Suppressed weapon"
            else:
                SuppressedOption = ", suppressed weapon"
        else: #no suppressor
            SuppressedOption = ""

        if FlashSuppressor == "Flash Suppessor":
            if (BayonetOption == "") and (MountOption == "") \
               and (SightOption =="") and (GrenadeOption == "") \
               and (SilencedOption == "") and (RecoilAbsorbOption == "")\
                and(RecoilCompOption == "") and(RecoilBrakeOption == "")\
                and (SuppressedOption != ""):
                FlashOption = "Flash Suppessor"
            else:
                FlashOption = ", flash suppessor"
        elif FlashSuppressor == "Long Flash Suppessor":
            if (BayonetOption == "") and (MountOption == "") \
               and (SightOption =="") and (GrenadeOption == "") \
               and (SilencedOption == "") and (RecoilAbsorbOption == "")\
                and(RecoilCompOption == "") and(RecoilBrakeOption == "")\
                and (SuppressedOption != ""):
                FlashOption = "Long Flash Suppessor"
            else:
                FlashOption = ", long flash suppessor"
        else: #no flash supressor
            FlashOption = ""               
            

        if (SightOption != "") or (MountOption != "") or (BayonetOption != "") \
        or (GrenadeOption != "") or (SilencedOption != "") or (RecoilAbsorbOption !="") \
        or (RecoilCompOption != "") or (RecoilBrakeOption != "") or (SuppressedOption !=""):
            Options = SightOption + MountOption + BayonetOption + \
                      GrenadeOption  + SilencedOption\
                      + RecoilAbsorbOption + RecoilCompOption + \
                      RecoilBrakeOption + SuppressedOption + FlashOption
        else: #nothing fitted
            Options = "None"

#======================
# recoil calcs
#======================

        #Set mod for muzzle energy

        if MuzzleEnergy < 2501:
            MuzzelEnergyMod = 1
        elif MuzzleEnergy < 5001:
            MuzzelEnergyMod = 2
        elif MuzzleEnergy < 10001:
            MuzzelEnergyMod = 3
        elif MuzzleEnergy < 20001:
            MuzzelEnergyMod = 4
        elif MuzzleEnergy < 50001:
            MuzzelEnergyMod = 5
        else: # over 50001 muzzle energy
            MuzzelEnergyMod = 6

            #Set mod for compenstor types

        if RecoilAbsorb == "Folding SA stock":
            RecoilAbsorbMod = 0.9
        elif RecoilAbsorb == "SA stock":
            if TechLevel in (5, 6):
                RecoilAbsorbMod = 0.95
            elif TechLevel in (7, 8):
                RecoilAbsorbMod = 0.9
            else: # for tech level greater than 9 
                RecoilAbsorbMod = 0.85
        else: #no recoil absorber
            RecoilAbsorbMod = 1

        if RecoilComp == "Gyroscopic Compensator":
            RecoilCompMod = 0.5
        elif RecoilComp == "Inertial Compensator":
            RecoilCompMod = 0.3
        else: #no recoil compensator
            RecoilCompMod = 1

        if RecoilBrake == "Muzzle Brake":
            if TechLevel == 6:
                RecoilBrakeMod = 0.9
            elif TechLevel == 7:
                RecoilBrakeMod = 0.85
            elif TechLevel == 8:
                RecoilBrakeMod = 0.8
            else: #Tech Level9+
                RecoilBrakeMod = 0.75               
        elif RecoilBrake == "Long Muzzle Brake":
            if TechLevel == 7:
                RecoilBrakeMod = 0.7
            elif TechLevel == 8:
                RecoilBrakeMod = 0.65
            else: # for tech level 9+
                RecoilBrakeMod = 0.6
        else: #no recoil absorber
            RecoilBrakeMod = 1

        if AmmoTypeVar == "ETC":
            RecoilAmmoMod = 0.6
        else: #standard ammo
            RecoilAmmoMod = 1

        if RateofFire in ('SA' or '3' or '5' or '10' or '3/5' or'5/10' or'3/5/10'):
            RecoilActionMod = 0.95
        else: #no auto or semi auto actions
            RecoilActionMod = 1

        RecoilMod = RecoilAbsorbMod*RecoilCompMod*RecoilBrakeMod\
                    *RecoilActionMod*RecoilAmmoMod


        #Set mod for mount type

        MountMod = 1
        if MountType == "Bipod":
            MountMod = 0.5
        if MountType == "Tripod":
            MountMod = 0.25

        # set weapon weight dependant on feed type
        
        if MagazineType in ( "Belt", "Cassette"):
            RecoilWeight = FinalEmptyWeight
        else : #everything but cassette and belt feeds
            RecoilWeight = FinalLoadedWeight

        # single shot recoil calc


        SSRecoil = (((0.15*math.sqrt(MuzzleEnergy))/RecoilWeight)+ \
                    MuzzelEnergyMod)* RecoilMod

        #calc for single shots on mounts

        if MountType == "Bipod":
            SSRecoilMount = SSRecoil * MountMod
        if MountType == "Tripod":
            SSRecoilMount = SSRecoil * MountMod
            
        # burst shot recoil calcs

        BurstRecoil3 = int(math.floor(((((1.5*(0.15*math.sqrt(MuzzleEnergy)))/RecoilWeight)+\
                       (1.5*MuzzelEnergyMod))*RecoilMod)))

        BurstRecoil5 = int(math.floor(((((2.5*(0.15*math.sqrt(MuzzleEnergy)))/RecoilWeight)+\
                       (2.5*MuzzelEnergyMod))*RecoilMod)))

        BurstRecoil10 =int(math.floor(((((5*(0.15*math.sqrt(MuzzleEnergy)))/RecoilWeight)+\
                       (5*MuzzelEnergyMod))*RecoilMod)))


        if RateofFire == '3':
            BurstRecoil  = BurstRecoil3
            BurstRecoilMount  = int(math.floor(BurstRecoil3)*MountMod)
        elif RateofFire == '5':
            BurstRecoil = BurstRecoil5
            BurstRecoilMount = int(math.floor(BurstRecoil5)*MountMod)
        elif RateofFire == '10':
            BurstRecoil = BurstRecoil10
            BurstRecoilMount = int(math.floor(BurstRecoil10)*MountMod)
        elif RateofFire == '3/5':
            BurstRecoil = str(BurstRecoil3)+"/"\
                          +str(BurstRecoil5)
            BurstRecoilMount = str(int(math.floor(BurstRecoil3)*MountMod))+"/"\
                          +str(int(math.floor(BurstRecoil5)*MountMod))
        elif RateofFire == '5/10':
            BurstRecoil = str(BurstRecoil5)+"/"\
                          +str(BurstRecoil10)
            BurstRecoilMount = str(int(math.floor(BurstRecoil5)*MountMod))+"/"\
                          +str(int(math.floor(BurstRecoil10)*MountMod))
        elif RateofFire == '3/5/10':
            BurstRecoil = str(BurstRecoil3)+"/"+str(BurstRecoil5)+"/"\
                          +str(BurstRecoil10)
            BurstRecoilMount = str(int(math.floor(BurstRecoil3)*MountMod))+"/"\
                               + str(int(math.floor(BurstRecoil5)*MountMod))+"/"\
                          +str(int(math.floor(BurstRecoil10)*MountMod))
        else:
            BurstRecoil = str("-")
            BurstRecoilMount = str("-")


#======================
# tripod values
#======================
        
        if RateofFire == '3':
            TripodWeight = BurstRecoil3
        elif RateofFire == '5':
            TripodWeight = BurstRecoil5
        elif RateofFire == '10':
            TripodWeight = BurstRecoil10
        elif RateofFire == '3/5':
            TripodWeight = BurstRecoil5
        elif RateofFire == '5/10':
            TripodWeight = BurstRecoil10
        elif RateofFire == '3/5/10':
            TripodWeight = BurstRecoil10
        else:
            TripodWeight = 0

        TripodPrice = 50+(10*TripodWeight)

#======================
# silenced weapon output values
#======================

        # silenced muzzle calc based on same diameter round and 15mm straight cartridge

        SilencedAverageMuzzleEnergy = MuzzleVelocityTLMult*0.4*\
                                15*math.pi*pow((AmmoDiameter/2),2) # in joules

        SilencedMuzzleEnergy = SilencedAverageMuzzleEnergy\
                               *(1+(0.5*((BarrelLength/AverageBarrelLength)-1)))

        # silenced weapon damage

        SilencedBaseDamageValue = round(math.sqrt(SilencedMuzzleEnergy)/15,0) 

        # damage for silenced HE and HEAP rounds

        SilencedHEAPDamageValue = pow((AmmoDiameter+TechLevel)-7,3)
        SilencedHEAPDamageValue = round(math.sqrt(SilencedHEAPDamageValue\
                                                  +SilencedMuzzleEnergy)/15,0)

        #silenced weapon penetration

        if SilencedMuzzleEnergy < 601:
            SilencedPenetration = "Nil"
        elif SilencedMuzzleEnergy < 2001:
            SilencedPenetration = "1-Nil"
        elif SilencedMuzzleEnergy < 3001:
            SilencedPenetration = "2-Nil"
        elif SilencedMuzzleEnergy < 5001:
            SilencedPenetration = "2-3-Nil"
        elif SilencedMuzzleEnergy < 10001:
            SilencedPenetration = "2-4-6"
        elif SilencedMuzzleEnergy < 20001:
            SilencedPenetration = "2-3-4"
        elif SilencedMuzzleEnergy < 50001:
            SilencedPenetration = "2-2-3"
        else:
            SilencedPenetration = "2-2-2"

        if SilencedPenetration == "Nil":
            SilencedDSPenetration = "1-Nil"
        elif SilencedPenetration == "1-Nil":
            SilencedDSPenetration = "1-2-Nil"
        elif SilencedPenetration == "2-Nil":
            SilencedDSPenetration = "2-3-Nil"
        elif SilencedPenetration == "2-3-Nil":
            SilencedDSPenetration = "1-2-Nil"
        elif SilencedPenetration == "2-4-6":
            SilencedDSPenetration = "1-3-5"
        elif SilencedPenetration == "2-3-4":
            SilencedDSPenetration = "1-2-3"
        elif SilencedPenetration == "2-2-3":
            SilencedDSPenetration = "1-1-2"
        else:
            SilencedDSPenetration = "1-1-1"  

        #silenced weapon ranges

        SilencedBaseShortRange = math.sqrt(SilencedMuzzleEnergy) * RangeConfigMod
        SilencedBaseTranqRange = SilencedBaseShortRange * 0.6
        SilencedBaseHEAPRange = SilencedBaseShortRange * 0.75
        SilencedBaseDSRange = SilencedBaseShortRange * 1.2

        # range mods for ilenced weapons and optics etc

        SilencedFinalShortRange = FinalShortRange*(SilencedBaseShortRange/BaseShortRange)
        SilencedFinalTranqRange = (SilencedBaseTranqRange/BaseTranqRange)*FinalTranqRange
        SilencedFinalHEAPRange = (SilencedBaseHEAPRange/BaseHEAPRange)*FinalHEAPRange
        SilencedFinalDSRange = (SilencedBaseDSRange/BaseDSRange)*FinalDSRange
        
        #Silenced recoil for single shot

        SilencedSSRecoil = (((0.15*math.sqrt(SilencedMuzzleEnergy))/RecoilWeight)+ \
                    MuzzelEnergyMod)* RecoilMod
            
        # Silenced burst shot recoil calcs

        SilencedBurstRecoil5 = int(math.floor(((((2.5*(0.15*math.sqrt(SilencedMuzzleEnergy)))\
                                         /RecoilWeight)+(2.5*MuzzelEnergyMod))\
                                       *RecoilMod)))

        SilencedBurstRecoil10 =int(math.floor(((((5*(0.15*math.sqrt(SilencedMuzzleEnergy)))\
                                         /RecoilWeight)+(5*MuzzelEnergyMod))\
                                       **RecoilMod)))

        SilencedBurstRecoil3 =int(math.floor((((1.5*((0.15*math.sqrt(SilencedMuzzleEnergy)))\
                                         /RecoilWeight)+ (1.5*MuzzelEnergyMod))\
                                       *RecoilMod)))


        if RateofFire == '3':
            SilencedBurstRecoil  = SilencedBurstRecoil3
        elif RateofFire == '5':
            SilencedBurstRecoil = SilencedBurstRecoil5
        elif RateofFire == '10':
            SilencedBurstRecoil = SilencedBurstRecoil10
        elif RateofFire == '3/5':
            SilencedBurstRecoil = str(SilencedBurstRecoil3)+"/"\
                          +str(SilencedBurstRecoil5)
        elif RateofFire == '5/10':
            SilencedBurstRecoil = str(SilencedBurstRecoil5)+"/"\
                          +str(SilencedBurstRecoil10)
        elif RateofFire == '3/5/10':
            SilencedBurstRecoil = str(SilencedBurstRecoil3)+"/"+str(SilencedBurstRecoil5)+"/"\
                          +str(SilencedBurstRecoil10)
        else:
            SilencedBurstRecoil = str("-")

  
#======================
# Display line build up
#======================

        if AmmoDiameter - int(AmmoDiameter) != 0:
            AmmoBaseDiameter = AmmoDiameter
        else:
            AmmoBaseDiameter = int(AmmoDiameter)

        if CartridgeLength - int(CartridgeLength) != 0:
            BaseCartridgeLength = CartridgeLength
        else:
            BaseCartridgeLength = int(CartridgeLength)

        AmmoBase = str(AmmoBaseDiameter)+'x'+str(BaseCartridgeLength)+"mm"


        NameLine = "Designation: " + WeaponName
        TLLine = "TL: "+str(TechLevel)
        if AmmoTypeVar == "ETC":
            AmmoLine = "Ammo: " + AmmoBase +" ETC-"+str(TechLevel)
        else:
            AmmoLine = "Ammo: "+ AmmoBase +"-"+str(TechLevel)
        MuzzleLine = "Muzzle Energy: " + str(round(MuzzleEnergy,1)) + " joules"
        WeaponLengthLine = "Weapon Length: " + str(FinalLength) + " cm"
        WeaponWeightLine = "Weapon Weight: " + str(FinalLoadedWeight) + " kg loaded, " + \
                           str(FinalEmptyWeight) + " kg empty (includes weight of empty "\
                           + MagazineType + ")"
        WeaponPriceLine = "Weapon Price: Cr" + str(round(FinalPrice,2))
        MagazineWeightLine = "Magazine Weight: " + str(MagazineLoadedWeight) +" kg loaded, "\
                             + str(MagazineEmptyWeight) + " kg empty"
        MagazinePriceLine = "Magazine Price: Cr" + str(MagazineLoadedPrice) + " (loaded), Cr" \
                            + str(MagazinePrice) + " (empty)" 
        AmmunitionPriceLine = "Ammunition Price: Cr" + str(round(AmmoPrice,2)) + " (Ball), Cr"\
                              + str(round(2*AmmoPrice,2)) + " (HE, DS, Tranq), Cr" \
                              +str(round(3*AmmoPrice,2))+ " (HEAP), Cr" \
                              +str(round(5*AmmoPrice,2))+ " (Flechette)"
        AmmunitionWeightLine = "Ammunition Weight: " + str(AmmoWeight) + " grams per round"
        FeaturesLine = "Features: " + Options
        if MountType == "Tripod":
            TripodLine = "Tripod weight: " +str(TripodWeight)  + " kg" +'\n'+ \
                         "Tripod Price: Cr"+str(TripodPrice)
        else:
            TripodLine = ""

#======================
# damage table build up
#======================
        Bulk = str(int(round(FinalLength/15,0)))
        ShortRange = str(FinalShortRange) + "("+str(int(round(BaseShortRange,0)))+")"
        MountShortRange = str(int(round(MountFinalShortRange,0))) \
                          + "("+str(int(round(MountBaseShortRange,0)))+")"
        SilencedShortRange = str(int(round(SilencedFinalShortRange,0))) \
                          + "("+str(int(round(SilencedBaseShortRange,0)))+")"

        DSShortRange = str(FinalDSRange) + "("+str(int(round(BaseDSRange,0)))+")"
        MountDSShortRange = str(int(round(MountFinalDSRange,0))) \
                          + "("+str(int(round(MountBaseDSRange,0)))+")"
        SilencedDSShortRange = str(int(round(SilencedFinalDSRange,0))) \
                          + "("+str(int(round(SilencedBaseDSRange,0)))+")"
        
        HEAPShortRange = str(FinalHEAPRange) + "("+str(int(round(BaseHEAPRange,0)))+")"
        MountHEAPShortRange = str(int(round(MountFinalHEAPRange,0))) \
                          + "("+str(int(round(MountBaseHEAPRange,0)))+")"
        SilencedHEAPShortRange = str(int(round(SilencedFinalHEAPRange,0))) \
                          + "("+str(int(round(SilencedBaseHEAPRange,0)))+")"

        TranqShortRange = str(FinalTranqRange) + "("+str(int(round(BaseTranqRange,0)))+")"
        MountTranqShortRange = str(int(round(MountFinalTranqRange,0))) \
                          + "("+str(int(round(MountBaseTranqRange,0)))+")"
        SilencedTranqShortRange = str(int(round(SilencedFinalTranqRange,0))) \
                          + "("+str(int(round(SilencedBaseTranqRange,0)))+")"

        ShotgunRateofFire = RateofFire + "(" + str(ShotgunBurst) + ")"

        FlechetteRateofFire = RateofFire + "(" + str(FlechetteBurst) + ")"

        if MagazineType == "cassette":
            MagazineListing = str(MagazineCap) + "C"
        else:
            MagazineListing = str(MagazineCap)

        if LaserSight == 1:
            if TechLevel == 8:
                LaserRange = 40
            else: # tech level 9+
                LaserRange = 240


        #damage table headers
        
        DamageTableheaders = "Round".ljust(24) +"ROF".ljust(6)+ "Dam Val".center(10)+ \
                             "Pen Rtg".center(10) + "Bulk".center(8) + "Magazine".center(10)\
                             + "SS Recoil".center(11) + "Burst Recoil".center(14) +\
                             "Short Range".center(13)

        #Ball ammo damage ouput
        if MountType == "Vehicle":
            BallLine =(AmmoBase+" Ball").ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(BaseDamageValue,0))).center(10) + Penetration.center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) + \
                   "0".center(11) + "0".center(14) + MountShortRange.center(13)
        else:
            BallLine = (AmmoBase+" Ball").ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(BaseDamageValue,0))).center(10) + Penetration.center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) + \
                   str(int(round(SSRecoil,0))).center(11) + \
                   str(BurstRecoil).center(14) + ShortRange.center(13)
        if MountType == "Bipod":
            BipodBallLine = "    Bipod".ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(BaseDamageValue,0))).center(10) + Penetration.center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) + \
                   str(int(round(SSRecoilMount,0))).center(11) + \
                   str(BurstRecoilMount).center(14) + MountShortRange.center(13) + '\n'
        else:
            BipodBallLine =""
        if MountType == "Tripod":                                           
            TripodBallLine = "    Tripod".ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(BaseDamageValue,0))).center(10) + Penetration.center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) +\
                   str(int(round(SSRecoilMount,0))).center(11) + \
                   str(BurstRecoilMount).center(14) + MountShortRange.center(13) + '\n'
        else:
            TripodBallLine =""
        if Silenced == 1:                                           
            SilencedBallLine = "    Silenced".ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(SilencedBaseDamageValue,0))).center(10) + \
                   SilencedPenetration.center(10) + Bulk.center(8) + \
                   MagazineListing.center(10) +\
                   str(int(round(SilencedSSRecoil,0))).center(11)\
                   + str(SilencedBurstRecoil).center(14) + \
                   SilencedShortRange.center(13) + '\n'
        else:
            SilencedBallLine =""

        #shotgun ammo damage ouput
        if MountType == "Vehicle":
            ShotgunLine =(AmmoBase+" Shot Short").ljust(24) + RateofFire.ljust(6)  + \
                    ShotgunShortDamage.center(10) + ShotgunPenetration.center(10)\
                    + Bulk.center(8) + MagazineListing.center(10) + \
                    "0".center(11) + "0".center(14) + MountShortRange.center(13)
        else:
            ShotgunLine = (AmmoBase+" Shot Short").ljust(24) + RateofFire.ljust(6)  + \
                    ShotgunShortDamage.center(10) + ShotgunPenetration.center(10)\
                    + Bulk.center(8) + MagazineListing.center(10) + \
                    str(int(round(SSRecoil,0))).center(11) + \
                    str(BurstRecoil).center(14) + ShortRange.center(13)

        ShotgunMedLine = "    Medium".ljust(24) + ShotgunRateofFire.ljust(6)  + \
                    str(ShotgunMediumDamage).center(10) + ShotgunPenetration.center(10)\
                    + Bulk.center(8) + MagazineListing.center(10) + \
                    str(int(round(SSRecoil,0))).center(11) + \
                    str(BurstRecoil).center(14) + ShortRange.center(13) + '\n'
                       
        if MountType == "Bipod":
            BipodShotgunLine = "    Bipod".ljust(24) + RateofFire.ljust(6)  + \
                    ShotgunShortDamage.center(10) + ShotgunPenetration.center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) + \
                   str(int(round(SSRecoilMount,0))).center(11) + \
                   str(BurstRecoilMount).center(14) + MountShortRange.center(13) + '\n'
        else:
            BipodShotgunLine =""
        if MountType == "Tripod":                                           
            TripodShotgunLine = "    Tripod".ljust(24) + RateofFire.ljust(6)  + \
                   ShotgunShortDamage.center(10) + ShotgunPenetration.center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) +\
                   str(int(round(SSRecoilMount,0))).center(11) + \
                   str(BurstRecoilMount).center(14) + MountShortRange.center(13) + '\n'
        else:
            TripodShotgunLine =""


        #DS ammo damage ouput
        if MountType == "Vehicle":
            DSLine = (AmmoBase+" DS").ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(BaseDamageValue,0))).center(10) + DSPenetration.center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) + \
                   "0".center(11) + "0".center(14) + MountDSShortRange.center(13)
        else:
            DSLine = (AmmoBase+" DS").ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(BaseDamageValue,0))).center(10) + DSPenetration.center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) + \
                   str(int(round(SSRecoil,0))).center(11) + \
                   str(BurstRecoil).center(14) + DSShortRange.center(13)
        if MountType == "Bipod":
            BipodDSLine = "    Bipod".ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(BaseDamageValue,0))).center(10) + DSPenetration.center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) + \
                   str(int(round(SSRecoilMount,0))).center(11) + \
                   str(BurstRecoilMount).center(14) + MountDSShortRange.center(13) + '\n'
        else:
            BipodDSLine =""
        if MountType == "Tripod":                                           
            TripodDSLine = "    Tripod".ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(BaseDamageValue,0))).center(10) + DSPenetration.center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) +\
                   str(int(round(SSRecoilMount,0))).center(11) + \
                   str(BurstRecoilMount).center(14) + MountDSShortRange.center(13) + '\n'
        else:
            TripodDSLine =""
        if Silenced == 1:                                           
            SilencedDSLine = "    Silenced".ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(SilencedBaseDamageValue,0))).center(10) + \
                   SilencedDSPenetration.center(10)+ Bulk.center(8) + \
                   MagazineListing.center(10) +\
                   str(int(round(SilencedSSRecoil,0))).center(11)\
                   + str(SilencedBurstRecoil).center(14) + \
                   SilencedDSShortRange.center(13) + '\n'
        else:
            SilencedDSLine =""

        #HE ammo damge ouput
        if MountType == "Vehicle":
            HELine =(AmmoBase+" HE").ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(HEAPDamageValue,0))).center(10) + "Nil".center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) + \
                   "0".center(11) + "0".center(14) + MountHEAPShortRange.center(13)
        else:
            HELine = (AmmoBase+" HE").ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(HEAPDamageValue,0))).center(10) + "Nil".center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) + \
                   str(int(round(SSRecoil,0))).center(11) + \
                   str(BurstRecoil).center(14) + HEAPShortRange.center(13)
        if MountType == "Bipod":
            BipodHELine = "    Bipod".ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(HEAPDamageValue,0))).center(10) + "Nil".center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) + \
                   str(int(round(SSRecoilMount,0))).center(11) + \
                   str(BurstRecoilMount).center(14) + MountHEAPShortRange.center(13) + '\n'
        else:
            BipodHELine =""
        if MountType == "Tripod":                                           
            TripodHELine = "    Tripod".ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(HEAPDamageValue,0))).center(10) + "Nil".center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) +\
                   str(int(round(SSRecoilMount,0))).center(11) + \
                   str(BurstRecoilMount).center(14) + MountHEAPShortRange.center(13) + '\n'
        else:
            TripodHELine =""
        if Silenced == 1:                                           
            SilencedHELine = "    Silenced".ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(SilencedHEAPDamageValue,0))).center(10) + \
                   "Nil".center(10)+ Bulk.center(8) + \
                   MagazineListing.center(10) +\
                   str(int(round(SilencedSSRecoil,0))).center(11)\
                   + str(SilencedBurstRecoil).center(14) + \
                   SilencedHEAPShortRange.center(13) + '\n'
        else:
            SilencedHELine =""

        #HEAP ammo damge ouput
        if MountType == "Vehicle":
            HEAPLine =(AmmoBase+" HEAP").ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(HEAPDamageValue,0))).center(10) + "2-2-2".center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) + \
                   "0".center(11) + "0".center(14) + MountHEAPShortRange.center(13)
        else:
            HEAPLine = (AmmoBase+" HEAP").ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(HEAPDamageValue,0))).center(10) + "2-2-2".center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) + \
                   str(int(round(SSRecoil,0))).center(11) + \
                   str(BurstRecoil).center(14) + HEAPShortRange.center(13)
        if MountType == "Bipod":
            BipodHEAPLine = "    Bipod".ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(HEAPDamageValue,0))).center(10) + "2-2-2".center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) + \
                   str(int(round(SSRecoilMount,0))).center(11) + \
                   str(BurstRecoilMount).center(14) + MountHEAPShortRange.center(13) + '\n'
        else:
            BipodHEAPLine =""
        if MountType == "Tripod":                                           
            TripodHEAPLine = "    Tripod".ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(HEAPDamageValue,0))).center(10) + "2-2-2".center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) +\
                   str(int(round(SSRecoilMount,0))).center(11) + \
                   str(BurstRecoilMount).center(14) + MountHEAPShortRange.center(13) + '\n'
        else:
            TripodHEAPLine =""
        if Silenced == 1:                                           
            SilencedHEAPLine = "    Silenced".ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(SilencedHEAPDamageValue,0))).center(10) + \
                   "2-2-2".center(10)+ Bulk.center(8) + \
                   MagazineListing.center(10) +\
                   str(int(round(SilencedSSRecoil,0))).center(11)\
                   + str(SilencedBurstRecoil).center(14) + \
                   SilencedHEAPShortRange.center(13) + '\n'
        else:
            SilencedHEAPLine =""   

        #Tranq ammo damge ouput
        if MountType == "Vehicle":
            TranqLine =(AmmoBase+" Tranq").ljust(24) + RateofFire.ljust(6)  + \
                   "-1*".center(10) + "Nil".center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) + \
                   "0".center(11) + "0".center(14) + MountTranqShortRange.center(13)
        else:
            TranqLine = (AmmoBase+" Tranq").ljust(24) + RateofFire.ljust(6)  + \
                   "-1*".center(10) + "Nil".center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) + \
                   str(int(round(SSRecoil,0))).center(11) + \
                   str(BurstRecoil).center(14) + TranqShortRange.center(13)
        if MountType == "Bipod":
            BipodTranqLine = "    Bipod".ljust(24) + RateofFire.ljust(6)  + \
                   "-1*".center(10) + "Nil".center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) + \
                   str(int(round(SSRecoilMount,0))).center(11) + \
                   str(BurstRecoilMount).center(14) + MountTranqShortRange.center(13) + '\n'
        else:
            BipodTranqLine =""
        if MountType == "Tripod":                                           
            TripodTranqLine = "    Tripod".ljust(24) + RateofFire.ljust(6)  + \
                   "-1*".center(10) + "Nil".center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) +\
                   str(int(round(SSRecoilMount,0))).center(11) + \
                   str(BurstRecoilMount).center(14) + MountTranqShortRange.center(13) + '\n'
        else:
            TripodTranqLine =""
        if Silenced == 1:                                           
            SilencedTranqLine = "    Silenced".ljust(24) + RateofFire.ljust(6)  + \
                   "-1*".center(10) + "Nil".center(10)+ Bulk.center(8) + \
                   MagazineListing.center(10) +\
                   str(int(round(SilencedSSRecoil,0))).center(11)\
                   + str(SilencedBurstRecoil).center(14) + \
                   SilencedTranqShortRange.center(13) + '\n'
        else:
            SilencedTranqLine =""

        #flechette ammo damage ouput
        if MountType == "Vehicle":
            FlechetteLine =(AmmoBase+" Flechette").ljust(24) + '\n'+ "    Short".ljust(24)  \
                            + RateofFire.ljust(6)  + \
                    FlechetteShortDamage.center(10) + FlechettePenetration.center(10)\
                    + Bulk.center(8) + MagazineListing.center(10) + \
                    "0".center(11) + "0".center(14) + MountShortRange.center(13)
        else:
            FlechetteLine =(AmmoBase+" Flechette").ljust(24) + '\n'+ "    Short".ljust(24)  \
                             + RateofFire.ljust(6)  + \
                    FlechetteShortDamage.center(10) + FlechettePenetration.center(10)\
                    + Bulk.center(8) + MagazineListing.center(10) + \
                    str(int(round(SSRecoil,0))).center(11) + \
                    str(BurstRecoil).center(14) + ShortRange.center(13)

        FlechetteMedLine = "    Medium".ljust(24) + FlechetteRateofFire.ljust(6)  + \
                    str(FlechetteMediumDamage).center(10) + FlechettePenetration.center(10)\
                    + Bulk.center(8) + MagazineListing.center(10) + \
                    str(int(round(SSRecoil,0))).center(11) + \
                    str(BurstRecoil).center(14) + ShortRange.center(13) + '\n'
                       
        if MountType == "Bipod":
            BipodFlechetteLine = "    Bipod".ljust(24) + RateofFire.ljust(6)  + \
                    FlechetteShortDamage.center(10) + FlechettePenetration.center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) + \
                   str(int(round(SSRecoilMount,0))).center(11) + \
                   str(BurstRecoilMount).center(14) + MountShortRange.center(13) + '\n'
        else:
            BipodFlechetteLine =""
        if MountType == "Tripod":                                           
            TripodFlechetteLine = "    Tripod".ljust(24) + RateofFire.ljust(6)  + \
                   FlechetteShortDamage.center(10) + FlechettePenetration.center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) +\
                   str(int(round(SSRecoilMount,0))).center(11) + \
                   str(BurstRecoilMount).center(14) + MountShortRange.center(13) + '\n'
        else:
            TripodFlechetteLine =""
        

        TranqExlainLine = "*1D-1 points of damage plus tranq effect on TNE, page 350."
        RangeExplainLine ="Range in parentheses is unrounded iron sight range."

        if MagazineType == "cassette":
            CassetteLine = "C stands for cassette magazine type"
        else:
            CassetteLine = ""
        AverageMuzzleLine = '\n' + "Average Muzzle Energy: " + str(round(AverageMuzzleEnergy,0)) + \
                            " joules (Tranq: " + str(round((AverageMuzzleEnergy *0.6),0)) \
                            + " joules)"

        if LaserSight == 1:
            LaserSightLine = '\n' + "Laser sight allows 3 aimed shots per turn and all"\
                             " others to be quick shots, out to " + str(LaserRange)+ "m"
        else:
            LaserSightLine = ""

        if MountType == "Vehicle":
            VehicleVolumeLine = '\n' + "This weapon takes up " + str(FinalLoadedWeight)+\
                                "L, when vehicle mounted"
        else:
            VehicleVolumeLine = ""

        if Small_Arms.WeaponTypeVar == "Shotgun":
            ShotgunDamageLine = ShotgunLine + '\n' + ShotgunMedLine + BipodShotgunLine\
                                + TripodShotgunLine
        else:
            ShotgunDamageLine =""

        if RotaryWeapon == 1:
            RotaryLine = '\n'+"This weapon is a rotary weapon with " + str(RotaryBarrels)\
                         + " barrels"
        else:
            RotaryLine =""

        
        # damage table output assembled 
        DamageTableOutput = DamageTableheaders + '\n' + BallLine + '\n' \
                            +BipodBallLine + TripodBallLine + SilencedBallLine\
                            + ShotgunDamageLine +  DSLine + '\n' \
                            +BipodDSLine + TripodDSLine + SilencedDSLine + HELine + '\n' \
                            +BipodHELine + TripodHELine + SilencedHELine + HEAPLine + '\n' \
                            +BipodHEAPLine + TripodHEAPLine + SilencedHEAPLine + TranqLine + '\n' \
                            +BipodTranqLine + TripodTranqLine + SilencedTranqLine \
                             + FlechetteLine + '\n' + FlechetteMedLine + BipodFlechetteLine \
                             + TripodFlechetteLine  + TranqExlainLine + '\n' \
                             + RangeExplainLine + RotaryLine + CassetteLine + AverageMuzzleLine \
                             + LaserSightLine + VehicleVolumeLine



#======================
# final output
#======================

        Small_Arms_Calcs.FinalDesign = NameLine + '\n' + TLLine + '\n' + AmmoLine + '\n' \
                                          + MuzzleLine + '\n' + WeaponLengthLine + '\n' + \
                                          WeaponWeightLine + '\n' + WeaponPriceLine + '\n' + \
                                          MagazineWeightLine + '\n' + MagazinePriceLine + '\n' \
                                          + AmmunitionPriceLine + '\n' + AmmunitionWeightLine \
                                          + '\n' + FeaturesLine + '\n' + TripodLine + \
                                          '\n' + DamageTableOutput

        Small_Arms_Calcs.AmmoWeight = AmmoWeight
        Small_Arms_Calcs.RecieverLength = RecieverLength
        Small_Arms_Calcs.AmmoLength = AmmoLength
        Small_Arms_Calcs.BarrelLength = BarrelLength
        Small_Arms_Calcs.StockLength = StockLength
        Small_Arms_Calcs.AverageMuzzleEnergy = AverageMuzzleEnergy
        Small_Arms_Calcs.AmmoDiameter = AmmoDiameter
        Small_Arms_Calcs.ShotgunBullets = ShotgunBullets
        Small_Arms_Calcs.FlechetteDarts = FlechetteDarts

        
        
