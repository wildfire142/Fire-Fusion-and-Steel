import math

class GaussWeaponsCalcs ():

    FinalDesign = str()
    GaussAmmoWeight = float()
    RecieverLength =float()
    AmmoDiameter = float()
    MagazineCap = int()
    MuzzleVelocity = int()
    
    def __init__(self, WidgetValues):

        self.WidgetValues = WidgetValues
        
        TechLevel = int(self.WidgetValues[0])
        WeaponName = str(self.WidgetValues[1])
        AmmoDiameter = float(self.WidgetValues[2])
        AmmoTypeVar = float(self.WidgetValues[3])
        MuzzleVelocity = int(self.WidgetValues[4])
        RateofFire = str(self.WidgetValues[5])
        MagazineCap = int(self.WidgetValues[6])
        StockType = str(self.WidgetValues[7])
        MountType = str(self.WidgetValues[8])
        MagazineType = str(self.WidgetValues[9])
        SightType = str(self.WidgetValues[10])
        RecoilAbsorb = str(self.WidgetValues[11])
        RecoilComp = str(self.WidgetValues[12])
        BayonetLug = int(self.WidgetValues[13])
        Grenade = int(self.WidgetValues[14])
        Silenced = int(self.WidgetValues[15])
        LaserSight = int(self.WidgetValues[17])
        Options = str()

#======================
# ammo design section
#======================
        GaussAmmoLength = AmmoDiameter*5 #in mm

        GaussAmmoWeight = 0.02*math.pi*pow((AmmoDiameter/2),3)

        GaussAmmoWeight = round(GaussAmmoWeight,2) # in grams

        GaussAmmoPrice = GaussAmmoWeight * AmmoTypeVar # in Credits


#======================
# Barrel figures
#======================

        BarrelTLMods = [1.6,1.3,1.0,0.8,0.6,0.6,0.4]

        if TechLevel >16:
           BarreLengthMult = 0.4
        else:
            BarreLengthMult = BarrelTLMods [TechLevel-10]

        GaussBarrelLength = MuzzleVelocity / 100*BarreLengthMult # in cm

        GaussBarrelWeight = 0.03*GaussBarrelLength # in kg

        GaussBarrelPrice = GaussBarrelWeight*600 # in Credits

        MuzzleEnergy = (0.5*GaussAmmoWeight*pow(MuzzleVelocity,2))/1000 # in joules

        EnergyEfficiencyMod = [3,2.4,2,1.8,1.6,1.6,1.4]

        if TechLevel >16:
           EnergyEfficiency = 1.4
        else:
            EnergyEfficiency = EnergyEfficiencyMod [TechLevel-10]

        RequiredEnergy = MuzzleEnergy*EnergyEfficiency # in joules


#======================
#Receiver figures
#======================

        ReceiverTLMods =[0.00016, 0.00012, 0.00010, 0.00009, 0.00008, 0.00007,0.00006,\
                         0.00005, 0.00004, 0.00003, 0.00002, 0.00001]
        ReceiverWeight = RequiredEnergy * ReceiverTLMods [TechLevel-10]

        if RateofFire == '5':
            ReceiverWeight = (ReceiverWeight * 1.1)
        elif RateofFire == '10':
            ReceiverWeight = (ReceiverWeight * 1.1)
        elif RateofFire == '5/10':
            ReceiverWeight = (ReceiverWeight * 1.2)
        elif RateofFire == '50':
            ReceiverWeight = (ReceiverWeight * 5)
        else:
            ReceiverWeight = ReceiverWeight

        RecieverLength = math.sqrt(1000*ReceiverWeight)

        if RecieverLength < (GaussAmmoLength/10):
            RecieverLength = GaussAmmoLength
        else:
            RecieverLength = RecieverLength


        if RateofFire == 'SA':
            ReceiverPrice = (ReceiverWeight * 100)
        else:
            ReceiverPrice = (ReceiverWeight * 100*1.2)


