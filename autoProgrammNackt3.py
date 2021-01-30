
from datetime import datetime
#print(datetime.today().strftime('%Y'))


class Auto():
    marke="a2"
    MaxAutoID=0
    def __init__(self,a,m,k,np,lz,bj):
        self.marke=m
        self.kilometer=k
        self.baujahr=bj
        self.neupreis=np
        self.antrieb=a
        self.ladeZyklen=lz  
        Auto.MaxAutoID=Auto.MaxAutoID+1
        self.autoID=Auto.MaxAutoID+1
        #self.aa=Elektro("Elektro","mm", 100000,29999,970, 2020) 
        def __str__(self):
            return  "AutoID: " +str(self.autoID) \
                + ", Marke: " + str(self.marke) \
                + ", Kilmoterstand:" +str(self.kilometer)\
                + ", Neupreis:" + str(self.neupreis) \
                + ", Baujahr:" + str(self.baujahr) \
                + ", AutoID:" + str(self.autoID) \
                + ", Ladezyklen: " + str(self.ladeZyklen) \
                + ", Preis: "+ str(int(self.neupreis*(0.4*(max(0,(1000-self.ladeZyklen))/1000)**(2/3)+0.3*(max(0,(20-(int(datetime.today().strftime('%Y'))-int(self.baujahr)))/20))**2+0.3*(max(0,(300000-self.kilometer))/300000)**0.5)))  \
                
class Elektro(Auto):
    ladeZyklen=1 
    # ea=Elektro(abc,10000,1970,20000,100,e)
    def __init__(self,a,m,k,np,lz,bj):
        Auto.__init__(self,a,m,k,np,lz,bj)
        #self.aa=Elektro("Elektro","mm", 100000,29999,970, 2020) 
        #self.ladeZyklen=lz    
        # self.ea=Eauto
    def __str__(self):
        return  "AutoID: " +str(self.autoID) \
            + ", Marke: " + str(self.marke) \
            + ", Kilmoterstand:" +str(self.kilometer)\
            + ", Neupreis:" + str(self.neupreis) \
            + ", Baujahr:" + str(self.baujahr) \
            + ", AutoID:" + str(self.autoID) \
            + ", Ladezyklen: " + str(self.ladeZyklen) \
            + ", Preis: "+ str(int(self.neupreis*(0.4*(max(0,(1000-self.ladeZyklen))/1000)**(2/3)+0.3*(max(0,(20-(int(datetime.today().strftime('%Y'))-int(self.baujahr)))/20))**2+0.3*(max(0,(300000-self.kilometer))/300000)**0.5)))  \

class Hilfsklasse():
     aa=Auto("Elektro","mm", 100000,29999,970, 2020)
     def __init__ (self,ao):
         self.aa=ao
     # def __str__(self):
     #    return  "AutoID: " +str(self.autoID) \
     #        + ", Marke: " + str(self.marke) \
     #        + ", Kilmoterstand:" +str(self.kilometer)\
     #        + ", Neupreis:" + str(self.neupreis) \
     #        + ", Baujahr:" + str(self.baujahr) \
     #        + ", AutoID:" + str(self.autoID) \
     #        + ", Ladezyklen: " + str(self.ladeZyklen) \
        
         
class Bestand():     
    def __init__(self):
        self.bestandListe=[]
        #self.aa=auto("Elektro","mm", 100000,29999,970, 2020)             
    def Autohinzufuegen(self,ao):#a,m,k,np,lz,bj):#auto=Auto(a,Ibd)
        print("Modell hinzufuegen funktion aufgerufen")
        self.bestandListe.append(Hilfsklasse(ao))#a,m,k,np,lz,bj))   
        print("Modell hinzufuegen funktion ausgeführt")
    def loeschenAus(self,t):
       self.bestandListe.remove(t)
    def zeigeBestand (self):
        print("zeig Bestand befehl in modell aufgerufen")
        print(self.bestandListe,"XX")
        return[ e for e in self.bestandListe ]
        print("zeig bestand im modell ausgeführt")
    def zeigeBestandElektro (self):
        return[i for i in self.bestandListe if a==elektro]
    def printAuto(self,an):
        for a in self.bestandListe :
            if a==an:
                print

Auto1=Elektro("Elektro","test", 100, 20200, 1, 2020) 
#Bestand.Autohinzufuegen(("Elektro","test", 100, 20200, 1, 2020))
#def test(t):               
 #   t.Autohinzufuegen(("Elektro","test", 100, 20200, 1, 2020))
  #  t.Autohinzufuegen(("Elektro","rst", 1000, 20200, 10, 2014))
   # t.zeigeBestand(1)
#y.test(1)   
# A=Auto("Elektro","test", 100, 20200, 1, 2020)
B=Elektro("Elektro","rst", 1000, 20200, 10, 2014)
# C=Auto("Elektro","terrrst", 10000, 20200, 100, 2012)
# #="test", 100, 2020, 26000, 1, "e"
print(Auto1,"manueler befehl")
#print(bestandListe)
print(B)
# print(C)
# -*- coding: utf-8 -*-


