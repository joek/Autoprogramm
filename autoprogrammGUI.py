from tkinter import *
from tkinter import ttk
from autoProgrammNackt3 import *

################# Controller ############################
class AutoProgrammController():
    modellBestand = Bestand()
    BestandAnsicht = []
    
    def __init__(self):
        self.modellBestand.Autohinzufuegen(Auto("Elektro","test", 100, 20200, 1, 2020))
        self.modellBestand.Autohinzufuegen(Auto("Elektro","rst", 1000, 20200, 10, 2014))
        self.modellBestand.Autohinzufuegen(Auto("Elektro","terrrst", 10000, 20200, 100, 2012))
    
    def AutoHinzufuegen(self,a,m,k,np,lz,bj):
        print("controller aufgerufen")
        self.modellBestand.Autohinzufuegen(Auto(str(a),str(m),int(k),int(np),int(lz),int(bj)))
        print("hinzufuegen an modell weitergeleitet")
           
    def ZeigeBestandZurAnsicht(self):
        print("controller aufgerufen")
        self.BestandAnsicht = self.modellBestand.zeigeBestand()
        print("Controler ausgeführt")
        
################## View ##################################
class AutoGUI():

    def __init__(self):
        self.controller = AutoProgrammController()
        self.hauptfenster = Tk()
        self.hauptfenster.title("BestandsProgramm")
        
        self.hauptrahmen = ttk.Frame(self.hauptfenster)
        self.hauptrahmen.grid(column=0,
                              row=0,
                              rowspan=5,
                              columnspan=5)
           
        self.waehlenAlleButton = ttk.Button(
            self.hauptrahmen,text="Alle Autos",
            command=self.AlleWaehlen)
        self.waehlenAlleButton.grid(column=0,row=0)
        
        self.waehlenBenzinButton = ttk.Button(
            self.hauptrahmen,text="Benzin Autos",
            command=self.BenzinWaehlen)
        self.waehlenBenzinButton.grid(column=1,row=0)
        
        self.waehlenDieselButton = ttk.Button(
            self.hauptrahmen,text="Diesel Autos",
            command=self.DieselWaehlen)
        self.waehlenDieselButton.grid(column=2,row=0)

        self.waehlenElektroButton = ttk.Button(
            self.hauptrahmen,text="Elektro Autos",
            command=self.ElektroWaehlen)
        self.waehlenElektroButton.grid(column=3,row=0)

        self.AutoAnsichtTabelle = StringVar(value=[])
        self.AutosAnsicht = Listbox(
            self.hauptrahmen,
            listvariable=self.AutoAnsichtTabelle)
        self.AutosAnsicht.grid(
            column=0,
            row=2,
            columnspan=4,
            sticky=(N,S,E,W))

        self.hinzufuegenButton = ttk.Button(
            self.hauptrahmen,
            text="Hinzufuegen",
            command=self.NeuesAuto)
        self.hinzufuegenButton.grid(column=0,row=3)

        self.loeschenButton = ttk.Button(
            self.hauptrahmen,
            text="Loeschen",
            command=self.loescheAuto)
        self.loeschenButton.grid(column=1,row=3)

        self.beendenButton = ttk.Button(
            self.hauptrahmen,
            text="Programm beenden",
            command=self.hauptfenster.destroy)
        self.beendenButton.grid(column=2,row=3)

        self.hauptfenster.mainloop()

    def erneuereAnsicht(self):
        self.AutoAnsichtTabelle.set(
            self.controller.BestandAnsicht)
        
    def AlleWaehlen(self):
        self.controller.ZeigeBestandZurAnsicht() 
        print("zeige bestand im controller wird aufgerufen")         
        self.erneuereAnsicht()
        print("befehl komplett ausgefuert")
        
    def ElektroWaehlen(self):
        self.controller.ZeigeBestandZurAnsicht()          
        self.erneuereAnsicht()
        
    def BenzinWaehlen(self):
        self.controller.ZeigeBestandZurAnsicht()          
        self.erneuereAnsicht()
        
    def DieselWaehlen(self):
        self.controller.ZeigeBestandZurAnsicht()          
        self.erneuereAnsicht()
                
    def loescheAuto(self):
        self.controller.entferneAuto(
            self.AutoAnsichtTabelle.curselection()[0])
        self.erneuereAnsicht()
                      
    def NeuesAuto(self):
        addFenster = Tk()
        addFenster.title("Auto in Bestand aufnehmen")
        addRahmen = ttk.Frame(addFenster)
        addRahmen.grid(column=0,
                       row=0,
                       rowspan=3,
                       columnspan=5)
        addAntriebsart = ttk.Label(
            addRahmen,text="Antriebsart")
        addAntriebsart.grid(column=0, row=0)
        addMarke = ttk.Label(
            addRahmen,text="Marke")
        addMarke.grid(column=1, row=0)
        addKilometerstand = ttk.Label(
            addRahmen,text="Kilometerstand")
        addKilometerstand.grid(column=2, row=0)
        addNeupreis = ttk.Label(
            addRahmen,text="Neupreis")
        addNeupreis.grid(column=3, row=0)
        addLadezyklen = ttk.Label(
            addRahmen,text="wenn E-Auto: Ladezyklen")
        addLadezyklen.grid(column=4, row=0)
        addBaujahr = ttk.Label(
            addRahmen,text="Baujahr")
        addBaujahr.grid(column=5, row=0)

        addAntriebsartEingabe = ttk.Combobox(addRahmen)
        addAntriebsartEingabe["values"]=("Elektro","Benzin","Diesel")
        addAntriebsartEingabe.current(0)
        addAntriebsartEingabe.grid(column=0, row=1)
        addMarkeEingabe = ttk.Entry(
        addRahmen,width=40)
        addMarkeEingabe.insert(0,"ABC")
        addMarkeEingabe.grid(column=1, row=1)
        addKilometerstandEingabe = ttk.Entry(
            addRahmen,width=40)
        addKilometerstandEingabe.insert(0,200000)
        addKilometerstandEingabe.grid(column=2, row=1)
        addNeupreisEingabe = ttk.Entry(
            addRahmen,width=40)
        addNeupreisEingabe.insert(0, 30000)
        addNeupreisEingabe.grid(column=3, row=1)          
        addLadezyklenEingabe = ttk.Entry(
            addRahmen,width=40)
        addLadezyklenEingabe.insert(0,100)
        addLadezyklenEingabe.grid(column=4, row=1)
        addBaujahrEingabe = ttk.Entry(
            addRahmen,width=40)
        addBaujahrEingabe.insert(0,2015)
        addBaujahrEingabe.grid(column=5, row=1) 
  
        OKButton = ttk.Button(
            addRahmen,text="OK",
            command= lambda : self.addAuto(
                addAntriebsartEingabe.get(),
                addMarkeEingabe.get(),
                addKilometerstandEingabe.get(),
                addNeupreisEingabe.get(),
                addLadezyklenEingabe.get(),
                addBaujahrEingabe.get(),
                addFenster))
        OKButton.grid(column=1,row=2)
        cancelButton = ttk.Button(
            addRahmen,text="Cancel",
            command=addFenster.destroy)
        cancelButton.grid(column=2,row=2)
        addFenster.mainloop()

    def addAuto(self,a,m,k,np,lz,bj,fenster):
        print("eingabe fenster ausgelesen")
        self.controller.AutoHinzufuegen(a,m,k,np,lz,bj)
        print("erzeugt")
        #self.AlleWaehlen()
        fenster.destroy()
################## Main Program #############################
Start = AutoGUI()   