#======================
#stock figures
#======================

# in cm
        if StockType == "Pistol grip":
            StockLength = 0
        elif StockType == "Hollow pistol grip":
            StockLength = 0
        elif StockType == "Rifle stock":
            StockLength = 25
        else: #Bullpup rifle stock
            StockLength = 5

# in kg

        if StockType == "Pistol grip":
            StockWeight = 0.2
        elif StockType == "Hollow pistol grip":
            StockWeight = 0.1
        elif StockType == "Rifle stock":
            StockWeight = 0.5
        else: #Bullpup rifle stock
            StockWeight = 0.1

# in Cr

        if StockType == "Pistol grip":
            StockPrice = 5
        elif StockType == "Hollow pistol grip":
            StockPrice = 25
        elif StockType == "Rifle stock":
            StockPrice = 30
        else: #Bullpup rifle stock
            StockPrice = 10

#======================
#feed figures
#======================

        BatteryTLMods =[ 0.00001, 0.000009, 0.000006, 0.0000055, \
                         0.000004, 0.0000035, 0.000003,\
                         0.000003, 0.000003, 0.000003, 0.000003, 0.000003]

        BatteryWeight = MagazineCap * RequiredEnergy * BatteryTLMods [TechLevel-10] #in kg

        if RateofFire == 'SA':
            RoundsPerTurn = 1
        elif RateofFire == '5':
            RoundsPerTurn = 5
        elif RateofFire == '10':
            RoundsPerTurn = 10
        elif RateofFire == '5/10':
            RoundsPerTurn = 5
        else: # rate of fire 50
            RoundsPerTurn = 50

        if MountType == "Vehicle":
            if MagazineType == "Cassette":
                MagazineEmptyWeight = 2
                VehiclePower = ((MagazineCap * RequiredEnergy)/1000000)/(MagazineCap/RoundsPerTurn)
            else: #all other magazine types
                MagazineEmptyWeight = (0.0006 * ((MagazineCap+4) * \
                                                 GaussAmmoWeight))+ BatteryWeight
        else: #non vehicle mounts
            if MagazineType == "Cassette":
                MagazineEmptyWeight = 2 + BatteryWeight
            else: #all other magazine types
                MagazineEmptyWeight = (0.0006 * ((MagazineCap+4) * \
                                                 GaussAmmoWeight))+ BatteryWeight

        MagazineLoadedWeight = MagazineEmptyWeight + \
                               (MagazineCap*(GaussAmmoWeight/1000)) #in kg

        if MagazineType == "Cassette":
            MagazinePrice = math.ceil(10*MagazineEmptyWeight)
        else: #all other magazine types
            MagazinePrice = math.ceil(2*MagazineEmptyWeight)  


        MagazineLoadedPrice = MagazinePrice + (MagazineCap*GaussAmmoPrice)


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
            LaserSightMass = 0.5
            LaserSightPrice = 300
        else: #no laser sight fitted
            LaserSightMass = 0.0
            LaserSightPrice = 0            

#======================
# compensators Values
#======================

        if RecoilAbsorb == "Folding SA stock":
            RecoilAbsorbWeight = 0.2
            RecoilAbsorbPrice = 150
        elif RecoilAbsorb == "SA stock":
            RecoilAbsorbWeight = 0.2
            RecoilAbsorbPrice = 75
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

        if MuzzleEnergy < 1001:
            Penetration = "Nil"
        elif MuzzleEnergy < 3001:
            Penetration = "1-Nil"
        elif MuzzleEnergy < 5001:
            Penetration = "1-2-Nil"
        elif MuzzleEnergy < 10001:
            Penetration = "1-3-5"
        elif MuzzleEnergy < 20001:
            Penetration = "1-2-4"
        elif MuzzleEnergy < 50001:
            Penetration = "2-2-3"
        else:
            Penetration = "2-2-2"

#======================
# Range Values
#======================

        #stock and mount mods to range
        if StockType == "Pistol grip":
            RangeConfigMod = 0.5
        elif StockType == "Hollow pistol grip":
            RangeConfigMod = 0.5            
        elif StockType == "Bullpup rifle stock":
            RangeConfigMod = (0.9*1.6)
        else: # two handed weapons
            RangeConfigMod = 1.6
            
        if MountType == "Tripod":
            RangeConfigMod = 1.6
        if MountType == "Vehicle":
            RangeConfigMod = 1.6
            
        #base range calcs

        BaseShortRange = math.sqrt(MuzzleEnergy) * RangeConfigMod
        BaseTranqRange = BaseShortRange * 0.6
        BaseHEAPRange = BaseShortRange * 0.75

        #sight range adjustments

        if SightType == "Optic sights":
            FinalShortRange = BaseShortRange * 1.15
            FinalTranqRange = BaseTranqRange * 1.15
            FinalHEAPRange = BaseHEAPRange * 1.15
        elif SightType =="Telescopic sights":
            FinalShortRange = BaseShortRange + 15
            FinalTranqRange = BaseTranqRange + 15
            FinalHEAPRange = BaseHEAPRange + 15
        elif SightType =="Electronic sights":
            FinalShortRange = BaseShortRange + 20
            FinalTranqRange = BaseTranqRange + 20
            FinalHEAPRange = BaseHEAPRange + 20
        else: # iron sights
            FinalShortRange = BaseShortRange
            FinalTranqRange = BaseTranqRange
            FinalHEAPRange = BaseHEAPRange

        #Mount range adjustments

        if MountType == "Bipod":
            MountBaseShortRange = BaseShortRange * 1.3
            MountBaseTranqRange = BaseTranqRange * 1.3
            MountBaseHEAPRange = BaseHEAPRange * 1.3
            MountFinalShortRange = FinalShortRange * 1.3
            MountFinalTranqRange = FinalTranqRange * 1.3
            MountFinalHEAPRange = FinalHEAPRange * 1.3
        elif (MountType == "Tripod") or (MountType == "Vehicle"):
            MountBaseShortRange = BaseShortRange * 2
            MountBaseTranqRange = BaseTranqRange * 2
            MountBaseHEAPRange = BaseHEAPRange * 2
            MountFinalShortRange = FinalShortRange * 2
            MountFinalTranqRange = FinalTranqRange * 2
            MountFinalHEAPRange = FinalHEAPRange * 2
        else:
            MountBaseShortRange = 0
            MountBaseTranqRange = 0
            MountBaseHEAPRange =0
            MountFinalShortRange = 0
            MountFinalTranqRange = 0
            MountFinalHEAPRange = 0

#======================
# Final range adjustments
#======================

        # caping base ranges

        if BaseShortRange > 300:
            BaseShortRange = 300
        if BaseHEAPRange > 300:
            BaseHEAPRange = 300
        if BaseTranqRange > 30:
            BaseTranqRange = 30
        if MountBaseShortRange > 300:
            MountBaseShortRange = 300
        if MountBaseHEAPRange > 300:
            MountBaseHEAPRange = 300
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

        if MountFinalTranqRange > 30:
            MountFinalTranqRange = 30
        elif MountFinalTranqRange < 4:
            MountFinalTranqRange = 4
        else:
            MountFinalTranqRange = int(round(MountFinalTranqRange,0))

#======================
# Final values calculations
#======================

        FinalLength = round(GaussBarrelLength + RecieverLength + StockLength + \
                            GrenadeLength, 1)
        FinalEmptyWeight = round(GaussBarrelWeight + ReceiverWeight + StockWeight \
                                 + MagazineEmptyWeight + SightMass + LaserSightMass +\
                                 RecoilAbsorbWeight\
                                 + RecoilCompWeight + MountWeight, 3)
        FinalLoadedWeight = round (FinalEmptyWeight - MagazineEmptyWeight \
                                   + MagazineLoadedWeight, 3)
        FinalPrice = round(GaussBarrelPrice + ReceiverPrice + StockPrice + SightPrice\
                           + LaserSightPrice + RecoilAbsorbPrice + RecoilCompPrice + \
                           MountPrice + GrenadePrice, 2)
        MagazineLoadedWeight = round(MagazineLoadedWeight,4)
        MagazineEmptyWeight = round(MagazineEmptyWeight,4)
        MagazineLoadedPrice =round(MagazineLoadedPrice,2)
        MagazineType = MagazineType.lower()
        AmmoVelocity = int(MuzzleVelocity/100)

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
            

        if (SightOption != "") or (MountOption != "") or (BayonetOption != "") \
        or (GrenadeOption != "") or (SilencedOption != "") or (RecoilAbsorbOption !="") \
        or (RecoilCompOption != ""):
            Options = SightOption + MountOption + BayonetOption + \
                      GrenadeOption  + SilencedOption\
                      + RecoilAbsorbOption + RecoilCompOption
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
        else: # over 500001 muzzel energy
            MuzzelEnergyMod = 6

            #Set mod for compenstor types

        if RecoilAbsorb == "Folding SA stock":
            RecoilAbsorbMod = 0.9
        elif RecoilAbsorb == "SA stock":
            RecoilAbsorbMod = 0.85
        else: #no recoil absorber
            RecoilAbsorbMod = 1

        if RecoilComp == "Gyroscopic Compensator":
            RecoilCompMod = 0.5
        elif RecoilComp == "Inertial Compensator":
            RecoilCompMod = 0.3
        else: #no recoil compensator
            RecoilCompMod = 1

        RecoilMod = RecoilAbsorbMod*RecoilCompMod


        #Set mod for mount type

        MountMod = 1
        if MountType == "Bipod":
            MountMod = 0.5
        if MountType == "Tripod":
            MountMod = 0.25

        # set weapon weight dependant on feed type
        
        if MagazineType == "Cassette":
            RecoilWeight = FinalEmptyWeight
        else : #everything but cassette feeds
            RecoilWeight = FinalLoadedWeight

        # single shot recoil calc


        SSRecoil = (((0.15*math.sqrt(MuzzleEnergy))/RecoilWeight)+ \
                    MuzzelEnergyMod)* (0.5*RecoilMod)

        #calc for single shots on mounts

        if MountType == "Bipod":
            SSRecoilMount = SSRecoil * MountMod
        if MountType == "Tripod":
            SSRecoilMount = SSRecoil * MountMod
            
        # burst shot recoil calcs

        BurstRecoil5 = int(math.floor(((((2.5*(0.15*math.sqrt(MuzzleEnergy)))/RecoilWeight)+\
                       (2.5*MuzzelEnergyMod))*(0.5*RecoilMod))))

        BurstRecoil10 =int(math.floor(((((5*(0.15*math.sqrt(MuzzleEnergy)))/RecoilWeight)+\
                       (5*MuzzelEnergyMod))*(0.5*RecoilMod))))

        BurstRecoil50 =int(math.floor((((25*((0.15*math.sqrt(MuzzleEnergy)))/RecoilWeight)+\
                       (25*MuzzelEnergyMod))*(0.5*RecoilMod))))


        if RateofFire == '5':
            BurstRecoil  = BurstRecoil5
            BurstRecoilMount  = int(math.floor(BurstRecoil5)*MountMod)
        elif RateofFire == '10':
            BurstRecoil = BurstRecoil10
            BurstRecoilMount = int(math.floor(BurstRecoil10)*MountMod)
        elif RateofFire == '5/10':
            BurstRecoil = str(BurstRecoil5)+"/"\
                          +str(BurstRecoil10)
            BurstRecoilMount = str(int(math.floor(BurstRecoil5)*MountMod))+"/"\
                          +str(int(math.floor(BurstRecoil10)*MountMod))
        elif RateofFire == '50':
            BurstRecoil = BurstRecoil50
            BurstRecoilMount = int(math.floor(BurstRecoil50)*MountMod)
        else:
            BurstRecoil = str("-")
            BurstRecoilMount = str("-")

#======================
# tripod values
#======================
        
        if RateofFire == '5':
            TripodWeight = BurstRecoil5
        elif RateofFire == '10':
            TripodWeight = BurstRecoil10
        elif RateofFire == '5/10':
            TripodWeight = BurstRecoil10
        elif RateofFire == '50':
            TripodWeight = BurstRecoil50
        else:
            TripodWeight = 0

        TripodPrice = 50+(10*TripodWeight)

#======================
# silenced weapon values
#======================

        # silenced muzzle calc based on 300m muzzle velocity

        SilencedMuzzleEnergy = (0.5*GaussAmmoWeight*pow(300,2))/1000 # in joules

        # silenced weapon damage

        SilencedBaseDamageValue = round(math.sqrt(SilencedMuzzleEnergy)/15,0) 

        # damage for silenced HE and HEAP rounds

        SilencedHEAPDamageValue = pow((AmmoDiameter+TechLevel)-7,3)
        SilencedHEAPDamageValue = round(math.sqrt(SilencedHEAPDamageValue\
                                                  +SilencedMuzzleEnergy)/15,0)

        #silenced weapon penetration
        
        if SilencedMuzzleEnergy < 1001:
            SilencedPenetration = "Nil"
        elif SilencedMuzzleEnergy < 3001:
            SilencedPenetration = "1-Nil"
        elif SilencedMuzzleEnergy < 5001:
            SilencedPenetration = "1-2-Nil"
        elif SilencedMuzzleEnergy < 10001:
            SilencedPenetration = "1-3-5"
        elif SilencedMuzzleEnergy < 20001:
            SilencedPenetration = "1-2-4"
        elif SilencedMuzzleEnergy < 50001:
            SilencedPenetration = "2-2-3"
        else:
            SilencedPenetration = "2-2-2"

        #silenced weapon ranges

        SilencedBaseShortRange = math.sqrt(SilencedMuzzleEnergy) * RangeConfigMod
        SilencedBaseTranqRange = SilencedBaseShortRange * 0.6
        SilencedBaseHEAPRange = SilencedBaseShortRange * 0.75

        # range mods for ilenced weapons and optics etc

        SilencedFinalShortRange = FinalShortRange*(SilencedBaseShortRange/BaseShortRange)
        SilencedFinalTranqRange = (SilencedBaseTranqRange/BaseTranqRange)*FinalTranqRange
        SilencedFinalHEAPRange = (SilencedBaseHEAPRange/BaseHEAPRange)*FinalHEAPRange
        
        #Silenced recoil for single shot

        SilencedSSRecoil = (((0.15*math.sqrt(SilencedMuzzleEnergy))/RecoilWeight)+ \
                    MuzzelEnergyMod)* (0.5*RecoilMod)
            
        # Silenced burst shot recoil calcs

        SilencedBurstRecoil5 = int(math.floor(((((2.5*(0.15*math.sqrt(SilencedMuzzleEnergy)))\
                                         /RecoilWeight)+(2.5*MuzzelEnergyMod))\
                                       *(0.5*RecoilMod))))

        SilencedBurstRecoil10 =int(math.floor(((((5*(0.15*math.sqrt(SilencedMuzzleEnergy)))\
                                         /RecoilWeight)+(5*MuzzelEnergyMod))\
                                       *(0.5*RecoilMod))))

        SilencedBurstRecoil50 =int(math.floor((((25*((0.15*math.sqrt(SilencedMuzzleEnergy)))\
                                         /RecoilWeight)+ (25*MuzzelEnergyMod))\
                                       *(0.5*RecoilMod))))


        if RateofFire == '5':
            SilencedBurstRecoil  = SilencedBurstRecoil5
        elif RateofFire == '10':
            SilencedBurstRecoil = SilencedBurstRecoil10
        elif RateofFire == '5/10':
            SilencedBurstRecoil = str(SilencedBurstRecoil5)+"/"\
                          +str(SilencedBurstRecoil10)
        elif RateofFire == '50':
            SilencedBurstRecoil = SilencedBurstRecoil50
        else:
            SilencedBurstRecoil = str("-")

        #price adjustment for silenced weapons
        if Silenced == 1:
            FinalPrice = FinalPrice + ReceiverPrice
  
#======================
# Display line build up
#======================

        if AmmoDiameter - int(AmmoDiameter) != 0:
            AmmoBaseDiameter = AmmoDiameter
        else:
            AmmoBaseDiameter = int(AmmoDiameter)

        if GaussAmmoLength - int(GaussAmmoLength) != 0:
            BaseGaussAmmoLength = GaussAmmoLength
        else:
            BaseGaussAmmoLength = int(GaussAmmoLength)

        AmmoBase = str(AmmoBaseDiameter)+'x'+str(BaseGaussAmmoLength)+"mm"

        NameLine = "Designation: " + WeaponName
        TLLine = "TL: "+str(TechLevel)
        AmmoLine = "Ammo: "+ AmmoBase + "/"+str(AmmoVelocity)
        MuzzleLine = "Muzzle Energy: " + str(round(MuzzleEnergy,1)) + " joules (required power: " + \
                     str(round(RequiredEnergy,1)) + " joules)"
        WeaponLengthLine = "Weapon Length: " + str(FinalLength) + " cm"
        WeaponWeightLine = "Weapon Weight: " + str(FinalLoadedWeight) + " kg loaded, " + \
                           str(FinalEmptyWeight) + " kg empty (includes weight of empty "\
                           + MagazineType + ")"
        WeaponPriceLine = "Weapon Price: Cr" + str(round(FinalPrice,2))
        MagazineWeightLine = "Magazine Weight: " + str(MagazineLoadedWeight) +" kg loaded, "\
                             + str(MagazineEmptyWeight) + " kg empty"
        MagazinePriceLine = "Magazine Price: Cr" + str(MagazineLoadedPrice) + " (loaded), Cr" \
                            + str(MagazinePrice) + " (empty)" 
        AmmunitionPriceLine = "Ammunition Price: Cr" + str(round(GaussAmmoPrice,2)) + " (Dart), Cr"\
                              + str(round(2*GaussAmmoPrice,2)) + " (HE, Tranq), Cr" \
                              +str(round(3*GaussAmmoPrice,2))+ " (HEAP)"
        AmmunitionWeightLine = "Ammunition Weight: " + str(GaussAmmoWeight) + " grams per round"
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

        if MagazineType == "cassette":
            MagazineListing = str(MagazineCap) + "C"
        else:
            MagazineListing = str(MagazineCap)

        #damage table headers
        DamageTableheaders = "Round".ljust(24) +"ROF".ljust(6)+ "Dam Val".center(10)+ \
                             "Pen Rtg".center(10) + "Bulk".center(8) + "Magazine".center(10)\
                             + "SS Recoil".center(11) + "Burst Recoil".center(14) +\
                             "Short Range".center(13)

        #Dart ammo damage ouput
        if MountType == "Vehicle":
            DartLine =(AmmoBase+" Dart").ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(BaseDamageValue,0))).center(10) + Penetration.center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) + \
                   "0".center(11) + "0".center(14) + MountShortRange.center(13)
        else: DartLine = (AmmoBase+" Dart").ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(BaseDamageValue,0))).center(10) + Penetration.center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) + \
                   str(int(round(SSRecoil,0))).center(11) + \
                   str(BurstRecoil).center(14) + ShortRange.center(13)
        if MountType == "Bipod":
            BipodDartLine = "    Bipod".ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(BaseDamageValue,0))).center(10) + Penetration.center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) + \
                   str(int(round(SSRecoilMount,0))).center(11) + \
                   str(BurstRecoilMount).center(14) + MountShortRange.center(13) + '\n'
        else: BipodDartLine =""
        if MountType == "Tripod":                                           
            TripodDartLine = "    Tripod".ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(BaseDamageValue,0))).center(10) + Penetration.center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) +\
                   str(int(round(SSRecoilMount,0))).center(11) + \
                   str(BurstRecoilMount).center(14) + MountShortRange.center(13) + '\n'
        else: TripodDartLine =""
        if Silenced == 1:                                           
            SilencedDartLine = "    Silenced".ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(SilencedBaseDamageValue,0))).center(10) + \
                   SilencedPenetration.center(10) + Bulk.center(8) + \
                   MagazineListing.center(10) +\
                   str(int(round(SilencedSSRecoil,0))).center(11)\
                   + str(SilencedBurstRecoil).center(14) + \
                   SilencedShortRange.center(13) + '\n'
        else: SilencedDartLine =""

        #HE ammo damge ouput
        if MountType == "Vehicle":
            HELine =(AmmoBase+" HE").ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(HEAPDamageValue,0))).center(10) + "Nil".center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) + \
                   "0".center(11) + "0".center(14) + MountHEAPShortRange.center(13)
        else: HELine = (AmmoBase+" HE").ljust(24) + RateofFire.ljust(6)  + \
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
        else: BipodHELine =""
        if MountType == "Tripod":                                           
            TripodHELine = "    Tripod".ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(HEAPDamageValue,0))).center(10) + "Nil".center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) +\
                   str(int(round(SSRecoilMount,0))).center(11) + \
                   str(BurstRecoilMount).center(14) + MountHEAPShortRange.center(13) + '\n'
        else: TripodHELine =""
        if Silenced == 1:                                           
            SilencedHELine = "    Silenced".ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(SilencedHEAPDamageValue,0))).center(10) + \
                   "Nil".center(10)+ Bulk.center(8) + \
                   MagazineListing.center(10) +\
                   str(int(round(SilencedSSRecoil,0))).center(11)\
                   + str(SilencedBurstRecoil).center(14) + \
                   SilencedHEAPShortRange.center(13) + '\n'
        else: SilencedHELine =""

        #HEAP ammo damge ouput
        if MountType == "Vehicle":
            HEAPLine =(AmmoBase+" HEAP").ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(HEAPDamageValue,0))).center(10) + "2-2-2".center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) + \
                   "0".center(11) + "0".center(14) + MountHEAPShortRange.center(13)
        else: HEAPLine = (AmmoBase+" HEAP").ljust(24) + RateofFire.ljust(6)  + \
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
        else: BipodHEAPLine =""
        if MountType == "Tripod":                                           
            TripodHEAPLine = "    Tripod".ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(HEAPDamageValue,0))).center(10) + "2-2-2".center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) +\
                   str(int(round(SSRecoilMount,0))).center(11) + \
                   str(BurstRecoilMount).center(14) + MountHEAPShortRange.center(13) + '\n'
        else: TripodHEAPLine =""
        if Silenced == 1:                                           
            SilencedHEAPLine = "    Silenced".ljust(24) + RateofFire.ljust(6)  + \
                   str(int(round(SilencedHEAPDamageValue,0))).center(10) + \
                   "2-2-2".center(10)+ Bulk.center(8) + \
                   MagazineListing.center(10) +\
                   str(int(round(SilencedSSRecoil,0))).center(11)\
                   + str(SilencedBurstRecoil).center(14) + \
                   SilencedHEAPShortRange.center(13) + '\n'
        else: SilencedHEAPLine =""   

        #Tranq ammo damge ouput
        if MountType == "Vehicle":
            TranqLine =(AmmoBase+" Tranq").ljust(24) + RateofFire.ljust(6)  + \
                   "-1*".center(10) + "Nil".center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) + \
                   "0".center(11) + "0".center(14) + MountTranqShortRange.center(13)
        else: TranqLine = (AmmoBase+" Tranq").ljust(24) + RateofFire.ljust(6)  + \
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
        else: BipodTranqLine =""
        if MountType == "Tripod":                                           
            TripodTranqLine = "    Tripod".ljust(24) + RateofFire.ljust(6)  + \
                   "-1*".center(10) + "Nil".center(10)\
                   + Bulk.center(8) + MagazineListing.center(10) +\
                   str(int(round(SSRecoilMount,0))).center(11) + \
                   str(BurstRecoilMount).center(14) + MountTranqShortRange.center(13) + '\n'
        else: TripodTranqLine =""
        if Silenced == 1:                                           
            SilencedTranqLine = "    Silenced".ljust(24) + RateofFire.ljust(6)  + \
                   "-1*".center(10) + "Nil".center(10)+ Bulk.center(8) + \
                   MagazineListing.center(10) +\
                   str(int(round(SilencedSSRecoil,0))).center(11)\
                   + str(SilencedBurstRecoil).center(14) + \
                   SilencedTranqShortRange.center(13) + '\n'
        else: SilencedTranqLine =""

        TranqExlainLine = "*1D-1 points of damage plus tranq effect on TNE, page 350."
        RangeExplainLine ="Range in parentheses is unrounded iron sight range."

        if MagazineType == "cassette":
            CassetteLine = '\n' + "C stands for cassette magazine type"
        else:
            CassetteLine = ""

        if (MountType == "Vehicle") and (MagazineType == "cassette"):
            VehiclePowerLine = '\n' + "This weapon draws " + str(round(VehiclePower,2)) + \
                               "MW from the vehicle its mounted on"
        else:
            VehiclePowerLine = ""

        if LaserSight == 1:
            LaserSightLine = '\n' + "Laser sight allows 3 aimed shots per turn and all"\
                             " others to be quick shots, out to 240m"
        else:
            LaserSightLine = ""
        
        # damage table output assembled 
        DamageTableOutput = DamageTableheaders + '\n' + DartLine + '\n' \
                            +BipodDartLine + TripodDartLine + SilencedDartLine + HELine + '\n' \
                            +BipodHELine + TripodHELine + SilencedHELine + HEAPLine + '\n' \
                            +BipodHEAPLine + TripodHEAPLine + SilencedHEAPLine + TranqLine + '\n' \
                            +BipodTranqLine + TripodTranqLine + SilencedTranqLine + '\n' + \
                            TranqExlainLine + '\n' + RangeExplainLine + CassetteLine \
                            + VehiclePowerLine + LaserSightLine



#======================
# final output
#======================

        GaussWeaponsCalcs.FinalDesign = NameLine + '\n' + TLLine + '\n' + AmmoLine + '\n' \
                                          + MuzzleLine + '\n' + WeaponLengthLine + '\n' + \
                                          WeaponWeightLine + '\n' + WeaponPriceLine + '\n' + \
                                          MagazineWeightLine + '\n' + MagazinePriceLine + '\n' \
                                          + AmmunitionPriceLine + '\n' + AmmunitionWeightLine \
                                          + '\n' + FeaturesLine + '\n' + TripodLine + \
                                          '\n' + DamageTableOutput

        GaussWeaponsCalcs.GaussAmmoWeight = GaussAmmoWeight
        GaussWeaponsCalcs.RecieverLength = RecieverLength
        GaussWeaponsCalcs.AmmoDiameter = AmmoDiameter
        GaussWeaponsCalcs.MuzzleVelocity = MuzzleVelocity

        
